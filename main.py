from game_2048 import Game_2048 as Game


def play_game():
    n = int(input('请输入棋盘大小:'))
    game = Game(n)

    while True:
        # 打印界面
        game.print_background()

        # 请用户输入移动方向
        s = input('请输入方向(w,s,a,d)，输入其它字符结束:')
        if s not in('w', 's', 'a', 'd'):
            break

        # 移动数据
        game.move(s)

        # 判定游戏是否结束
        if game.is_game_over():
            game.print_background()
            break

    # 计算游戏分数
    score = game.cal_score()
    print('游戏结束，得分为:%d' % score)


if __name__ == '__main__':
    play_game()
