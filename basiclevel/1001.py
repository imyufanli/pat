"""
Author: Yufan Li (yufan.l@hotmail.com)
PAT (Basic Level) Practice
1001 害死人不偿命的(3n+1)猜想
"""

count = 0


def main(n):
    global count
    if n == 1:
        print(count)
    # 偶数
    elif n % 2:
        count += 1
        n = (3*n + 1)/2
        main(n)
    # 奇数
    else:
        count += 1
        n = n/2
        main(n)


main(int(input()))
