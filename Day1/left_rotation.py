def rotateLeft(d, arr):
    n = len(arr)
    d = d % n  
    return arr[d:] + arr[:d]
n,d=map(int,input().split(' '))
arr=list(map(int,input().split()))
print(rotateLeft(d,arr))