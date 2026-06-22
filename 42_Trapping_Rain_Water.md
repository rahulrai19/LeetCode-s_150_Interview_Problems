class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length-1;
        int leftMax = 0,rightMax = 0;
        int maxtrap = 0;
        while(left<right){
            leftMax = Math.max(leftMax,height[left]);
            rightMax = Math.max(rightMax,height[right]);

            if(leftMax<rightMax){
                maxtrap+= leftMax - height[left];
                left++;
            }else{
                maxtrap+=rightMax -height[right];
                right--;
            }

        }
        
      return maxtrap;
    }
}