# # 这是转角双层石墨烯的连续模型和紧束缚模型的代码整理，里面包含了一些功能实现，如吸收谱，拉曼光谱等。
# # 这部分为在计算当中需要用到的常数
from public.consts import *
from public.method import *


class ContiTbgInst:  # # 连续性模型的核心代码
    # # 若干常量的定义
    
    if 'SLURM_CPUS_PER_TASK' in os.environ:
        cores_num = int(os.environ['SLURM_CPUS_PER_TASK'])
    else:
        cores_num = multiprocessing.cpu_count()
    print("Cores Num: ", cores_num)

    interval_k = 0.005

    b_p_arr = array([sqrt(3) / 2, 3 / 2])
    b_n_arr = array([-sqrt(3) / 2, 3 / 2])

    gamma0_arr = array([0, 0])
    gamma1_arr = array([-sqrt(3) / 2, 3 / 2])
    gamma2_arr = array([-sqrt(3), 0])
    k_b_arr = array([-sqrt(3) / 2, -1 / 2])
    k_t_arr = array([-sqrt(3) / 2, 1 / 2])
    m_1_arr = array([-sqrt(3) / 2, 0])
    m_2_arr = array([-sqrt(3) / 4, 3 / 4])

    # # k空间的路径定义
    default_paths = [[k_b_arr, k_t_arr, gamma1_arr, gamma0_arr, k_b_arr],
                     [k_b_arr, k_t_arr, gamma1_arr, gamma2_arr, k_b_arr],
                     [k_b_arr, gamma0_arr, m_1_arr, k_t_arr]]
    default_path_labels = [[r"$K_b$", r"$K_t$", r"$\Gamma$", r"$\Gamma$", r"$K_b$"],
                           [r"$K_b$", r"$K_t$", r"$\Gamma$", r"$\Gamma$", r"$K_b$"],
                           [r"$K_b$", r"$\Gamma$", r"$M$", r"$K_t$"]]

    # # 初始化及可选参数定义
    def __init__(self, twist_angle_conti, v_F=1e6, w=118, kp_num=70, raman_gamma=100, ab_delta=100,
                 e_phonon=196, a0_constant=1.42 * sqrt(3), basis_loop_times=7, density_per_path=100):  # m/s for v_F, meV for w
        self.density_per_path = density_per_path
        self.twist_angle_conti = twist_angle_conti
        self.twist_theta_conti = twist_angle_conti / 180 * pi

        self.a0_constant_conti = a0_constant
        self.unit_origin_cell_area_conti = sqrt(3) / 2 * self.a0_constant_conti ** 2
        self.norm_KG_conti = 4 * pi / (3 * self.a0_constant_conti)

        self.aM_lattice_conti = self.a0_constant_conti / (2 * sin(self.twist_theta_conti / 2))
        self.unit_moire_cell_area_conti = sqrt(3) / 2 * self.aM_lattice_conti ** 2
        self.norm_Kg_conti = abs(4 * pi / (3 * self.aM_lattice_conti))

        self.v_F = v_F
        self.epsilon = h_bar_eV * self.v_F * self.norm_Kg_conti * m2A * eV2meV
        self.w = w

        self.kp_num = kp_num
        self.N_k = int(kp_num ** 2)

        self.raman_gamma = raman_gamma
        self.e_phonon = e_phonon
        self.ab_delta = ab_delta
        self.ab_renorm_const = 2 * c_eV ** 2 / (h_bar_eV * c_speed * epsilon_0) / self.N_k / self.unit_moire_cell_area_conti

        self.pre_basis_list = self.basis_set(basis_loop_times)
        self.pre_basis_layer_base = [ele_basis for ele_basis in self.pre_basis_list if ele_basis[2] == 1]
        self.pre_basis_layer_twist = [ele_basis for ele_basis in self.pre_basis_list if ele_basis[2] == 2]
        self.inter_h_12, self.inter_h_21 = self.inter_h_pre_mat()
        self.intra_h1_k, self.intra_h2_k = self.intra_h_pre_k_mat()
        # print(len(self.pre_basis_list))

        self.mat_type = 'TBG'

    # # 底层石墨烯哈密顿量定义，k矢量已经旋转
    def h_b(self, k):
        x_wave = k[0] - self.k_b_arr[0]
        y_wave = k[1] - self.k_b_arr[1]
        return self.epsilon * array(
            [
                [0, (x_wave - 1j * y_wave) * exp(-1j * self.twist_theta_conti / 2)],
                [(x_wave + 1j * y_wave) * exp(1j * self.twist_theta_conti / 2), 0]
            ]
        )

    # # 顶层石墨烯哈密顿量定义，k矢量已经旋转
    def h_t(self, k):
        x_wave = k[0] - self.k_t_arr[0]
        y_wave = k[1] - self.k_t_arr[1]
        return self.epsilon * array(
            [
                [0, (x_wave - 1j * y_wave) * exp(1j * self.twist_theta_conti / 2)],
                [(x_wave + 1j * y_wave) * exp(-1j * self.twist_theta_conti / 2), 0]
            ]
        )

    # # 层间耦合矩阵1
    def t_0(self):
        return self.w * array(
            [
                [1, 1],
                [1, 1]
            ]
        )

    # # 层间耦合矩阵2
    def t_p1(self):
        return self.w * array(
            [
                [1, exp(-2j * pi / 3)],
                [exp(2j * pi / 3), 1]
            ]
        )

    # # 层间耦合矩阵3
    def t_n1(self):
        return self.w * array(
            [
                [1, exp(2j * pi / 3)],
                [exp(-2j * pi / 3), 1]
            ]
        )

    # # 1层至2层k点的耦合
    @staticmethod
    def layer1to2(vec):  # (the number of b_p, the number of b_n)
        v1 = (vec[0], vec[1], 2)  # the same wave vector
        v2 = (vec[0] + 1, vec[1], 2)  # plus a b_p
        v3 = (vec[0], vec[1] + 1, 2)  # plus a b_n
        return v1, v2, v3

    # # 2层至1层k点的耦合
    @staticmethod
    def layer2to1(vec):
        v1 = (vec[0], vec[1], 1)  # the same wave vector
        v2 = (vec[0] - 1, vec[1], 1)  # minus a b_p
        v3 = (vec[0], vec[1] - 1, 1)  # minus a b_n
        return v1, v2, v3

    # # 基矢构建
    @staticmethod
    def basis_set(loop_times):  # create the basis of calculation
        t1 = time.perf_counter()
        layer1_basis = [(0, 0, 1)]
        layer1_to_2 = True
        layer2_basis = []
        layer2_to_1 = False
        times = 0
        layer1_new_basis = [(0, 0, 1)]
        layer2_new_basis = []
        while times < loop_times:
            times = times + 1
            if layer1_to_2 and (not layer2_to_1):
                new_layer2_basis_list = [ele_tuple + array([[0, 0, 1], [1, 0, 1], [0, 1, 1]]) for ele_tuple in layer1_new_basis]
                tmp_array_mat = array(new_layer2_basis_list).reshape(-1, 3)
                new_basis_tuples = set([tuple(ele) for ele in tmp_array_mat])
                layer2_new_basis = list(new_basis_tuples - (new_basis_tuples & set(layer2_basis)))
                layer2_basis.extend(list(new_basis_tuples))
                layer1_to_2 = False
                layer2_to_1 = True
            elif layer2_to_1 and (not layer1_to_2):
                new_layer1_basis_list = [ele_tuple + array([[0, 0, -1], [-1, 0, -1], [0, -1, -1]]) for ele_tuple in layer2_new_basis]
                tmp_array_mat = array(new_layer1_basis_list).reshape(-1, 3)
                new_basis_tuples = set([tuple(ele) for ele in tmp_array_mat])
                layer1_new_basis = list(new_basis_tuples - (new_basis_tuples & set(layer1_basis)))
                layer1_basis.extend(list(new_basis_tuples))
                layer1_to_2 = True
                layer2_to_1 = False
        output_basis = list(set(layer1_basis) | set(layer2_basis))
        return output_basis

    def intra_h_pre_k_mat(self):
        h1_diagonal_term = [ele_basis[0] * self.b_p_arr + ele_basis[1] * self.b_n_arr - self.k_b_arr for ele_basis in self.pre_basis_layer_base]
        h1_mat = h1_diagonal_term
        h2_diagonal_term = [ele_basis[0] * self.b_p_arr + ele_basis[1] * self.b_n_arr - self.k_t_arr for ele_basis in self.pre_basis_layer_twist]
        h2_mat = h2_diagonal_term
        return array(h1_mat), array(h2_mat)
    
    def inter_h_pre_mat(self):
        mat_in_list = []
        for layer1_basis in self.pre_basis_layer_base:
            row = []
            for layer2_basis in self.pre_basis_layer_twist:
                if layer2_basis == (layer1_basis[0], layer1_basis[1], 2):
                    row.append(self.t_0())
                elif layer2_basis == (layer1_basis[0] + 1, layer1_basis[1], 2):
                    row.append(self.t_p1())
                elif layer2_basis == (layer1_basis[0], layer1_basis[1] + 1, 2):
                    row.append(self.t_n1())
                else:
                    row.append(zeros((2, 2)))
            mat_in_list.append(row)
        return block(mat_in_list), conj(block(mat_in_list)).T

    def diag_h_construct(self, k_arr):
        h1_plus_k = k_arr + self.intra_h1_k
        h2_plus_k = k_arr + self.intra_h2_k
        
        intra_h1_mat = [PubMeth.sigma_angle_dot_p(ele_arr, self.twist_angle_conti / 2) for ele_arr in h1_plus_k]
        intra_h2_mat = [PubMeth.sigma_angle_dot_p(ele_arr, -self.twist_angle_conti / 2) for ele_arr in h2_plus_k]

        return self.epsilon * block_diag(*intra_h1_mat), self.epsilon * block_diag(*intra_h2_mat)
    
    def hamiltonian_construction(self, k_arr):
        intra_h_1, intra_h_2 = self.diag_h_construct(k_arr)
        out_mat = [
            [intra_h_1, self.inter_h_12],
            [self.inter_h_21, intra_h_2]
        ]
        return block(out_mat)

    # # k空间路径描述
    def path_depiction(
            self,
            i,
            point1,
            point2,
            out_list,
            multi_process='off',
            hint=False):
        k_along = PubMeth.path_between_two_vec(point1, point2, density=int(norm(point1 - point2) * self.density_per_path))
        if multi_process == 'on':
            value_list = []
            for kp in k_along:
                eig_v_f= np.linalg.eig(
                    self.hamiltonian_construction(kp))[0]
                eig_v_f.sort()
                value_list.append(eig_v_f)
                if hint:
                    print("Complete: ", kp)
            value_list.append(i)
            out_list.append(value_list)
            print("Complete: ", point1, " to ", point2)

    # # k空间路径坐标构建
    def label_pos(self, path_list):
        pos_list = [0]
        for ii in range(len(path_list) - 1):
            number_of_points = int(self.density_per_path *
                                   sqrt((path_list[ii +
                                                   1][1] -
                                         path_list[ii][1]) ** 2 +
                                        (path_list[ii +
                                                   1][0] -
                                         path_list[ii][0]) ** 2))
            next_pos = pos_list[-1] + number_of_points
            pos_list.append(next_pos)
        return pos_list

    # # 多进程计算k空间路径能带，每条路径一个核计算
    def multi_proc_path(self, kp_path_list, save_or_not=False, y_range=[-1000, 1000], line_type='k-', x_labs=[], show_or_not=False, lw=1, hold_on=False, figsize=(7,5), comm_angle_in_title=None, delta_angle_in_title=None, shift_energy=True, test_mode=False, selected_bds_index_list=[], hint=False):
        x_label_pos = PubMeth.situate_x_labels(kp_path_list, self.density_per_path)
        out_eig_list_f = multiprocessing.Manager().list()
        path_num = len(kp_path_list) - 1
        p_f = Pool(path_num)
        path_depiction = functools.partial(self.path_depiction, hint=hint)
        for i in range(path_num):
            p_f.apply_async(path_depiction, args=(
                i, kp_path_list[i], kp_path_list[i + 1], out_eig_list_f, 'on'))
        print('Waiting for all subprocesses done...')
        p_f.close()
        p_f.join()
        print('All subprocesses done.')
        total_energy_list = []
        for path_i in range(path_num):
            for ele_path in out_eig_list_f:
                if ele_path[-1] == path_i:
                    total_energy_list.extend(ele_path[0:-1])
        
        if isinstance(shift_energy, bool):
            half_energy = PubMeth.find_half_filling_energy(total_energy_list)
            if shift_energy:
                shifted_energy_list = array(total_energy_list) - half_energy
            else:
                shifted_energy_list = array(total_energy_list)

            if (not comm_angle_in_title) and (comm_angle_in_title != 0):
                figure_title = r"Band structure for $\theta={:.3f} \degree$".format(self.twist_angle_conti)
                save_title = 'conti_band_{:.3f}_{}'.format(self.twist_angle_conti, self.mat_type)
                PubMeth.plot_energies(real(shifted_energy_list), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='conti_energies_{:.4f}_{}'.format(self.twist_angle_conti, self.mat_type))
            else:
                if not delta_angle_in_title:
                    figure_title = r"Band structure for $\theta={:.3f} \degree$".format(comm_angle_in_title)
                    save_title = 'conti_band_{:.3f}_{}'.format(comm_angle_in_title, self.mat_type)
                    PubMeth.plot_energies(real(shifted_energy_list), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='conti_energies_{:.4f}_{}'.format(self.twist_angle_conti, self.mat_type))
                else:
                    figure_title = r"$\theta_0={:.5f} \degree, \delta \theta = {:e} \degree$".format(comm_angle_in_title, delta_angle_in_title)
                    save_title = 'conti_band_{:.3f}_{:e}'.format(comm_angle_in_title, delta_angle_in_title)
                    PubMeth.plot_energies(real(shifted_energy_list), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='conti_energies_{:.4f}_{:.e}'.format(comm_angle_in_title, self.twist_angle_conti))

            return shifted_energy_list  # total_energy_list is un-shifted energy list
        else:
            shift_energy = array(total_energy_list) - shift_energy
            if (not comm_angle_in_title) and (comm_angle_in_title != 0):
                figure_title = r"Band structure for $\theta={:.3f} \degree$".format(self.twist_angle_conti)
                save_title = 'conti_band_{:.3f}_{}'.format(self.twist_angle_conti, self.mat_type)
                PubMeth.plot_energies(real(shift_energy), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='conti_energies_{:.4f}_{}'.format(self.twist_angle_conti, self.mat_type))
            else:
                if not delta_angle_in_title:
                    figure_title = r"Band structure for $\theta={:.3f} \degree$".format(comm_angle_in_title)
                    save_title = 'conti_band_{:.3f}_{}'.format(comm_angle_in_title, self.mat_type)
                    PubMeth.plot_energies(real(shift_energy), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='conti_energies_{:.4f}'.format(self.twist_angle_conti, self.mat_type))
                else:
                    figure_title = r"$\theta_0={:.3f} \degree, \delta \theta = {:e} \degree$".format(comm_angle_in_title, delta_angle_in_title)
                    save_title = 'conti_band_{:.3f}_{:e}'.format(comm_angle_in_title, delta_angle_in_title)
                    PubMeth.plot_energies(real(shift_energy), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='energies_{:.4f}_{:e}'.format(comm_angle_in_title, self.twist_angle_conti))
            return total_energy_list

    # # 布里渊区k点的定义
    def moire_b_zone(self, kp_num):  # # kp_num 为菱形边长上k点的数目
        kp_list_f = []
        for ele_m in arange(0, 1, 1 / kp_num):
            for ele_n in arange(0, 1, 1 / kp_num):
                k_p = ele_m * self.b_p_arr + ele_n * self.b_n_arr
                kp_list_f.append(k_p)
        return kp_list_f

    @staticmethod
    def rect_moire_b_zone(kp_num):
        kp_list = []
        for ele_x in arange(-sqrt(3) / 2, sqrt(3) / 2, sqrt(3) / kp_num):
            for ele_y in arange(-1 / 2, 1, 3 / (2 * kp_num)):
                kp_list.append(array([ele_x, ele_y]))
        return kp_list

    # # 将布里渊区的k点分成若干个列表
    def divide_kp_list(self):
        all_kp_list_f = self.moire_b_zone(self.kp_num)
        kp_part_list_f = []
        for i in range(self.cores_num - 1):
            kp_part_list_f.append(all_kp_list_f[int(len(
                all_kp_list_f) / self.cores_num) * i:int(len(all_kp_list_f) / self.cores_num) * (i + 1)])
        kp_part_list_f.append(all_kp_list_f[int(
            len(all_kp_list_f) / self.cores_num) * (self.cores_num - 1):])
        return kp_part_list_f

    def part_e_dic(
            self,
            i,
            point_list,
            out_list,
            multi_process='off'):
        if multi_process == 'off':
            all_energy_list = []
            dic = {}
            for k_index, k_point in enumerate(point_list):
                eig_v= np.linalg.eig(
                    self.hamiltonian_construction(k_point))[0]
                eig_v.sort()
                dic[(k_point[0], k_point[1])] = eig_v
                all_energy_list.extend(eig_v)
            return dic, all_energy_list
        elif multi_process == 'on':
            print("The # ", i, "process is running")
            all_energy_list = []
            dic = {}
            for k_index, k_point in enumerate(point_list):
                eig_v= np.linalg.eig(
                    self.hamiltonian_construction(k_point))[0]
                eig_v.sort()
                dic[(k_point[0], k_point[1])] = eig_v
                all_energy_list.extend(eig_v)
            out_list.append(all_energy_list)

    def get_fermi_vel(self):
        e_at_k = eig(
            self.hamiltonian_construction(self.k_b_arr))[0]
        e_at_k.sort()
        e_c1_k = e_at_k[int(len(e_at_k) / 2)]
        e_at_m = eig(
            self.hamiltonian_construction(self.m_1_arr))[0]
        e_at_m.sort()
        e_c1_m = e_at_m[int(len(e_at_m) / 2)]
        Delta_E = e_c1_m - e_c1_k
        Delta_k = norm(self.m_1_arr - self.k_b_arr) * self.norm_Kg_conti
        return real(Delta_E / (Delta_k * h_bar_eV * m2A * eV2meV))  # m/s

    def multi_proc_all_e(
            self,
            kp_part_list_f,
            save_or_not=False):
        out_eig_list_f = multiprocessing.Manager().list()
        p_f = Pool(self.cores_num)
        for i in range(self.cores_num):
            p_f.apply_async(
                self.part_e_dic,
                args=(
                    i,
                    kp_part_list_f[i],
                    out_eig_list_f,
                    'on'))
        print('Waiting for all subprocesses done...')
        p_f.close()
        p_f.join()
        print('All subprocesses done.')
        total_energy_list = []
        for ele_e_list in out_eig_list_f:
            total_energy_list.extend(ele_e_list)
        if save_or_not:
            target_dir = PubMeth.get_right_save_path("Dat")
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
            np.save(
                target_dir +
                "conti_tbg_%.2f_all_e.npy" %
                self.twist_angle_conti,
                total_energy_list)
        return total_energy_list

    def plot_along_path(
            self,
            path=0,
            labels=0,
            yrange=[-2000, 2000],
            line_s='k-',
            lw=1,
            save_or_not=True,
            show=False,
            hold_or_not=False,
            figsize=(7, 5),
            shift_or_not=True,
            test_mode=True,
            selected_bds=[]):
        if isinstance(path, int):
            self.multi_proc_path(self.default_paths[path], x_labs=self.default_path_labels[path], y_range=yrange, line_type=line_s, lw=lw, save_or_not=save_or_not, show_or_not=show, hold_on=hold_or_not, shift_energy=shift_or_not, test_mode=test_mode, selected_bds_index_list=selected_bds)
        else:
            self.multi_proc_path(
                path, save_or_not=save_or_not, x_labs=labels, y_range=yrange, line_type=line_s, lw=lw, show_or_not=show, hold_on=hold_or_not, figsize=figsize, shift_energy=shift_or_not, test_mode=test_mode, selected_bds_index_list=selected_bds)

    def raman_i_cal(self, k_point_arr, num_half_f, e_photon, hint=False):
        cent_h = self.hamiltonian_construction(k_point_arr)
        partial_hx = (
                             self.hamiltonian_construction(
                                 (k_point_arr[0] + self.interval_k,
                                  k_point_arr[1])) - cent_h) / (self.interval_k * self.norm_Kg_conti)
        partial_hy = (
                             self.hamiltonian_construction(
                                 (k_point_arr[0],
                                  k_point_arr[1] + self.interval_k)) - cent_h) / (self.interval_k * self.norm_Kg_conti)

        eig_v, eig_a = eig(cent_h)

        mid_i = len(eig_v) // 2

        v_energy_list = eig_v[argsort(real(eig_v))[mid_i - num_half_f : mid_i]]
        v_states_list = eig_a.T[argsort(real(eig_v))[mid_i - num_half_f:mid_i]]

        c_energy_list = eig_v[argsort(real(eig_v))[mid_i : mid_i + num_half_f]]
        c_states_list = eig_a.T[argsort(real(eig_v))[mid_i:mid_i + num_half_f]]

        term_h_x = conj(c_states_list) @ partial_hx @ v_states_list.T
        term_h_y = conj(c_states_list) @ partial_hy @ v_states_list.T
        trans_list = (abs(term_h_x) ** 2 + abs(term_h_y) ** 2)
        e_diff_list = array([ele_c_e - v_energy_list for ele_c_e in c_energy_list])

        raman_term_list = array(trans_list) / (
                (e_photon - array(e_diff_list) - 1j * self.raman_gamma) * (
                    e_photon - self.e_phonon - array(e_diff_list) - 1j * self.raman_gamma))
        raman_i = raman_term_list.sum()
        if hint:
            print("Complete: ", k_point_arr)
        return raman_i

    def multi_proc_raman_i_cal(self, args_list, figs_save=True, hint=False, save_mat=False, mod_pics_save_dir="raman_pics_mod"):
        """
        :param args_list: [num_half, e_photon]
        :return:
        """
        parts_list = self.divide_kp_list()
        raman_i_cal = functools.partial(self.raman_i_cal, hint=hint)
        all_list = PubMeth.multi_proc_func(
            raman_i_cal, parts_list, args_list)
        im_mat = array(all_list).reshape((self.kp_num, self.kp_num))
        if figs_save:
            PubMeth.rect2diam(real(im_mat), "Conti_raman_theta_%.2f" % self.twist_angle_conti, r"$\theta = %.2f \degree$" % self.twist_angle_conti, save_2d_plots=figs_save, save_mat=save_mat, mod_pics_save_dir=mod_pics_save_dir)
            
        return abs(im_mat.sum()) ** 2 / self.unit_moire_cell_area_conti ** 2

    def ab_cal(self, k_point_arr, num_half_f, e_photon_list):
        cent_h = self.hamiltonian_construction(k_point_arr)
        partial_hx = (
                             self.hamiltonian_construction(
                                 (k_point_arr[0] + self.interval_k,
                                  k_point_arr[1])) - cent_h) / (self.interval_k * self.norm_Kg_conti)
        partial_hy = (
                             self.hamiltonian_construction(
                                 (k_point_arr[0],
                                  k_point_arr[1] + self.interval_k)) - cent_h) / (self.interval_k * self.norm_Kg_conti)

        eig_v, eig_a = eig(cent_h)
        vv_dic = {}
        for i_f in range(len(eig_v)):
            vv_dic[eig_v[i_f]] = eig_a.T[i_f]

        eig_v.sort()
        mid_i = len(eig_v) // 2
        chosen_energy = []
        states_list = []
        for i_b in range(-num_half_f, num_half_f):
            chosen_energy.append(eig_v[mid_i + i_b])
            states_list.append(vv_dic[eig_v[mid_i + i_b]])

        v_energy_list = chosen_energy[:num_half_f]
        c_energy_list = chosen_energy[num_half_f:]

        v_states_list = states_list[:num_half_f]
        c_states_list = states_list[num_half_f:]

        e_diff_list = []

        trans_list = []
        for i1 in range(len(v_states_list)):
            for i2 in range(len(c_states_list)):
                term1 = dot(
                    dot(conj(c_states_list[i2]), partial_hx), v_states_list[i1])
                term2 = dot(
                    dot(conj(c_states_list[i2]), partial_hy), v_states_list[i1])
                e_diff_list.append(c_energy_list[i2] - v_energy_list[i1])
                trans_list.append(abs(term1) ** 2 + abs(term2) ** 2)

        ab_along_e = []
        for ele_photon in e_photon_list:
            tmp_term = array(trans_list) * self.ab_delta / \
                           ((array(e_diff_list) - ele_photon) ** 2 + self.ab_delta ** 2)
            tmp_sum = tmp_term.sum() / ele_photon
            ab_along_e.append(tmp_sum)
        return ab_along_e

    def multi_proc_ab_cal(self, args_list):
        """
        :param args_list: [num_half, e_photon_list]
        :return:
        """
        dir_name = PubMeth.get_right_save_path('absorption')
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        parts_list = self.divide_kp_list()
        ab_all_k_along_e = PubMeth.multi_proc_func(self.ab_cal, parts_list, args_list)

        out_ab = zeros(len(args_list[-1]))
        for ele_along in ab_all_k_along_e:
            out_ab = out_ab + array(ele_along) * self.ab_renorm_const

        plt.figure(figsize=(6, 4))
        plt.plot(args_list[-1], real(out_ab))
        ax = plt.gca()
        ax.set_xlabel('E(meV)', fontsize=12)
        ax.set_ylabel('Absorption', fontsize=12)
        ax.set_title('The absorption of {:.3f}-{}'.format(self.twist_angle_conti, self.mat_type), fontsize=14)
        plt.xlim(ax.get_xlim())
        plt.ylim(ax.get_ylim())
        plt.savefig(dir_name + "ab_{:.3f}_{}.svg".format(self.twist_angle_conti, self.mat_type), dpi=300, facecolor='w')
        plt.close()

        trace1 = go.Scatter(x=args_list[-1], y=real(out_ab))
        layout = PubMeth.plotly_layout()
        fig = go.Figure(data=[trace1], layout=layout)
        fig.write_html(dir_name + 'ab_{:.3f}_{}_.html'.format(self.twist_angle_conti, self.mat_type))

        return out_ab

    def multi_proc_ab_2d(self, args_list, figs_save=True):
        """
        :param args_list: [num_half, e_photon_list]
        :return:
        """
        parts_list = self.divide_kp_list()
        ab_all_k_along_e = PubMeth.multi_proc_func(self.ab_cal, parts_list, args_list)
        ab_all_k_along_e = array(ab_all_k_along_e)
        out_ab = []
        for i in range(len(args_list[-1])):
            chosen_e = args_list[-1][i]
            chosen_mat = real(ab_all_k_along_e)[:, i].reshape((self.kp_num, self.kp_num))
            PubMeth.rect2diam(chosen_mat, "Conti_e_%.2f" % chosen_e, r"$E=%.2f meV$" % chosen_e, save_2d_plots=figs_save)
            print("Complete: ", args_list[-1][i], "meV")
            out_ab.append(ab_all_k_along_e[:, i].sum() * self.ab_renorm_const)

        return out_ab

    def berry_cur_niumeth(self, kp_arr, band_i):

        if band_i > 0:
            chosen_band_i = len(self.pre_basis_list) + band_i - 1
        else:
            chosen_band_i = len(self.pre_basis_list) + band_i

        cent_h = self.hamiltonian_construction(kp_arr)
        e_v, e_a = eig(cent_h)
        vector_n = e_a.T[np.argsort(real(e_v))[chosen_band_i]]
        e_n = e_v[np.argsort(real(e_v))[chosen_band_i]]

        other_n_pri = list(e_a.T)
        other_e = list(e_v)
        other_n_pri.pop(np.argsort(real(e_v))[chosen_band_i])
        other_e.pop(np.argsort(real(e_v))[chosen_band_i])

        par_h_kx = (self.hamiltonian_construction(array([kp_arr[0] + self.interval_k, kp_arr[1]])) - cent_h) / (self.interval_k * self.norm_Kg_conti)
        par_h_ky = (self.hamiltonian_construction(array([kp_arr[0], kp_arr[1] + self.interval_k])) - cent_h) / (self.interval_k * self.norm_Kg_conti)

        t1 = time.time()
        out_result = 0
        for ele_i in range(len(other_e)):
            tmp_e = other_e[ele_i]
            tmp_n_pri = other_n_pri[ele_i]

            mat_n_n_pri = tmp_n_pri.reshape(-1, 1) @ conj(tmp_n_pri.reshape(1, -1))
            cent_mat_xy = par_h_kx @ mat_n_n_pri @ par_h_ky
            cent_mat_yx = par_h_ky @ mat_n_n_pri @ par_h_kx
            term_xy = conj(vector_n.reshape(1, -1)) @ cent_mat_xy @ vector_n
            term_yx = conj(vector_n.reshape(1, -1)) @ cent_mat_yx @ vector_n
            out_result = out_result + (term_xy - term_yx) / (real(e_n - tmp_e)) ** 2

        print(time.time() - t1)
        print("Complete: ", kp_arr)
        return out_result * 1j

    def multi_proc_chern_num_niumeth(self, kp_density, args_list):
        """
        :param kp_density: num of points along a side of MBZ
        :param args_list: [band_i]
        :return:
        """
        # all_kps = self.moire_b_zone(kp_density)
        all_kps = self.rect_moire_b_zone(kp_density)
        print("N_k: ", len(all_kps))
        all_parts = PubMeth.divide_list(all_kps)
        berry_cur_list = PubMeth.multi_proc_func(self.berry_cur_niumeth, all_parts, args_list)
        return sum(berry_cur_list) / (len(all_kps) * self.unit_moire_cell_area_conti) * 2 * pi

    def multi_proc_berry_2d_niumeth(self, kp_density, args_list):
        """
        :param kp_density: num points along a side of MBZ
        :param args_list: [band_i]
        :return:
        """
        xy_list = []
        for ele_y in linspace(1, -1, kp_density):
            for ele_x in linspace(-sqrt(3) / 2, sqrt(3) / 2, kp_density):
                xy_list.append(array([ele_x, ele_y]))

        print("N_k: ", len(xy_list))
        all_parts = PubMeth.divide_list(xy_list)
        berry_list = PubMeth.multi_proc_func(self.berry_cur_niumeth, all_parts, args_list)
        im_mat = array(berry_list).reshape((kp_density, kp_density))
        return real(im_mat)

    def berry_cur_jmeth(self, k_arr, band_i, kp_num):

        delta_space = 1 / kp_num

        delta_kx = self.b_p_arr[0] * delta_space * 2
        delta_ky = self.b_p_arr[1] * delta_space

        if band_i > 0:
            chosen_band_i = len(self.pre_basis_list) + band_i - 1
        else:
            chosen_band_i = len(self.pre_basis_list) + band_i

        cent_h = self.hamiltonian_construction(k_arr)
        e_v, e_a = eig(cent_h)
        cent_vec = e_a[:, np.argsort(real(e_v))[chosen_band_i]]

        delta_kx_h = self.hamiltonian_construction(k_arr + array([delta_kx, 0]))
        e_v, e_a = eig(delta_kx_h)
        delta_kx_vec = e_a[:, np.argsort(real(e_v))[chosen_band_i]]

        delta_ky_h = self.hamiltonian_construction(array(k_arr + array([0, delta_ky])))
        e_v, e_a = eig(delta_ky_h)
        delta_ky_vec = e_a[:, np.argsort(real(e_v))[chosen_band_i]]

        delta_kx_ky_h = self.hamiltonian_construction(k_arr + array([delta_kx, delta_ky]))
        e_v, e_a = eig(delta_kx_ky_h)
        delta_kx_ky_vec = e_a[:, np.argsort(real(e_v))[chosen_band_i]]

        Ux = dot(conj(cent_vec), delta_kx_vec) / abs(dot(conj(cent_vec), delta_kx_vec))
        Uy = dot(conj(cent_vec), delta_ky_vec) / abs(dot(conj(cent_vec), delta_ky_vec))
        Ux_y = dot(conj(delta_ky_vec), delta_kx_ky_vec) / abs(dot(conj(delta_ky_vec), delta_kx_ky_vec))
        Uy_x = dot(conj(delta_kx_vec), delta_kx_ky_vec) / abs(dot(conj(delta_kx_vec), delta_kx_ky_vec))

        F_12 = cmath.log(Ux * Uy_x * (1 / Ux_y) * (1 / Uy))
        # print("Complete: ", k_arr)
        return F_12

    def multi_proc_chern_num_jmeth(self, args_list, save_2d_plot=True, mat_2d_save=True):
        """
        :param args_list: [band_i, kp_num]
        :return:
        """
        all_kps = self.moire_b_zone(args_list[-1])
        all_parts = PubMeth.divide_list(all_kps)
        berry_cur_list = PubMeth.multi_proc_func(self.berry_cur_jmeth, all_parts, args_list)
        chern_num = 1j * sum(berry_cur_list) / (2 * pi)
        if save_2d_plot:
            PubMeth.rect2diam(-array(imag(berry_cur_list)).reshape((args_list[-1], args_list[-1])), file_name="berry_2D_{}_chern_num_{:.2f}".format(self.mat_type, real(chern_num)), title_name="Chern Number={:.2f}, N={:.0f}".format(real(chern_num), len(all_kps)), save_2d_plots=save_2d_plot, save_in_case_same_name=True, rm_raw=True, save_mat=mat_2d_save)
        print('Chern number: ', chern_num)
        return chern_num


