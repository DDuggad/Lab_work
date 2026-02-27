int searchInsert(int* nums, int numsSize, int target) {
    int position;
    for (int i=0;i<numsSize;i++){
        position=i;
        if(nums[i]>=target){break;}
        position++;
    }
    return position;
}
