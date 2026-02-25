int findGCD(int* nums, int numsSize) {
    int n=numsSize;
    int gcd=nums[0];
    for (int i=1;i<n;i++){
        if(gcd==1){return gcd;}
        int m=gcd, n=nums[i];
        while (n!=0){
            int r=m%n;
            m=n;n=r;
        }
        gcd=m;
    }
    return gcd;
}
