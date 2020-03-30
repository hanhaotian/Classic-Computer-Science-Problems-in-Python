def lcs(f, s, flag):

    res = set()
    sum = 0
    f_size = len(f)
    s_size = len(s)
    if f_size == 0 or s_size ==0 :
        return 1
    for i in range(f_size):
        for j in range(s_size):
            if f[i] == s[j]:
                sum += lcs(f[i+1:], s[j+1:], True)
            else:
                if flag:
                    return 1 if sum < 2 else sum
                else:
                    res.add(sum)
                    sum = 0

    return max(res)

a = [1, 0, 0, 1, 0, 1, 0, 1]
b = [0, 1, 0, 1, 1, 0, 1, 1, 0]

if len(a) > len(b):
    print('lcs is :', lcs(b, a, False))
else:
    print('lcs is :', lcs(a, b, False))



