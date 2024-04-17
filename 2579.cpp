#include<iostream>
#include<algorithm>
#define MAX 10005
using namespace std;
int arr[MAX];
int dp[MAX]; int n;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	dp[1] = arr[1];
	dp[2] = arr[1] + arr[2];//연속 두개까지는 밟을 수 있음
	dp[3] = max(arr[1] + arr[3], arr[2] + arr[3]);
	for (int i = 4; i <= n; i++) {
		dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);//위 점화식은 dp가 4개 이상이면 2번의 답과 새로운 영역의 합 또는 영역 두개 연속 밟고 dp3개 이전을 고르는 것이기 때문
	}
	cout << dp[n] << "\n";
	return 0;
}