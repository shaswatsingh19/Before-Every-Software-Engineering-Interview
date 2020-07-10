Problem Description :
    Input : [1,2,0,1 ,0]
    Output: [0,0,1,1,2]
    In log(n) time 
    
    It is also called The Dutch National  Flag problem
    
SOLUTION:
arr = list(map(int,input().split()))
le= len(arr)
l = 0
m = 0
h = le- 1
while m <= h:
    if arr[m] == 0:
        temp = arr[m]
        arr[m] = arr[l]
        arr[l] = temp
        m += 1
        l += 1
    elif arr[m] == 1:
        m += 1
    elif arr[m] == 2:
        temp = arr[m]
        arr[m] = arr[h]
        arr[h] = temp
        h -= 1

print(arr)
