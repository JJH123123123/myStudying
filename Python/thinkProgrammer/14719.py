from sys import stdin
input = stdin.readline
n, h = map(int,input().split())
st = list(map(int,input().split()))

res = 0
# 구간을 어떻게 나눌까 ? 

for i in range(1, h-1):
    tmp = st[i]
    
    # left
    left = i-1
    left_max = st[left]
    # flag_left = False
    while(left>=0):
        left_max = max(left_max, st[left])
        # if(left_max >= tmp): # 등호 ? 
        #     flag_left = True
        #     break
        left-=1

    # right 
    right = i+1
    right_max = st[right]
    while(right<h):
        right_max = max(right_max, st[right])
        right+=1

    if(left_max > tmp and right_max > tmp):
        res += min(left_max, right_max) - tmp

print(res)






# 4 8
# 3 2 1 2 1 0 3 2
#   1 2 1 2 3 
# 4 8
# 3 2 1 2 1 0 3 2 


