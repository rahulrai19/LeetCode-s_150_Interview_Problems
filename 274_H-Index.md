class Solution {
    public int hIndex(int[] citations) {
        //citations[i]>= i+1;
        int n = citations.length;
        Arrays.sort(citations);
        int h = 0;
        for(int i=0;i<n;i++){
            h = Math.max(h,Math.min(citations[i],n-i));
        }
        return h;
    }
}