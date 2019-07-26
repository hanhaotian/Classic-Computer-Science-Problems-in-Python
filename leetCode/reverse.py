# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
#  示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。


def reverse(x: int) -> int:

    res = 0
    flag = x > 0
    tag = abs(x)
    max_int = (pow(2, 31) - 1)
    min_int = -(pow(2, 31))
    print(max_int)
    print(min_int)
    while tag != 0:
        temp: int = tag % 10
        tag //= 10
        if flag:
            if res > (max_int // 10) or (res == max_int // 10 and temp > 7):
                return 0
        else:
            if res < (min_int // 10) or (res == min_int // 10 and -temp > -8):
                return 0
        if flag:
            res = res * 10 + temp
        else:
            res = res * 10 - temp
    return res


print(reverse(-1563847412))
