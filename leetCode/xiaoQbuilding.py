
n = 10
building = [73289, 45963, 22522, 44454, 58143, 31977, 59209,  85753, 45063, 9507]
# building = [5, 3, 8, 3, 2, 5]
right = []
left = []
R = [0 for i in range(n)]
L = [0 for j in range(n)]
for i in range(n):
    R[i] = len(right)
    if i == 0:
        right.append(building[0])
    elif right[-1:].pop() > building[i]:
        right.append(building[i])
    else:
        while len(right) != 0 and right[-1:].pop() <= building[i]:
            right.pop()
        right.append(building[i])
for i in range(n - 1,-1,-1):
    L[i] = len(left)
    if i == n -1:
        left.append(building[n -1])
    elif left[-1:].pop() > building[i]:
        left.append(building[i])
    else:
        while len(left) != 0 and left[-1:].pop() <= building[i]:
            left.pop()
        left.append(building[i])


for i in range(n):
    print(L[i] + R[i] + 1)
# 5 7 7 7 7 5 5 4 3 3
# 6
# 538325

# 3 3 5 4 4 4

