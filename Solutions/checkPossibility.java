// NAME : Non-decreasing Array
// LINK : https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/
// DATE : 06/05/2021

class Solution {
    public boolean checkPossibility(int[] nums) {
        boolean needModifiation = false;
        for (int i = 1; i < nums.length; i ++) {
            if (nums[i - 1] > nums[i]) {
                if (needModifiation) {
                    return false;
                }
                needModifiation = true;
                if (! (i == 1 || nums[i - 2] <= nums[i])) {
                    nums[i] = nums[i - 1];
                }
            }
        }
        return true;
    }
}