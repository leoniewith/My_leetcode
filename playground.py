import time
def add_one(given_arr):

    result = [0] * len(given_arr)
    carry = 1

    for i in range(len(given_arr)-1, -1, -1):
        sum = given_arr[i] + carry
        if sum == 10:
            carry = 1

        else:
            carry = 0

        result[i] = sum % 10

    if carry == 1:
        result.insert(0, 1)

    return result

def add_one_2(given_arr):
    pre_sum = eval(''.join(map(str, given_arr)))

    cur_sum = pre_sum + 1

    result = list(map(int, str(cur_sum)))

    return result





