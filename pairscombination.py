
def pairscombination():
    n = 4
    k = 2
    ll = []

    for i in range(1,n):
        for j in range(i+1,n+1):
            l = [0,1]
            l[0] = i
            l[1] = j
            ll.append(l)

    print(ll)

if __name__ == '__main__':
    pairscombination()