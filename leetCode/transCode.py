def trans_code(code):
    i = 0
    while i < len(code):
        if code[i] == ']':
            j = i  # j用来向前寻找与]相匹配的[
            k = 0  # k用来记录'|'所在位置
            while code[j] != '[':
                if code[j] == '|':
                    k = j
                j -= 1
            temp_code = code[k+1:i]
            temp_num = code[j+1:k]
            temp_res = temp_code * int(temp_num)
            code = code.replace(code[j:i+1], temp_res)
            i = j
        i += 1
    return code


test = 'HG[3|B[2|CA]]F'

# test = 'BHCJSBCSCW[100|DASKDNKJWDNWCNQWCNOQCNQWOICNWQOINCWQOICNQWOIXWOISWIODAOWPQWDMQKOQZCDWF]WQJDWQUINCQQW[99|SDWQJCIQIUWCNQUCNWQIDNWQUIFNSALQP]DQOJOIXZALPPQQAAX'

print(trans_code(test))
