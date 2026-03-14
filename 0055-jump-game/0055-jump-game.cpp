class Solution {
public:
    vector<int> dp;
    int solve(vector<int>&nums, int idx){
        int n= nums.size();
        if(idx>=n-1)return true;
        if(dp[idx]!=-1)return dp[idx];
        
        for(int i=1; i<=nums[idx]; i++){
            if(solve(nums,idx+i)==true){
                return dp[idx]=1;
            }
        }
        return dp[idx]=0;
    }
    bool canJump(vector<int>& nums) {
        
        dp.assign(nums.size(), -1);
        return solve( nums,0);
    }
};