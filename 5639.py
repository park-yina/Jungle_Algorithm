import sys
sys.setrecursionlimit(10**9)

# 이미 대가리는 알고있으니 왼오를 구분해야한다.
# 그런데 전위순환의 결과물은 대가리 왼 오 이므로, 대가리의 바로 뒤가 왼쪽이다.
# 왼쪽에서 키보다 작으면 또다시 왼쪽 서브트리 아니면 오른쪽으로 붙인다.
# 이후 최종적은 왼쪽보다 큰 친구가 등장하면(예제에서는 45보다 큰 98등장)
pre = []

# 엔터 들어올 때까지 입력
while True:
    try:
        pre.append(int(sys.stdin.readline().rstrip()))
    except:
        break
def post_order(s,e):
    if(s>e):return
    global pre
    right=e+1
    for i in range (s+1,e+1):
        if(pre[s]<pre[i]):
            #더 작다는 것은 왼쪽에 속한다는 뜻이다
            right=i
            break
    post_order(s+1,right-1)
    post_order(right,e)
    print(pre[s])
post_order(0,len(pre)-1)

