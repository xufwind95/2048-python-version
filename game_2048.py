import random
import copy


class Game_2048:
    def __init__(self, n_row_col):
        """初始化一个二维数组，用来记录每个格子的数"""
        d = []
        for row in range(n_row_col):
            d_row = []
            for col in range(n_row_col):
                d_row.append(0)
            d.append(d_row)
        self.data = d
        self.gen_random_data()
        self.gen_random_data()
        self.data_before = copy.deepcopy(self.data)

    def get_data(self):
        """获取游戏中的数据，用于打印"""
        return self.data

    def gen_random_data(self):
        """在随机位置生成一个数"""
        r_num = random.choice((2, 2, 2, 2, 4))
        # r_num = 2
        r_pos = random.choice(range(self.cal_rand_pos_range())) + 1
        length = len(self.data)
        n = 0
        for x in range(length):
            for y in range(length):
                if self.data[x][y] == 0:
                    n += 1
                    if n == r_pos:
                        self.data[x][y] = r_num
                        return

    def cal_rand_pos_range(self):
        """计算随机位置范围"""
        n_pos = 0
        for l in self.data:
            for e in l:
                if e == 0:
                    n_pos += 1
        return n_pos

    def move_down(self, length, x):
        """将上下大于0的数据填充到列表中"""
        l_real_num = []
        for y in range(length - 1, -1, -1):
            if self.data[y][x] > 0:
                l_real_num.append(self.data[y][x])
                self.data[y][x] = 0

        if l_real_num:
            self.__cal_move(l_real_num, 0)
        else:
            l_real_num = [0]

        # 将返回的值放回格子(按顺序放，且挨着放)
        y = length - 1
        res_len = len(l_real_num)
        pos = 0
        while True:
            if pos < res_len:
                self.data[y][x] = l_real_num[pos]
                y -= 1
                pos += 1
            else:
                break

    def move_up(self, length, x):
        """将上下大于0的数据填充到列表中"""
        l_real_num = []
        for y in range(length):
            if self.data[y][x] > 0:
                l_real_num.append(self.data[y][x])
                self.data[y][x] = 0

        if l_real_num:
            self.__cal_move(l_real_num, 0)
        else:
            l_real_num = [0]

        # 将返回的值放回格子(按顺序放，且挨着放)
        y = 0
        res_len = len(l_real_num)
        pos = 0
        while True:
            if pos < res_len:
                self.data[y][x] = l_real_num[pos]
                y += 1
                pos += 1
            else:
                break

    def move_left(self, length, x):
        """将左右大于0的数据填充到列表中"""
        l_real_num = []
        for y in range(length):
            if self.data[x][y] > 0:
                l_real_num.append(self.data[x][y])
                self.data[x][y] = 0

        if l_real_num:
            self.__cal_move(l_real_num, 0)
        else:
            l_real_num = [0]

        # 将返回的值放回格子(按顺序放，且挨着放)
        y = 0
        res_len = len(l_real_num)
        pos = 0
        while True:
            if pos < res_len:
                self.data[x][y] = l_real_num[pos]
                y += 1
                pos += 1
            else:
                break

    def move_right(self, length, x):
        """将左右大于0的数据填充到列表中"""
        l_real_num = []
        for y in range(length - 1, -1, -1):
            if self.data[x][y] > 0:
                l_real_num.append(self.data[x][y])
                self.data[x][y] = 0

        if l_real_num:
            self.__cal_move(l_real_num, 0)
        else:
            l_real_num = [0]

        # 将返回的值放回格子(按顺序放，且挨着放)
        y = length - 1
        res_len = len(l_real_num)
        pos = 0
        while True:
            if pos < res_len:
                self.data[x][y] = l_real_num[pos]
                y -= 1
                pos += 1
            else:
                break

    def copy_to_before(self):
        length = len(self.data)

        for x in range(length):
            for y in range(length):
                self.data_before[x][y] = self.data[x][y]

    def move(self, fangxiang):
        """定义移动的放法
        2:下移　8:上移　4:左移　６: 右移
        """
        # 移动前先将两组数据同步
        self.copy_to_before()

        length = len(self.data)

        for x in range(length):
            if fangxiang == 's':
                self.move_down(length, x)
            elif fangxiang == 'w':
                self.move_up(length, x)
            elif fangxiang == 'a':
                self.move_left(length, x)
            elif fangxiang == 'd':
                self.move_right(length, x)

        # 比较两个移动前后的是否有变化，没有变化的不生成新数
        if self.data != self.data_before:
            self.gen_random_data()

    def cal_score(self):
        """统计游戏分数"""
        max_score = 0
        for l in self.data:
            for e in l:
                if max_score < e:
                    max_score = e
        return max_score

    def print_background(self):
        """打印游戏界面"""
        width = 4
        line_len = len(self.data)
        line = ''
        for i in range(line_len):
            line += '+' + '-' * width
        line += '+'
        print(line)  # 打印行首
        for l in self.data:
            row = ''
            for e in l:
                if e == 0:
                    row += "|" + ' ' * width
                else:
                    row += '|' + str(e).center(width)
            row += '|'
            print(row)  # 打印数据
            print(line)  # 打印每一行的底边

    def __cal_move(self, cal_arr, begin_idx):
        """计算位移方式"""
        cal_flag = False
        for i in range(begin_idx, len(cal_arr) - 1):
            if cal_arr[i] == cal_arr[i + 1] and cal_arr[i] > 0:
                cal_arr[i] += cal_arr[i + 1]
                cal_arr[i + 1:] = cal_arr[i + 2:]
                cal_flag = True
                next_index = i + 1
                break
        if cal_flag:
            self.__cal_move(cal_arr, next_index)
        return

    def is_game_over(self):
        """判定游戏是否结束"""
        length = len(self.data)

        for l in self.data:
            for i in range(length - 1):
                if l[i] == 0 or l[i] == l[i + 1] or l[i + 1] == 0:
                    return False

        for x in range(length):
            for y in range(length - 1):
                if self.data[y][x] == self.data[y + 1][x]:
                    return False

        return True
