
def powerSum(X, N):
    res = []
    l = []
    helper(res, 0, 1, X, N, l)
    
    return len(res)

def helper(res, total, start, X, N, l):
    if total == X:
        copy = l.copy()
        print(copy)
        res.append(copy)
    else:
        for i in range(start, X + 1):
            
            temp = i**N
            total += temp
            l.append(i)
            if total > X:
                total -= temp
                l.remove(i)
                break
            helper(res, total, i+1, X, N, l)
            total -= temp
            l.remove(i)

if __name__ == '__main__':

    X = 100

    N = 2

    result = powerSum(X, N)
    
    print(result)