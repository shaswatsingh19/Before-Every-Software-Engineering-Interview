# arr = [1,2,3,4,1,2,3]
#output  : 1,2,3

ar = list(map(int,input().split()))
di = {}
for i in ar:
    if i not in di:
        di[i] = 1
    else:
        di[i] = di[i] + 1
print(di)
no_dup = True
for k,v in di.items():
    if v == 1:
        print(k,"\t")
        no_dup = False
if no_dup == True:
    print(-1)
