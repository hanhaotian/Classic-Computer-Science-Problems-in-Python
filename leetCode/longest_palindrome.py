# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"


def check_point(s: str, left: int, right: int) -> int:
    ll = left
    rr = right
    while ll >= 0 and rr < len(s) and s[ll].__eq__(s[rr]):
        ll -= 1
        rr += 1

    return rr - ll - 1


def longest_palindrome(s: str) -> str:
    start: int = 0
    end: int = 0
    for i in range(0, len(s)):
        len1 = check_point(s, i, i)
        len2 = check_point(s, i, i+1)
        lens = max(len1, len2)
        if lens > end - start:
            start = i - (lens - 1) // 2
            end = i + lens // 2

    return s[start: end+1]


print(longest_palindrome('abacdfgdcaba'))
