def is_tidy(num):
    n = len(num)
    if n == 1:
        return True
    for idx in range(n - 1):
        if num[idx] > num[idx + 1]:
            return False
    return True


# O(log(n))
# find the first break in the sequence, then backtrack to find the nearest
# digit that can be changed without breaking the ascending sequence
# fill the rest with 9's
def solve(num):
    i = 0
    n = len(num)
    while i < n - 1:
        if num[i] > num[i + 1]:
            break
        i += 1
    if i == n - 1:
        return num
    while i > 0:
        if num[i - 1] < num[i]:
            break
        i -= 1
    if i == 0 and num[0] == '1':
        return '9' * (n - 1)
    return num[:i] + str(int(num[i]) - 1) + '9' * (n - i - 1)


# easier to code, O(log(n)^2)
def solve2(num):
    n = len(num)
    numint = int(num)
    sols = [int('9' * (n - 1))] if numint > 9 else []
    for i in range(n + 1):
        subs = num[:i]
        if i < n:
            for d in range(10):
                sols.append(int(subs + str(d) + '9' * (n - i - 1)))
    return max(x for x in sols if x <= numint and is_tidy(str(x)))


def read_input():
    n = int(input())
    for case in range(1, n + 1):
        num = input()
        solution = solve(num)
        print(f'CASE #{case}: {solution}')


read_input()
