from random import randint


def play():
    random_int=randint(1,100)

    while True:
        user_guess=int(input("please input one number between 1 to 100:"))

        if user_guess==random_int:
            print("you win")
            break
        if user_guess<random_int:
            print("less")
            continue
        if user_guess>random_int:
            print("more")
            continue


if __name__=='__main__':
    play()