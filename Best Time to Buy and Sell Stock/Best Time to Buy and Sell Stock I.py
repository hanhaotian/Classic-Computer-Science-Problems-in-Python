'''
题目一：用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。 如果只允许进行一次交易，也就是说只允许买一支股票并卖掉，求最大的收益。
分析：动态规划法。从前向后遍历数组，记录当前出现过的最低价格，作为买入价格，并计算以当天价格出售的收益，作为可能的最大收益，整个遍历过程中，出现过的最大收益就是所求。
代码：O(n)时间，O(1)空间。
'''


def max_income1(prices):
    if len(prices) == 2:
        return prices[1] - prices[0]
    minPay = prices[0]
    maxGet = 0
    for i in range(len(prices[1:]) + 1):
        minPay = min(minPay, prices[i])
        maxGet = max(maxGet, prices[i] - minPay)
    return maxGet


'''
题目二：用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。交易次数不限，但一次只能交易一支股票，也就是说手上最多只能持有一支股票，求最大收益。
分析：贪心法。从前向后遍历数组，只要当天的价格高于前一天的价格，就算入收益。
代码：时间O(n)，空间O(1)。
'''


def max_income2(prices):
    if len(prices) == 2:
        return prices[1] - prices[0]
    diff = 0
    sum = 0
    for i in range(len(prices) - 1):
        diff = prices[i + 1] - prices[i]
        if diff > 0:
            sum += diff
    return sum


'''
题目三：用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。最多交易两次，手上最多只能持有一支股票，求最大收益。
分析：动态规划法。以第i天为分界线，计算第i天之前进行一次交易的最大收益preProfit[i]，和第i天之后进行一次交易的最大收益postProfit[i]，最后遍历一遍，
max{preProfit[i] + postProfit[i]} (0≤i≤n-1)就是最大收益。第i天之前和第i天之后进行一次的最大收益求法同题目一。
代码：时间O(n)，空间O(n)。
'''


def max_income3(prices):
    if len(prices) == 2:
        return prices[1] - prices[0]
    n = len(prices)
    first = [0] * n
    second = [0] * n

    minPay = prices[0]
    for i in range(1, n):
        minPay = min(minPay, prices[i])
        first[i] = max(first[i - 1], prices[i] - minPay)

    maxGet = prices[n - 1]
    for i in range(n - 2, 0, -1):
        maxGet = max(maxGet, prices[i])
        second[i] = max(second[i + 1], maxGet - prices[i])

    maxIncome = 0
    for k in range(0, n):
        maxIncome = max(maxIncome, first[k] + second[k])
    return maxIncome


'''
题目四：用一个数组表示股票每天的价格，数组的第i个数表示股票在第i天的价格。最多交易k次，手上最多只能持有一支股票，求最大收益。
分析：特殊动态规划。用local[i][j]表示到达第i天时，最多进行j次交易的局部最优解，local[i][j]意味着在第i天一定有交易（卖出）发生；用global[i][j]表示到达第i天时，
最多进行j次的全局最优解，global[i][j]就是我们所求的前i天最多进行k次交易的最大收益。它们二者的关系如下
（其中diff = prices[i] – prices[i – 1]）：local[i][j] = max(global[i – 1][j – 1] , local[i – 1][j] + diff)；global[i][j] = max(global[i – 1][j], local[i][j])
代码：时间O(nk)，空间O(nk)。
'''


def max_income4(prices, k):
    n = len(prices)
    if n == 2:
        return prices[1] - prices[0]
    if k >= n:
        return max_income2(prices)

    local = [[0] * n for i in range(n)]
    glbal = [[0] * n for i in range(n)]

    for i in range(1, n):
        diff = prices[i] - prices[i - 1]

        for j in range(1, k + 1):
            local[i][j] = max(glbal[i - 1][j - 1], local[i - 1][j] + diff)
            glbal[i][j] = max(glbal[i - 1][j], local[i][j])
    return glbal[n - 1][k]


'''
动态规划所用的二维辅助数组可以降为一维的，即只用大小为k的一维数组记录到达第i天时的局部最优解和全局最优解。
需要注意的是，由于第i天时交易k次的最优解依赖于第i-1天时交易k-1次的最优解，所以数组更新应当从后往前（即从k到1）更新。
'''


def max_income5(prices, k):
    n = len(prices)
    if n == 2:
        return prices[1] - prices[0]
    if k >= n:
        return max_income2(prices)

    local = [0] * n
    glbal = [0] * n

    for i in range(1, n):
        diff = prices[i] - prices[i - 1]

        for j in range(k, 0, -1):
            local[j] = max(glbal[j - 1], local[j] + diff)
            glbal[j] = max(glbal[j], local[j])

    return glbal[k]


if __name__ == '__main__':
    prices = [2, 8, 4, 5, 6, 7, 22, 31]
    # print(max_income1(prices))
    # print(max_income2(prices))
    # print([i for i in range(10, 0, -1)])
    print(max_income3(prices))
    print(max_income4(prices, 2))
    print(max_income5(prices, 2))
