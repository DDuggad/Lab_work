int findTargetSumWays(int* nums, int numsSize, int target) {
    int n = numsSize;
    int sum = 0;
    for (int i=0;i<n;i++) sum+=nums[i];
    if (abs(target) > sum || (target + sum) % 2 != 0 || (target + sum) < 0) {return 0;}
    int sum1= (target+sum)/2;
    int dp[sum1+1];
    for (int i=0;i<=sum1;i++) dp[i]=0;
    dp[0]=1;
    for (int i=0;i<n;i++){
        for (int j=sum1;j>=nums[i];j--){
            dp[j] += dp[j - nums[i]];
        }
    }
    return dp[sum1];
}
