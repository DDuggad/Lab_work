/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* frequencySort(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int num[100], freq[100] = {0};
    int top = 0;
    for (int i = 0; i < n; i++) {
        int val = -1;
        for (int j = 0; j < top; j++) {
            if (nums[i] == num[j]) {val = j;break;}
        }
        if (val == -1) {val = top;num[val] = nums[i];top++;}
        freq[val]++;
    }
    for (int i = 0; i < top - 1; i++) {
        for (int j = 0; j < top - i - 1; j++) {
            if (freq[j] > freq[j+1] || (freq[j] == freq[j+1] && num[j] < num[j+1])) {
                int tempFreq = freq[j];freq[j] = freq[j+1];freq[j+1] = tempFreq;
                
                int tempNum = num[j];num[j] = num[j+1];num[j+1] = tempNum;
            }
        }
    }

    int* result = (int*)malloc(n * sizeof(int));
    int index = 0;
    for (int i = 0; i < top; i++) {
        for (int k = 0; k < freq[i]; k++) {
            result[index++] = num[i];
        }
    }
    *returnSize = n;
    return result;
}
