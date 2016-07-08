# 画面に自分の「学科名」「学年」「学籍番号」を出力してください
def print_self_information():
    pass


# 自分の年齢が、80歳になるまであと何年か計算して出力してください
def print_how_many_years_to_80():
    pass


# 与えられた整数パラメータが「偶数」か「奇数」かを出力してください
def print_odd_or_even(target):
    if target % 2 == 0:
        print('偶数')
    else:
        print('奇数')


# randomモジュールを使用して0-50の整数を生成し、25が出るまで「ほげ」と出力してください
def print_hoge():
    from random import randint
    # randint(0,50) で、0-50 の範囲内から整数乱数を生成してくれる
    while randint(0, 50) != 25:
        print("ほげ")


# 100から1000までの偶数のみ表示してください
def print_even_from_100_to_1000():
    for num in range(100, 1000):
        if num % 2 == 0:
            print(num)


if __name__ == '__main__':
    print_self_information()
    print_how_many_years_to_80()
    print_odd_or_even(10)
    print_odd_or_even(13)
    print_hoge()
    print_even_from_100_to_1000()
