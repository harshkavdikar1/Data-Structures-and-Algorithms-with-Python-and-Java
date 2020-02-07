public class MedianOfSortedArrays {
    
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        if (m>n){
            return median(nums2, nums1, n, m);
        }
        return median(nums1, nums2, m, n);
    }
    
    public double median(int[] A, int[] B, int m, int n){
        
        int low = 0;
        int high = m;
        int balancer = (m + n + 1)/2;
        while (low<=high){
            int midA = (low + high)/2;
            int midB = balancer - midA;
            
            if (midA > 0 && A[midA-1] > B[midB])
                high = midA - 1;
            else if (midA < m && A[midA] < B[midB-1])
                low = midA + 1;
            else{
                double L;
                if (midA==0) L = B[midB-1];
                else if (midB==0) L = A[midA-1];
                else L = Math.max(A[midA-1], B[midB-1]);
                
                if ((m+n)%2 == 1) return L;
                
                double R;
                if (midA==m) R = B[midB];
                else if (midB==n) R = A[midA];
                else R = Math.min(A[midA], B[midB]);
                
                return (L+R)/2.0;
            }
        }
        return 0.0;
    }

}