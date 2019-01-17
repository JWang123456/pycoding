def superDigit(n, k):
    if len(str(n)) == 1 and k == 1:
        return n
    temp = ''
    for i in range(k):
        temp += str(n)

    return int(recur(temp))


def recur(n):
    if len(n) == 1:
        return n

    nxt = 0
    for index in range(len(n)):
        nxt += int(n[index])

    return recur(str(nxt))

if __name__ == '__main__':
    n = '148'

    k = 3

    result = superDigit(n, k)

    print(result)