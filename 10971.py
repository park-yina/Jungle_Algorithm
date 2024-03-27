import sys 
global INF
INF= float("inf")
#이 문제 딱봐도 dfs를 도는데 거기에 가격을 추가한거 같다..근데 그걸 어떻게 해야할까
# 대충 보면 내가 어디에 있는지랑 이제 지금까지 더해진 가격 이번 graph를 통해 생긴 비용을 더하고 이제 횟수를 더해서 횟수가 grahp전체를 돌면 다음번 지점부터 비교하는 문제인데
#그래서 이걸 해결하기 위해서 최악의 상황인 INF를 define함수 쓰듯이 맨 위에 넣어놓은 뒤에 쟬아 이제 지금 ans를 어찌저찌 하면 정답이 나올텐데 그 어찌저찌가 뭐더라
global n
n=0
def input_map(n):
    map_ = []
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        map_.append(row)
    return map_
def dfs(start,cost,cnt):
    if(cnt-1==n):


# 일단 c++로 스케치를 하고 파이썬으로 고쳐보자
#define INF 987654321
#define MAX 15
bool visit[MAX][MAX]
int n, int graph[MAX][MAX],int ans;
using namespace std;
void input(){
    cin>>n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            cin>>graph[i][j]
        }
    }
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);cout.tie(0);``````       
}