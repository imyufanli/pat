"""
Author: Yufan Li (yufan.l@hotmail.com)
PAT (Basic Level) Practice
1002 写出这个数
score: 15 out of 15
"""


def split_num(n):
    sum_n = 0
    while n % 10 != n:
        sum_n += n % 10
        n //= 10
    return sum_n + n % 10


def to_pinyin(n):
    words = []
    while n != 0:
        words.append(num_cn[n % 10])
        n //= 10
    return words


num_cn = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]


words = to_pinyin(split_num(int(input())))
words.reverse()
print(" ".join(words))
