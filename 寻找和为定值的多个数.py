'''
寻找和为定值的多个数
题目描述
输入两个整数n和sum，从数列1，2，3.......n 中随意取几个数，使其和等于sum，要求将其中所有的可能组合列出来。

分析与解法
解法一
注意到取n，和不取n个区别即可，考虑是否取第n个数的策略，可以转化为一个只和前n-1个数相关的问题。

如果取第n个数，那么问题就转化为“取前n-1个数使得它们的和为sum-n”，对应的代码语句就是sumOfkNumber(sum - n, n - 1)；
如果不取第n个数，那么问题就转化为“取前n-1个数使得他们的和为sum”，对应的代码语句为sumOfkNumber(sum, n - 1)。
'''

cor_list = []


def SumOfNumber(target_sum, n):
    if target_sum == 0:
        print(cor_list)
    if n <= 0 or target_sum <0:
        return


    cor_list.append(n)
    SumOfNumber(target_sum - n, n - 1)
    cor_list.pop()
    SumOfNumber(target_sum, n - 1)




SumOfNumber(7, 6)
