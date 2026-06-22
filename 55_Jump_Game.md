```java
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int left = 0;
        int idx = 0;
        while(left<n && idx<n){
             if(left>idx ){
                return false;
            }
            idx = Math.max(idx,left+nums[left]);
            left++;
        }
        return true;
    }
}
```