class TightTbgInst:  # # 紧束缚模型核心代码
    if 'SLURM_CPUS_PER_TASK' in os.environ:
        cores_num = int(os.environ['SLURM_CPUS_PER_TASK'])
    else:
        cores_num = multiprocessing.cpu_count()
    print("Cores Num: ", cores_num)
    interval_k = 0.00001

    expand_vecs = [array([1, 0]), array([0, 1]), array(
        [-1, 0]), array([0, -1]), array([1, -1]), array([-1, 1])]

    def __init__(self, m0, r, t_intra=-2700, t_inter=480, ab_delta=20, kp_num=70,
                 dyn_cond_eta=20, raman_gamma=100, e_phonon=196, a0=1.42 * sqrt(3), d0=3.35, density_per_path=100, atoms_within_unit_cell=4):  # eV for two couplings
        self.mat_type = 'TBG'
        self.twist_angle_cos = (3 * m0 ** 2 + 3 * m0 * r + r ** 2 /
                          2) / (3 * m0 ** 2 + 3 * m0 * r + r ** 2)
        self.twist_angle_sin = sqrt(1 - self.twist_angle_cos ** 2)
        self.twist_angle = np.arccos(self.twist_angle_cos) / pi * 180
        self.twist_theta = np.arccos(self.twist_angle_cos)
        self.e_phonon = e_phonon

        self.a0_const = a0
        self.atoms_within_unit_cell = atoms_within_unit_cell
        # # rotate the basis to form a symmetric unit cell
        # self.a1 = PubMeth.rotation(-self.theta / 2) @ (self.a0 * array([sqrt(3) / 2, -1 / 2]))
        # self.a2 = PubMeth.rotation(-self.theta / 2) @ (self.a0 * array([sqrt(3) / 2, 1 / 2]))
        # self.b1 = PubMeth.rotation(-self.theta / 2) @ (2 * pi / a0 * array([1 / sqrt(3), -1]))
        # self.b2 = PubMeth.rotation(-self.theta / 2) @ (2 * pi / a0 * array([1 / sqrt(3), 1]))
        self.a1 = self.a0_const * array([sqrt(3) / 2, -1 / 2])
        self.a2 = self.a0_const * array([sqrt(3) / 2, 1 / 2])
        self.b1 = 2 * pi / a0 * array([1 / sqrt(3), -1])
        self.b2 = 2 * pi / a0 * array([1 / sqrt(3), 1])
        self.delta = (self.a1 + self.a2) / 3
        self.r_a1 = self.a1 * (self.twist_angle_cos - self.twist_angle_sin /
                               sqrt(3)) + self.a2 * 2 * self.twist_angle_sin / sqrt(3)
        self.r_a2 = self.a2 * (self.twist_angle_cos + self.twist_angle_sin /
                               sqrt(3)) - self.a1 * 2 * self.twist_angle_sin / sqrt(3)
        self.r_delta = (self.r_a1 + self.r_a2) / 3

        self.d0 = d0
        self.delta_0_par = 0.184 * self.a0_const
        self.m0 = m0
        self.r = r
        self.kp_num = kp_num
        self.Nk = int(kp_num ** 2)

        self.t_intra = t_intra
        self.t_inter = t_inter

        if self.r % 3 != 0:
            self.R_1 = self.m0 * self.a1 + (self.m0 + self.r) * self.a2
            self.R_2 = -(self.m0 + self.r) * self.a1 + \
                       (2 * self.m0 + self.r) * self.a2
            self.G_1 = ((2 * self.m0 + self.r) * self.b1 + (self.m0 + self.r) *
                        self.b2) / (3 * self.m0 ** 2 + 3 * self.m0 * self.r + self.r ** 2)
            self.G_2 = (-(self.m0 + self.r) * self.b1 + self.m0 * self.b2) / (
                    3 * self.m0 ** 2 + 3 * self.m0 * self.r + self.r ** 2)
            self.n_atoms = int(self.atoms_within_unit_cell * (3 * m0 ** 2 + 3 * m0 * r + r ** 2))
        else:
            n = self.r // 3
            self.R_1 = (self.m0 + n) * self.a1 + n * self.a2
            self.R_2 = -n * self.a1 + (self.m0 + 2 * n) * self.a2
            self.G_1 = ((self.m0 + 2 * n) * self.b1 + n * self.b2) / \
                       (self.m0 ** 2 + self.m0 * self.r + self.r ** 2 / 3)
            self.G_2 = (-n * self.b1 + (self.m0 + n) * self.b2) / \
                       (self.m0 ** 2 + self.m0 * self.r + self.r ** 2 / 3)
            self.n_atoms = int(self.atoms_within_unit_cell * (m0 ** 2 + m0 * r + r ** 2 / 3))
        
        self.n_unit_cells = int((m0 ** 2 + m0 * r + r ** 2 / 3))

        self.K_1 = (self.G_1 + 2 * self.G_2) / 3
        self.K_2 = (2 * self.G_1 + self.G_2) / 3
        self.M = (self.K_1 + self.K_2) / 2

        self.a_M_comm = norm(self.R_1)
        self.unit_moire_comm = sqrt(3) / 2 * self.a_M_comm ** 2

        self.a_M_conti = self.a0_const / (2 * sin(self.twist_theta / 2))
        self.unit_moire_conti = sqrt(3) / 2 * self.a_M_conti ** 2

        self.ab_renorm_const = c_eV ** 2 / h_bar_eV / c_speed / epsilon_0 / self.unit_moire_comm / self.Nk
        self.dyn_conda_renorm_const = 1 / self.Nk / self.unit_moire_comm * c_eV ** 2 / h_bar_eV / sigma_xx_mono * 2
        self.density_per_path = density_per_path / np.linalg.norm(self.K_1)
        self.ab_delta = ab_delta
        self.dyn_cond_eta = dyn_cond_eta
        self.raman_gamma = raman_gamma
        self.sup_vec_list = [array([0, 0]), self.R_1, self.R_2, -self.R_1, -self.R_2, self.R_2 - self.R_1, self.R_1 - self.R_2,
                             self.R_1 + self.R_2, -self.R_1 - self.R_2, 2 * self.R_2 - self.R_1, self.R_1 - 2 * self.R_2,
                             2 * self.R_1 - self.R_2, self.R_2 - 2 * self.R_1]
        
        self.sup_vec_3d_list = [array([*ele_arr, 0]) for ele_arr in self.sup_vec_list]

        self.Kg = norm(self.K_1)
        self.path_gamma = array([0, 0])

        self.indices_of_lattice = self.lattice_indices()
        self.positions_of_atoms_test = self.atom_positions()
        self.value_cos_mat, self.dists_arr_mat = self.atom_relations()

        self.positions_of_atoms = self.atom_positions_origin()
        self.relations_of_atoms = self.atom_relations_origin()

        self.V_pppi = self.couple_V_pppi()
        self.V_ppsigma = self.couple_V_ppsigma()

        self.K_energy_wavefunc_pair = np.linalg.eig(self.hamiltonian_construction(self.K_1))
        self.K_energy = self.K_energy_wavefunc_pair[0]
        self.K_energy.sort()
        self.ref_energy = (self.K_energy[len(self.K_energy) // 2] + self.K_energy[len(self.K_energy) // 2 - 1]) / 2

        self.default_paths = [
            [self.K_1, self.path_gamma, self.M, self.K_2],
            [self.path_gamma, self.G_2, 2 * self.K_1, self.K_1, self.path_gamma]
        ]
        self.default_path_labels = [
            [r"$K_1$", r"$\Gamma$", r"$M$", r"$K_2$"],
            [r"$\Gamma$", r"$G_2$", r"$K_2$", r"$K_1$", r"$\Gamma$"]
        ]
        

    def lattice_indices(self):
        def create_index(loop_times):
            initial = [(0, 0)]
            new_vecs = []
            i_flag = 0
            while i_flag < loop_times:
                i_flag = i_flag + 1
                if len(new_vecs) == 0:
                    for e_vec in self.expand_vecs:
                        new_vecs.append((e_vec[0], e_vec[1]))
                    initial.extend(new_vecs)
                else:
                    tmp_new_vecs = []
                    for old_vec in new_vecs:
                        for e_vec in self.expand_vecs:
                            tmp_vec = old_vec + e_vec
                            tmp_new_vecs.append((tmp_vec[0], tmp_vec[1]))
                    tmp_new_vecs = list(set(tmp_new_vecs))
                    out_vecs = []
                    for vec_f in tmp_new_vecs:
                        if vec_f not in initial:
                            out_vecs.append(vec_f)
                    new_vecs = out_vecs[:]
                    initial.extend(out_vecs)
            return initial
        i = 1
        loop_index_list = create_index(i)
        while (self.m0, self.m0 + self.r) not in loop_index_list:
            i = i + 1
            loop_index_list = create_index(i)
        return loop_index_list
    
    def arrange_bound_p(self):
        R_3 = self.R_2 - self.R_1
        return [(0, 0), (R_3[0], R_3[1]), (self.R_2[0],
                                           self.R_2[1]), (self.R_1[0], self.R_1[1]), (0, 0)]

    def atom_positions(self):
        atoms_tuple = []
        bound_list_f = self.arrange_bound_p()
        for ele_index in self.indices_of_lattice:
            A1 = ele_index[0] * self.a1 + ele_index[1] * self.a2
            B1 = ele_index[0] * self.a1 + ele_index[1] * self.a2 + self.delta
            A2 = ele_index[0] * self.r_a1 + ele_index[1] * self.r_a2
            B2 = ele_index[0] * self.r_a1 + \
                 ele_index[1] * self.r_a2 + self.r_delta
            if PubMeth.isInterArea(
                    A1, bound_list_f) and not PubMeth.at_corners(
                A1, bound_list_f):
                atoms_tuple.append((*A1, 0))
            if PubMeth.isInterArea(
                    B1, bound_list_f) and not PubMeth.at_corners(
                B1, bound_list_f):
                atoms_tuple.append((*B1, 0))
            if PubMeth.isInterArea(
                    A2, bound_list_f) and not PubMeth.at_corners(
                A2, bound_list_f):
                atoms_tuple.append((*A2, self.d0))
            if PubMeth.isInterArea(
                    B2, bound_list_f) and not PubMeth.at_corners(
                B2, bound_list_f):
                atoms_tuple.append((*B2, self.d0))
        atoms_tuple.append((0, 0, 0))
        atoms_tuple.append((0, 0, self.d0))
        return atoms_tuple
    
    def atom_relations(self):
        relations_arr_list = []
        value_cos_list = []
        for bra_p in self.positions_of_atoms_test:
            for ket_p in self.positions_of_atoms_test:
                dist_arr = array(ket_p) - array(bra_p)
                minimum_vec = PubMeth.get_smallest_distance(dist_arr, self.sup_vec_3d_list)
                tmp_value_cos = minimum_vec[-1] / norm(minimum_vec)
                value_cos_list.append(tmp_value_cos)
                relations_arr_list.append(minimum_vec)
        out_value_cos_mat = array(value_cos_list).reshape((self.n_atoms, self.n_atoms))
        rows, cols = np.diag_indices_from(out_value_cos_mat)
        out_value_cos_mat[rows, cols] = 0
        return out_value_cos_mat, array(relations_arr_list)

    def couple_V_pppi(self):
        V_pppi_mat = (self.t_intra * exp(- (norm(self.dists_arr_mat, axis=1) - self.a0_const / sqrt(3)) / self.delta_0_par)).reshape((self.n_atoms, self.n_atoms))
        V_pppi_mat = V_pppi_mat - diag(diag(V_pppi_mat))
        return V_pppi_mat

    def couple_V_ppsigma(self):
        V_ppsigma_mat = (self.t_inter * exp(- (norm(self.dists_arr_mat, axis=1) - self.d0) / self.delta_0_par)).reshape((self.n_atoms, self.n_atoms))
        V_ppsigma_mat = V_ppsigma_mat - diag(diag(V_ppsigma_mat))
        return V_ppsigma_mat

    def hamiltonian_construction(self, k_arr_f):
        t1 = time.perf_counter()
        k_dot_dist_arr_list = (k_arr_f * self.dists_arr_mat[:, :2]).sum(axis=1)
        phase_term = exp(-1j * k_dot_dist_arr_list).reshape((self.n_atoms, self.n_atoms))
        h_mat = (self.V_pppi * (1 - self.value_cos_mat ** 2) + self.V_ppsigma * self.value_cos_mat ** 2) * phase_term
        return h_mat

    def plot_atoms(self, save_or_not=True, fig_format='.svg', super_cell_view=True):
        layer1_atoms = []
        layer2_atoms = []
        for ele_index in self.indices_of_lattice:
            layer1_atoms.append(
                ele_index[0] *
                self.a1 +
                ele_index[1] *
                self.a2)
            layer1_atoms.append(
                ele_index[0] *
                self.a1 +
                ele_index[1] *
                self.a2 +
                self.delta)
            layer2_atoms.append(
                ele_index[0] *
                self.r_a1 +
                ele_index[1] *
                self.r_a2)
            layer2_atoms.append(
                ele_index[0] *
                self.r_a1 +
                ele_index[1] *
                self.r_a2 +
                self.r_delta)

        cor_x1 = array(layer1_atoms)[:, 0]
        cor_y1 = array(layer1_atoms)[:, 1]
        cor_x2 = array(layer2_atoms)[:, 0]
        cor_y2 = array(layer2_atoms)[:, 1]
        bound = self.arrange_bound_p()

        plt.scatter(cor_x1, cor_y1, marker='.')
        plt.scatter(cor_x2, cor_y2, marker='.')
        plt.plot(array(bound)[:, 0], array(bound)[:, 1], color='red')

        ax = plt.gca()
        ax.set_aspect('equal')
        plt.title(r"Atomic Structure of Twisted Bilayer Graphene. $\theta=%.3f \degree$" % self.twist_angle, fontsize=14)
        plt.xlabel("X($\AA$)", fontsize=12)
        plt.ylabel("Y($\AA$)", fontsize=12)
        if save_or_not:
            save_dir = PubMeth.get_right_save_path('structures')
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            plt.savefig(save_dir + "Atomic_structure_%.2f_%s" % (self.twist_angle, self.mat_type) + fig_format, dpi=300)
        if super_cell_view:
            ax = plt.gca()
            ax.set_xlabel('', fontsize=12)
            ax.set_ylabel('', fontsize=12)
            ax.set_title('', fontsize=14)
            plt.xlim([min([ele[0] for ele in bound]), max([ele[0] for ele in bound])])
            plt.ylim([min([ele[1] for ele in bound]), max([ele[1] for ele in bound])])
            plt.savefig(save_dir + "supercell_view_{:.3f}_{}".format(self.twist_angle, self.mat_type) + fig_format, dpi=300, facecolor='w')
        plt.close()
        
        trace1 = go.Scatter(x=cor_x1, y=cor_y1, mode='markers')
        trace2 = go.Scatter(x=cor_x2, y=cor_y2, mode='markers')
        layout = PubMeth.plotly_layout()
        fig = go.Figure(data=[trace1, trace2], layout=layout)
        fig.update_yaxes(scaleanchor = "x", scaleratio = 1,)
        fig.write_html(save_dir + 'atomic_structure_{:.3f}_{}.html'.format(self.twist_angle, self.mat_type))

    def plot_MBZ(self, save_or_not=True, fig_format='.svg'):
        vex_list = [self.K_1, self.K_2, self.K_2 - self.K_1, -self.K_1, -self.K_2, self.K_1 - self.K_2, self.K_1]
        PubMeth.draw_box(vex_list)
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.text(self.K_1[0], self.K_1[1], "K1")
        ax.text(self.K_2[0], self.K_2[1], "K2")
        ax.arrow(0, 0, self.G_1[0], self.G_1[1], width=0.015)
        ax.text(self.G_1[0], self.G_1[1], 'G1')
        ax.arrow(0, 0, self.G_2[0], self.G_2[1], width=0.015)
        ax.text(self.G_2[0], self.G_2[1], 'G2')
        ax.set_xlabel(r"$k_{x}$ ($\acute{A}$)")
        ax.set_ylabel(r"$k_{y}$ ($\acute{A}$)")
        ax.set_title(r"BZ of %.2f$\degree$ %s" % (self.twist_angle, self.mat_type))
        if save_or_not:
            save_dir = PubMeth.get_right_save_path('structures')
            if not os.path.exists(save_dir):
                os.mkdir(save_dir)
            plt.savefig(save_dir + 'BZ_%.2f_%s' % (self.twist_angle, self.mat_type) + fig_format, dpi=300)
        plt.close()

    def atom_positions_origin(self):
        atoms_tuple = []
        bound_list_f = self.arrange_bound_p()
        for ele_index in self.indices_of_lattice:
            A1 = ele_index[0] * self.a1 + ele_index[1] * self.a2
            B1 = ele_index[0] * self.a1 + ele_index[1] * self.a2 + self.delta
            A2 = ele_index[0] * self.r_a1 + ele_index[1] * self.r_a2
            B2 = ele_index[0] * self.r_a1 + \
                 ele_index[1] * self.r_a2 + self.r_delta
            if PubMeth.isInterArea(
                    A1, bound_list_f) and not PubMeth.at_corners(
                A1, bound_list_f):
                atoms_tuple.append((A1[0], A1[1], 1))
            if PubMeth.isInterArea(
                    B1, bound_list_f) and not PubMeth.at_corners(
                B1, bound_list_f):
                atoms_tuple.append((B1[0], B1[1], 1))
            if PubMeth.isInterArea(
                    A2, bound_list_f) and not PubMeth.at_corners(
                A2, bound_list_f):
                atoms_tuple.append((A2[0], A2[1], 2))
            if PubMeth.isInterArea(
                    B2, bound_list_f) and not PubMeth.at_corners(
                B2, bound_list_f):
                atoms_tuple.append((B2[0], B2[1], 2))
        atoms_tuple.append((0, 0, 1))
        atoms_tuple.append((0, 0, 2))
        return atoms_tuple

    def atom_relations_origin(self):
        out_dic = {}
        for bra_p in self.positions_of_atoms:
            out_dic[bra_p] = {}
            for ket_p in self.positions_of_atoms:
                dist_arr = array([ket_p[0] - bra_p[0], ket_p[1] - bra_p[1]])
                out_dic[bra_p][ket_p] = PubMeth.get_smallest_distance(
                    dist_arr, self.sup_vec_list)
        return out_dic

    def intra_term(self, k_arr, distance_arr):
        return self.t_intra * exp(- (np.linalg.norm(distance_arr) - self.a0_const / sqrt(
            3)) / self.delta_0_par) * exp(-1j * np.dot(k_arr, distance_arr))

    def inter_term(self, k_arr, distance_arr):
        d_norm = sqrt(norm(distance_arr) ** 2 + self.d0 ** 2)
        value_cos = self.d0 / sqrt(norm(distance_arr) ** 2 + self.d0 ** 2)
        return (self.t_intra * exp(- (d_norm - self.a0_const / sqrt(3)) / self.delta_0_par) * (1 - value_cos ** 2)
                + self.t_inter * exp(- (d_norm - self.d0) / self.delta_0_par) * value_cos ** 2) * exp(
            -1j * np.dot(k_arr, distance_arr))

    def moire_b_zone(self):
        v_2 = self.G_2
        v_1 = self.G_1 + self.G_2
        kp_list_f = []
        for ele_m in arange(0, 1, 1 / self.kp_num):
            for ele_n in arange(0, 1, 1 / self.kp_num):
                k_p = ele_m * v_1 + ele_n * v_2
                kp_list_f.append(k_p)
        return kp_list_f

    def divide_kp_list(self):
        all_kp_list_f = self.moire_b_zone()
        kp_part_list_f = PubMeth.divide_list(all_kp_list_f)
        return kp_part_list_f

    def velocity_me(
            self,
            half_b_num,
            kp_arr_f,
            delta_k):
        cent_h = self.hamiltonian_construction(
            kp_arr_f)
        partial_hx = (self.hamiltonian_construction(
            kp_arr_f + array([delta_k, 0])) - cent_h) / delta_k
        partial_hy = (self.hamiltonian_construction(
            kp_arr_f + array([0, delta_k])) - cent_h) / delta_k
        eig_v, eig_a = eig(cent_h)
        vv_dic = {}
        for i_e in range(len(eig_v)):
            vv_dic[eig_v[i_e]] = eig_a.T[i_e]
        eig_v.sort()
        mid_i = int(len(eig_v) / 2)
        states_list = []
        for i_e in arange(-half_b_num, half_b_num):
            states_list.append(vv_dic[eig_v[mid_i + i_e]])
        all_trans_list = []
        half_of_states = int(len(states_list) / 2)
        for bra_i in range(0, half_of_states):
            bra_state = states_list[bra_i]
            for ket_i in range(half_of_states, len(states_list)):
                ket_state = states_list[ket_i]
                term1 = dot(dot(conj(ket_state), partial_hx), bra_state)
                term2 = dot(dot(conj(ket_state), partial_hy), bra_state)
                # all_trans_list.append(abs(dot(dot(conj(ket_state), partial_hx + partial_hy), bra_state)))
                # print(dot(dot(conj(ket_state), partial_hx + partial_hy), bra_state))
                all_trans_list.append(abs(term1 ** 2 + term2 ** 2))
        return all_trans_list

    def path_depiction(
            self,
            i,
            point1,
            point2,
            out_list,
            multi_process='off'):
        k_along = []
        if point2[0] != point1[0]:
            k_slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
            number_of_points = int(
                self.density_per_path * sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2))
            for xx in linspace(point1[0], point2[0], number_of_points):
                k_along.append(
                    array([xx, k_slope * (xx - point2[0]) + point2[1]]))
        elif point2[0] == point1[0]:
            number_of_points = int(
                self.density_per_path * sqrt((point2[1] - point1[1]) ** 2))
            for yy in linspace(point1[1], point2[1], number_of_points):
                k_along.append(array([point2[0], yy]))
        if multi_process == 'on':
            value_list = []
            for index, kp in enumerate(k_along):
                eig_v_f, eig_a_f = eig(
                    self.hamiltonian_construction(
                        kp))
                eig_v_f.sort()
                value_list.append(eig_v_f)
                print("Complete: ", index)
            value_list.append(i)
            out_list.append(value_list)
            print("Complete: ", point1, " to ", point2)

    def multi_proc_path(
            self,
            kp_path_list,
            save_or_not=True, y_range=[-1000, 1000], line_type='k-', x_labs=[], show_or_not=False, lw=1, hold_on=False, figsize=(7,5), shift_energy=True, test_mode=True, selected_bds_index_list=[], fig_format='.svg'):
        out_eig_list_f = multiprocessing.Manager().list()
        path_num = len(kp_path_list) - 1
        p_f = Pool(path_num)
        for i in range(path_num):
            p_f.apply_async(self.path_depiction,
                            args=(i,
                                  kp_path_list[i],
                                  kp_path_list[i + 1],
                                  out_eig_list_f,
                                  'on'))
        x_label_pos = PubMeth.situate_x_labels(kp_path_list, self.density_per_path)
        print('Waiting for all subprocesses done...')
        p_f.close()
        p_f.join()
        print('All subprocesses done.')
        total_energy_list = []
        for path_i in range(path_num):
            for ele_path in out_eig_list_f:
                if ele_path[-1] == path_i:
                    total_energy_list.extend(ele_path[0:-1])

        if isinstance(shift_energy, bool):
            half_energy = PubMeth.find_half_filling_energy(total_energy_list)

            if shift_energy:
                shifted_energy_list = array(total_energy_list) - half_energy

                figure_title = r"Band structure for $\theta={:.3f} \degree$-{}".format(self.twist_angle, self.mat_type)
                save_title = 'tb_band_{:.3f}_{}'.format(self.twist_angle, self.mat_type)
                PubMeth.plot_energies(real(shifted_energy_list), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='tb_energies_{:.4f}_{}'.format(self.twist_angle, self.mat_type), fig_format=fig_format)
            else:
                shifted_energy_list = array(total_energy_list)

                figure_title = r"Band structure for $\theta={:.3f} \degree$-{}".format(self.twist_angle, self.mat_type)
                save_title = 'tb_band_{:.3f}_{}'.format(self.twist_angle, self.mat_type)
                PubMeth.plot_energies(real(shifted_energy_list), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='tb_energies_{:.4f}_{}'.format(self.twist_angle, self.mat_type), fig_format=fig_format)
            return shifted_energy_list  # total_energy_list is un-shifted energy list
        else:
            shift_energy = array(total_energy_list) - shift_energy
            figure_title = r"Band structure for $\theta={:.3f} \degree$-{}".format(self.twist_angle, self.mat_type)
            save_title = 'tb_band_{:.3f}_{}'.format(self.twist_angle, self.mat_type)
            PubMeth.plot_energies(real(shift_energy), y_range=y_range, line_type=line_type, figuretitle=figure_title, x_label_pos=x_label_pos, x_labs=x_labs, save_or_not=save_or_not, show=show_or_not, save_title=save_title, lw=lw, hold_on=hold_on, fig_size=figsize, test_mode=test_mode, selected_bds_indices=selected_bds_index_list, html_name='tb_energies_{:.4f}_{}'.format(self.twist_angle, self.mat_type), fig_format=fig_format)
            return total_energy_list

    def plot_along_path(
            self,
            path=0,
            labels=0,
            yrange=[-2000, 2000],
            line_s='k-',
            lw=1,
            save_or_not=True,
            show=False,
            hold_or_not=False,
            figsize=(7, 5),
            shift_energy=True,
            test_or_not=True,
            selected_bds_list=[],
            fig_format='.svg'):
        if isinstance(path, int):
            # label_positions = ContiTbgInst.label_pos(
            #     self, ContiTbgInst.default_paths[path])
            # print("The density: ", label_positions)
            self.multi_proc_path(self.default_paths[path], x_labs=self.default_path_labels[path], y_range=yrange, line_type=line_s, lw=lw, save_or_not=save_or_not, show_or_not=show, hold_on=hold_or_not, shift_energy=shift_energy, test_mode=test_or_not, selected_bds_index_list=selected_bds_list, fig_format=fig_format, figsize=figsize)
        else:
            # label_positions = ContiTbgInst.label_pos(self, path)
            # print("The density: ", label_positions)
            self.multi_proc_path(
                path, save_or_not=save_or_not, x_labs=labels, y_range=yrange, line_type=line_s, lw=lw, show_or_not=show, hold_on=hold_or_not, figsize=figsize, shift_energy=shift_energy, test_mode=test_or_not, selected_bds_index_list=selected_bds_list, fig_format=fig_format)

    def label_pos(self, path_list):
        pos_list = [0]
        for ii in range(len(path_list) - 1):
            number_of_points = int(self.density_per_path *
                                   sqrt((path_list[ii +
                                                   1][1] -
                                         path_list[ii][1]) ** 2 +
                                        (path_list[ii +
                                                   1][0] -
                                         path_list[ii][0]) ** 2))
            next_pos = pos_list[-1] + number_of_points
            pos_list.append(next_pos)

        return pos_list

    def ab_cal(self, kp_arr_f, num_half_f, e_photon_list):

        cent_h = self.hamiltonian_construction(
            kp_arr_f)
        partial_hx = (self.hamiltonian_construction(kp_arr_f + array([self.interval_k, 0])) - cent_h) / self.interval_k
        partial_hy = (self.hamiltonian_construction(kp_arr_f + array([0, self.interval_k])) - cent_h) / self.interval_k

        eig_v, eig_a = eig(cent_h)
        vv_dic = {}
        for i_f in range(len(eig_v)):
            vv_dic[eig_v[i_f]] = eig_a.T[i_f]

        # six energies
        eig_v.sort()
        mid_i = len(eig_v) // 2
        chosen_energy = []  # v3, v2, v1, c1, c2, c3
        states_list = []  # v3, v2, v1, c1, c2, c3
        for i_b in range(-num_half_f, num_half_f):
            chosen_energy.append(eig_v[mid_i + i_b])
            states_list.append(vv_dic[eig_v[mid_i + i_b]])

        v_energy_list = chosen_energy[:num_half_f]
        c_energy_list = chosen_energy[num_half_f:]

        v_states_list = states_list[:num_half_f]
        c_states_list = states_list[num_half_f:]

        e_diff_list = []

        trans_list = []
        for i1 in range(len(v_states_list)):
            for i2 in range(len(c_states_list)):
                term1 = dot(
                    dot(conj(c_states_list[i2]), partial_hx), v_states_list[i1])
                term2 = dot(
                    dot(conj(c_states_list[i2]), partial_hy), v_states_list[i1])
                e_diff_list.append(
                    c_energy_list[i2] - v_energy_list[i1])
                trans_list.append(abs(term1) ** 2 + abs(term2) ** 2)

        ab_along_e = []
        for ele_photon in e_photon_list:
            tmp_term = array(trans_list) * self.ab_delta / ((array(e_diff_list) - ele_photon) ** 2 + self.ab_delta ** 2)
            tmp_sum = tmp_term.sum() / ele_photon
            ab_along_e.append(tmp_sum)
        return ab_along_e

    def multi_proc_ab_cal(self, args_list):
        """
        :param args_list: [num_half_f, e_photon_list]
        :return: list of absorption
        """
        parts_list = self.divide_kp_list()
        ab_all_k_along_e = PubMeth.multi_proc_func(self.ab_cal, parts_list, args_list)

        out_ab = zeros(len(args_list[-1]))
        for ele_along in ab_all_k_along_e:
            out_ab = out_ab + array(ele_along) * self.ab_renorm_const
        return out_ab

    def multi_proc_ab_2d(self, args_list, figs_save=True):
        """
        :param args_list: [num_half_f, e_photon_list]
        :return: list of absorption
        """
        parts_list = self.divide_kp_list()
        ab_all_k_along_e = PubMeth.multi_proc_func(self.ab_cal, parts_list, args_list)
        ab_all_k_along_e = array(ab_all_k_along_e)
        out_ab = []
        for i in range(len(args_list[-1])):
            chosen_e = args_list[-1][i]
            chosen_mat = real(ab_all_k_along_e)[:, i].reshape((self.kp_num, self.kp_num))
            PubMeth.rect2diam(chosen_mat, "TB_e_%.2f" % chosen_e, r"$E=%.2f meV$" % chosen_e, save_2d_plots=figs_save)
            print("Complete: ", args_list[-1][i], "meV")
            out_ab.append(ab_all_k_along_e[:, i].sum() * self.ab_renorm_const)

        return out_ab

    def dyn_cond_cal(
            self,
            i_core,
            num_half_f,
            point_list,
            out_list,
            E_photon_list,
            multi_process='off'):
        i_count = 0
        if multi_process == 'on':
            print("The # ", i_core, "process is running")
            mat_trans = []
            mat_e_diff = []
            for k_index, kp_arr_f in enumerate(point_list):
                # t1 = time()
                cent_h = self.hamiltonian_construction(kp_arr_f)
                partial_hx = (self.hamiltonian_construction(kp_arr_f + array([self.interval_k, 0])) - cent_h) / self.interval_k
                eig_v, eig_a = eig(cent_h)
                vv_dic = {}
                for i in range(len(eig_v)):
                    vv_dic[eig_v[i]] = eig_a.T[i]

                # six energies
                eig_v.sort()
                mid_i = int(len(eig_v) / 2)
                chosen_energy = []  # v3, v2, v1, c1, c2, c3
                states_list = []  # v3, v2, v1, c1, c2, c3
                for i_b in range(-num_half_f, num_half_f):
                    chosen_energy.append(eig_v[mid_i + i_b])
                    states_list.append(vv_dic[eig_v[mid_i + i_b]])

                v_energy_list = chosen_energy[:num_half_f]
                c_energy_list = chosen_energy[num_half_f:]

                v_states_list = states_list[:num_half_f]
                c_states_list = states_list[num_half_f:]

                e_diff_list = []

                trans_list = []  # v3 -- c123, v2 -- c123, v1 -- c123
                for i1 in range(len(v_states_list)):
                    for i2 in range(len(c_states_list)):
                        term1 = dot(
                            dot(conj(c_states_list[i2]), partial_hx), v_states_list[i1])
                        e_diff_list.append(
                            c_energy_list[i2] - v_energy_list[i1])
                        trans_list.append(abs(term1) ** 2)

                mat_trans.append(trans_list)
                mat_e_diff.append(e_diff_list)
                i_count = i_count + 1
                if i_count % 100 == 0:
                    print("Core %s: " % i_core, "Complete: ", i_count)
                elif len(point_list) - i_count < 100 and i_count % 10 == 0:
                    print("Core %s: " % i_core, "Complete: ", i_count)

            out_dyn_cond = []
            for ele_photon_e in E_photon_list:
                tmp_term = array(mat_trans) / (array(mat_e_diff) *
                                               (array(mat_e_diff) - ele_photon_e + 1j * self.dyn_cond_eta))
                tmp_sum = tmp_term.sum()
                out_dyn_cond.append(tmp_sum)

            out_list.append(array(out_dyn_cond))

    def multi_proc_dyn_cond_cal(
            self,
            kp_part_list_f,
            num_half_f,
            E_photon_list,
            dict_save='off'):
        t1 = time.time()
        print("Dimension of matrix: ", len(self.relations_of_atoms))
        out_dyn_list_f = multiprocessing.Manager().list()
        p_f = Pool(self.cores_num)
        for i in range(self.cores_num):
            p_f.apply_async(
                self.dyn_cond_cal,
                args=(
                    i,
                    num_half_f,
                    kp_part_list_f[i],
                    out_dyn_list_f,
                    E_photon_list,
                    'on'))
        print('Waiting for all subprocesses done...')
        p_f.close()
        p_f.join()
        print('All subprocesses done.')
        print("Time consumed: ", time.time() - t1)
        out_result = zeros(len(E_photon_list))
        for ele_arr in out_dyn_list_f:
            out_result = out_result + ele_arr
        if dict_save == 'on':
            target_dir = PubMeth.get_right_save_path("tb_tbg_dyn_cond")
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
            save(target_dir + "m0_%s_r_%s_half_%s_nk_%s.npy" %
                 (self.m0, self.r, num_half_f, self.Nk), out_result)
        return -imag(array(out_result))

    def raman_i_cal(self, k_point_arr, num_half_f, e_photon, hint=False):
        t1 = time.perf_counter()
        cent_h = self.hamiltonian_construction(k_point_arr)
        partial_hx = (
                             self.hamiltonian_construction(
                                 (k_point_arr[0] + self.interval_k,
                                  k_point_arr[1])) - cent_h) / self.interval_k
        partial_hy = (
                             self.hamiltonian_construction(
                                 (k_point_arr[0],
                                  k_point_arr[1] + self.interval_k)) - cent_h) / self.interval_k

        eig_v, eig_a = eig(cent_h)

        mid_i = len(eig_v) // 2

        v_energy_list = eig_v[argsort(real(eig_v))[mid_i - num_half_f : mid_i]]
        v_states_list = eig_a.T[argsort(real(eig_v))[mid_i - num_half_f:mid_i]]

        c_energy_list = eig_v[argsort(real(eig_v))[mid_i : mid_i + num_half_f]]
        c_states_list = eig_a.T[argsort(real(eig_v))[mid_i:mid_i + num_half_f]]

        term_h_x = conj(c_states_list) @ partial_hx @ v_states_list.T
        term_h_y = conj(c_states_list) @ partial_hy @ v_states_list.T
        trans_list = (abs(term_h_x) ** 2 + abs(term_h_y) ** 2)
        e_diff_list = array([ele_c_e - v_energy_list for ele_c_e in c_energy_list])

        raman_term_list = array(trans_list) / (
                (e_photon - array(e_diff_list) - 1j * self.raman_gamma) * (
                    e_photon - self.e_phonon - array(e_diff_list) - 1j * self.raman_gamma))
        raman_i = raman_term_list.sum()
        if hint:
            print("Complete: ", k_point_arr)
        t2 = time.perf_counter()
        print("Modified function time: ", t2 - t1)
        return raman_i

    def multi_proc_raman_i_cal(self, args_list, figs_save=True, hint=False):
        """
        :param args_list: [num_half, e_photon]
        :return:
        """
        parts_list = self.divide_kp_list()
        raman_cal = functools.partial(self.raman_i_cal, hint=hint)
        all_list = PubMeth.multi_proc_func(
            raman_cal, parts_list, args_list)
        im_mat = array(all_list).reshape((self.kp_num, self.kp_num))
        if figs_save:
            PubMeth.rect2diam(real(im_mat), "TB_raman_{:.3f}_{}".format(self.twist_angle, self.mat_type), r"$\theta = %.2f \degree$" % self.twist_angle, save_2d_plots=figs_save)

        return abs(im_mat.sum()) ** 2 / self.unit_moire_comm ** 2

    def get_fermi_vel(self, proportion_K_to_M=1):
        e_at_k = eig(self.hamiltonian_construction(self.K_1))[0]
        e_at_k.sort()
        e_cv_k = e_at_k[int(len(e_at_k) / 2) - 2:int(len(e_at_k) / 2) + 2]

        delta_vec_K_to_M = (self.M - self.K_1) * proportion_K_to_M
        target_k_point = self.K_1 + delta_vec_K_to_M

        e_at_m = eig(self.hamiltonian_construction(target_k_point))[0]
        e_at_m.sort()
        e_cv_m = e_at_m[int(len(e_at_m) / 2) - 2:int(len(e_at_m) / 2) + 2]
        Delta_E = array(e_cv_m - e_cv_k)
        print("∆E: ", Delta_E)
        Delta_k = norm(self.K_1 - target_k_point) * ones(len(Delta_E))
        return abs(Delta_E / (Delta_k * h_bar_eV * m2A * eV2meV))  # m/s

    def energy_at_k(self, k_arr_in, band_index):
        eigen_values= np.linalg.eig(self.hamiltonian_construction(k_arr_in))[0]
        eigen_values.sort()
        energy_out = eigen_values[len(eigen_values) // 2 - band_index:len(eigen_values) // 2 + band_index]
        energy_out = array(energy_out) - self.ref_energy
        print('Complete: ', k_arr_in)
        return energy_out

    def multi_proc_energy_at_k(self, args_list):
        """
        :param args_list: [k_arr_list, band_index]
        :return: list
        """
        parts_list = PubMeth.divide_list(args_list[0])
        print("# of total k: ", len(args_list[0]))
        eigen_enegies = PubMeth.multi_proc_func(self.energy_at_k, parts_list, [args_list[-1]])
        return eigen_enegies

    def contour_of_band_around_point(self, center_vec, delta_vec, band_range_width, density=70):
        dots_arr_list = PubMeth.dots_around_one_point(center_vec, delta_vec, density=density)
        energies_list = self.multi_proc_energy_at_k([dots_arr_list, band_range_width])
        save_path = PubMeth.get_right_save_path('contour_band_plots')
        save_path_data = PubMeth.get_right_save_path('contour_band_data')
        
        for draw_i in range(0, 2 * band_range_width):
            trace1 = go.Contour(z=array(real(energies_list))[:, draw_i].reshape((density+1, density+1)), contours_coloring='lines', line_width=1, contours={"showlabels":True, "labelfont":{"size":12, "color":'green'}})
            layout = PubMeth.plotly_layout(figuretitle='Contour of Bands for Band {}. Angle = {:.2f}'.format(draw_i, self.twist_angle))
            fig = go.Figure(data=[trace1], layout=layout)
            fig.update_yaxes(
            scaleanchor = "x",
            scaleratio = 1,
        )
            filename = 'contour_{:.2f}_band_{}'.format(self.twist_angle, draw_i)
            fig.update_traces(ncontours=45, selector=dict(type='contour'))
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            if not os.path.exists(save_path_data):
                os.mkdir(save_path_data)
            np.save(save_path_data + filename + '.npy', array(real(energies_list))[:, draw_i].reshape((density+1, density+1)))
            fig.write_html(save_path + filename + '.html')

    def get_fermi_vel_from_K(self, k_arr_in, band_index, valley_index='K1'):
        eigen_values = np.linalg.eig(self.hamiltonian_construction(k_arr_in))[0]
        eigen_values.sort()
        fermi_vel_out = eigen_values[len(eigen_values) // 2 - band_index:len(eigen_values) // 2 + band_index]
        
        if valley_index == 'K1':
            # # Exclusion of K point, which is a singularity
            fermi_vel_out = abs((array(fermi_vel_out) - self.ref_energy) / (norm(k_arr_in - self.K_1))) / (h_bar_eV * eV2meV * m2A * 1e3)

            # # Inclusion of K point, which is a singularity
            # if norm(k_arr_in - self.K_1) != 0:
            #     fermi_vel_out = abs((array(fermi_vel_out) - self.ref_energy) / (norm(k_arr_in - self.K_1))) / (h_bar_eV * eV2meV * m2A * 1e6)
            # elif norm(k_arr_in - self.K_1) == 0:
            #     fermi_vel_out = np.zeros(len(fermi_vel_out))
        elif valley_index == 'K2':
            # # Exclusion of K point, which is a singularity
            fermi_vel_out = abs((array(fermi_vel_out) - self.ref_energy) / (norm(k_arr_in - self.K_2))) / (h_bar_eV * eV2meV * m2A * 1e3)

            # # Inclusion of K point, which is a singularity
            # if norm(k_arr_in - self.K_2) != 0:
            #     fermi_vel_out = abs((array(fermi_vel_out) - self.ref_energy) / (norm(k_arr_in - self.K_2))) / (h_bar_eV * eV2meV * m2A * 1e6)
            # elif norm(k_arr_in - self.K_2) == 0:
            #     fermi_vel_out = np.zeros(len(fermi_vel_out))
        return fermi_vel_out

    def multi_proc_get_fermi_vel_from_K(self, args_list):
        """
        :param args_list: [k_arr_list, band_index]
        :return: list
        """
        parts_list = PubMeth.divide_list(args_list[0])
        print("# of total k: ", len(args_list[0]))
        eigen_enegies = PubMeth.multi_proc_func(self.get_fermi_vel_from_K, parts_list, [args_list[-1]])
        return eigen_enegies

    def contour_of_fermi_vel_around_K(self, center_vec, delta_vec, band_range_width, density=70, filename='contour', contour_color='Hot', size_of_contour=0.001):
        dots_arr_list = PubMeth.dots_around_one_point(center_vec, delta_vec, density=density)
        energies_list = self.multi_proc_get_fermi_vel_from_K([dots_arr_list, band_range_width])
        save_path = PubMeth.get_right_save_path('contour_fermi_vel_plots')
        save_path_data = PubMeth.get_right_save_path('contour_fermi_vel_data')
        
        for draw_i in range(0, 2 * band_range_width):
            trace1 = go.Contour(z=array(real(energies_list))[:, draw_i].reshape((density+1, density+1)), contours_coloring='lines', colorscale=[[0, 'gold'], [0.5, 'mediumturquoise'], [1, 'lightsalmon']], line_width=1, contours={"showlabels":True, "labelfont":{"size":12, "color":'green'}, 'start': 0, 'end': 3000, 'size': 5})
            layout = PubMeth.plotly_layout(figuretitle='Contour of Fermi Velocity for Bnad {}. Angle = {:.2f}'.format(draw_i, self.twist_angle))
            fig = go.Figure(data=[trace1], layout=layout)
            fig.update_yaxes(
            scaleanchor = "x",
            scaleratio = 1,
        )
            filename = 'contour_{:.2f}_fermi_vel_{}'.format(self.twist_angle, draw_i)
            # fig.update_traces(ncontours=45, selector=dict(type='contour'))
            if not os.path.exists(save_path):
                os.mkdir(save_path)
            if not os.path.exists(save_path_data):
                os.mkdir(save_path_data)
            np.save(save_path_data + filename + '.npy', array(real(energies_list))[:, draw_i].reshape((density+1, density+1)))
            fig.write_html(save_path + filename + '.html')


class ContiNearComm(ContiTbgInst):

    def __init__(self, m0, r, couple_pars_list, displace_d=array([0, 0]), delta_angle=0, a0_constant=1.42 * sqrt(3), density_per_path=100, delta_angle_equal_magic=False, basis_loop_times=7) -> None:
        self.m0 = m0
        self.r = r

        self.chi_0 = couple_pars_list[0]
        self.chi_theta = self.chi_0 / 180 * pi
        self.w_0 = couple_pars_list[1]
        self.w_1 = couple_pars_list[2]
        self.w_2 = couple_pars_list[3]

        self.twist_angle_comm, self.twist_theta_comm = PubMeth.commensurate_angle(m0, r)
        self.n_unit_cell_within = PubMeth.unit_cell_per_supercell(m0, r)
        self.n_atoms = 4 * self.n_unit_cell_within
        self.norm_reci_vec = 4 * pi / (sqrt(3) * a0_constant)
        self.norm_K = 4 * pi / (3 * a0_constant)
        self.displace_d_arr = displace_d
        self.a0_constant = a0_constant
        self.norm_side = a0_constant / sqrt(3)

        self.v_F = 3.68423316 * a0_constant / (sqrt(3) * h_bar_eV * m2A)
        self.delta_theta_magic = sqrt(3) * self.w_1 / (h_bar_eV * self.v_F * eV2meV * m2A * sqrt(self.n_unit_cell_within) * self.norm_K)
        self.delta_angle_magic = self.delta_theta_magic / pi * 180

        if delta_angle_equal_magic:
            self.delta_angle = self.delta_angle_magic
            self.delta_theta = self.delta_theta_magic
        else:
            self.delta_angle = delta_angle
            self.delta_theta = delta_angle / 180 * pi
        
        self.a_1 = a0_constant * array([1, 0])
        self.a_2 = PubMeth.rotation(-60) @ self.a_1

        self.b_1 = self.norm_reci_vec * array([sqrt(3) / 2, 1 / 2])
        self.b_2 = PubMeth.rotation(-120) @ self.b_1
        self.Gamma_arr = array([0, 0])
        self.K_arr = self.norm_K * array([1, 0])
        self.K_prime_arr = PubMeth.rotation(-60) @ self.K_arr
        self.M_arr = (self.K_arr + self.K_prime_arr) / 2

        self.half_angle_cos = cos(self.twist_theta_comm / 2)
        self.half_angle_sin = sin(self.twist_theta_comm / 2)
        self.original_s = int((self.half_angle_cos * sqrt(self.n_unit_cell_within) + self.half_angle_sin * sqrt(self.n_unit_cell_within) * sqrt(3)))
        if self.original_s % 3 == 1:
            self.s = 1
        elif self.original_s % 3 == 2:
            self.s = -1
        else:
            self.s = 1
        
        self.Q_1 = self.s * sqrt(self.n_unit_cell_within) * self.K_arr
        self.Q_2 = PubMeth.rotation(120) @ self.Q_1
        self.Q_3 = PubMeth.rotation(240) @ self.Q_1
        self.Q_list = [self.Q_1, self.Q_2, self.Q_3]
        self.norm_Q = norm(self.Q_1)

        self.q_1 = PubMeth.operator_d_theta(self.delta_angle) @ self.Q_1
        self.q_2 = PubMeth.rotation(120) @ self.q_1
        self.q_3 = PubMeth.rotation(240) @ self.q_1
        self.q_list = [self.q_1, self.q_2, self.q_3]
        self.norm_q = norm(self.q_1)

        super().__init__(twist_angle_conti = self.delta_angle, v_F = self.v_F, a0_constant = self.a0_constant / sqrt(self.n_unit_cell_within), basis_loop_times=basis_loop_times)

        # self.K_M_arr = PubMeth.operator_d_theta(self.delta_angle) @ (self.s * sqrt(self.n_unit_cell_within) *  self.K_arr)
        # self.K_prime_M_arr = PubMeth.operator_d_theta(self.delta_angle) @ (self.s * sqrt(self.n_unit_cell_within) *  self.K_prime_arr)
        # self.M_M_arr = PubMeth.operator_d_theta(self.delta_angle) @ (self.s * sqrt(self.n_unit_cell_within) *  self.M_arr)
        
        self.norm_p0 = 3 * abs(self.w_0) / (h_bar_eV * self.v_F * eV2meV * m2A)
        self.p_0 = self.norm_p0 * array([1, 0])

        self.density_per_path = density_per_path / self.norm_K

    def T_Qj(self, j_index):  # # j_index = 1, 2, 3
        ksi_j = 2 * pi * (j_index - 1) / 3
        return self.w_0 * expm(1j * self.chi_theta * PubMeth.pauli_mat(3)) + self.w_1 * (PubMeth.pauli_mat(1) * cos(ksi_j) + PubMeth.pauli_mat(2) * sin(ksi_j))
    
    def T_0_comm(self):
        T_out = zeros((2, 2))
        for j_index in range(len(self.Q_list)):
            T_out = T_out + self.T_Qj(j_index + 1) * exp(1j * self.displace_d_arr @ (cos(self.twist_theta_comm / 2) * self.K_arr - self.Q_list[j_index]))
        return T_out
    
    def S_0_comm(self):
        return self.w_2 * PubMeth.pauli_mat(0) * exp(1j * self.displace_d_arr @ (cos(self.twist_theta_comm / 2) * self.K_arr))

    def intra_h_comm(self, p_arr):
        return h_bar_eV * self.v_F * m2A * eV2meV * np.block([
            [PubMeth.sigma_angle_dot_p(p_arr, self.twist_angle_comm / 2), zeros((2, 2))],
            [zeros((2, 2)), PubMeth.sigma_angle_dot_p(p_arr, -self.twist_angle_comm / 2)]
        ])

    def inter_h_comm(self):
        return np.block([
            [self.S_0_comm(), self.T_0_comm()],
            [conj(self.T_0_comm()).T, self.S_0_comm()]
        ])

    def h_b(self, k):
        k_mod = (k - self.k_b_arr) * self.norm_Kg_conti
        return h_bar_eV * self.v_F * m2A * eV2meV * PubMeth.sigma_angle_dot_p(k_mod, self.twist_angle_comm / 2) + self.w_2 * np.eye(2)

    def h_t(self, k):
        k_mod = (k - self.k_t_arr) * self.norm_Kg_conti
        return h_bar_eV * self.v_F * m2A * eV2meV * PubMeth.sigma_angle_dot_p(k_mod, -self.twist_angle_comm / 2) + self.w_2 * np.eye(2)

    def T_Qj(self, j_index):  # # j_index = 1, 2, 3
        ksi_j = 2 * pi * (j_index - 1) / 3
        return self.w_0 * expm(1j * self.chi_theta * PubMeth.pauli_mat(3)) + self.w_1 * (PubMeth.pauli_mat(1) * cos(ksi_j) + PubMeth.pauli_mat(2) * sin(ksi_j))

    def t_0(self):
        return conj(self.T_Qj(1)).T

    def t_p1(self):
        return conj(self.T_Qj(2)).T
    
    def t_n1(self):
        return conj(self.T_Qj(3)).T

    def hamiltonian_construction(self, p_arr):
        if self.delta_angle == 0:
            return self.intra_h_comm(p_arr) + self.inter_h_comm()
        elif self.delta_angle != 0:
            return super().hamiltonian_construction(p_arr)
    
    def plot_along_path(
            self,
            path,
            labels,
            yrange,
            line_s='k-',
            lw=1,
            save_or_not=True,
            show=False,
            hold_or_not=False,
            figsize=(7, 5),
            shift_energy=True,
            test_or_not=True):
        if isinstance(path, int):
            self.multi_proc_path(self.default_paths[path], x_labs=self.default_path_labels[path], y_range=yrange, line_type=line_s, lw=lw, save_or_not=save_or_not, show_or_not=show, hold_on=hold_or_not, comm_angle_in_title=self.twist_angle_comm, delta_angle_in_title=self.delta_angle, shift_energy=shift_energy, test_mode=test_or_not)
        else:
            self.multi_proc_path(
                path, save_or_not=save_or_not, x_labs=labels, y_range=yrange, line_type=line_s, lw=lw, show_or_not=show, hold_on=hold_or_not, figsize=figsize, comm_angle_in_title=self.twist_angle_comm, delta_angle_in_title=self.delta_angle, shift_energy=shift_energy, test_mode=test_or_not)


def main():
    pass


if __name__ == '__main__':
    main()
