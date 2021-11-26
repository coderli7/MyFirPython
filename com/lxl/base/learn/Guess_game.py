from random import randint


def play():
    random_int=randint(1,100)

    while True:
        user_guess=int(input("输入数字 between 1 to 100:"))

        if user_guess==random_int:
            print("你赢了")
            break
        if user_guess<random_int:
            print("太小了")
            continue
        if user_guess>random_int:
            print("太大了")
            continue


if __name__=='__main__':
    play()