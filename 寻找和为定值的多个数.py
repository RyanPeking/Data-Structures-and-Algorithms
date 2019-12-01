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
