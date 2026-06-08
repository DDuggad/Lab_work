int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int total = 1;
    for (int i = 1; i <= numsSize; i++) total *= i;
    
    *returnSize = total;
    *returnColumnSizes = (int*)malloc(total * sizeof(int));
    int** res = (int**)malloc(total * sizeof(int*));

    int p[6], d[6];
    for (int i = 0; i < numsSize; i++) { 
        p[i] = i; 
        d[i] = 0; 
    }

    for (int count = 0; count < total; count++) {
        res[count] = (int*)malloc(numsSize * sizeof(int));
        (*returnColumnSizes)[count] = numsSize;
        for (int i = 0; i < numsSize; i++) res[count][i] = nums[p[i]];

        if (count == total - 1) break; 

        int mob = -1, m_idx = -1;
        for (int i = 0; i < numsSize; i++) {
            if (d[i] == 0 && i > 0 && p[i] > p[i - 1]) {
                if (p[i] > mob) { mob = p[i]; m_idx = i; }
            }
            if (d[i] == 1 && i < numsSize - 1 && p[i] > p[i + 1]) {
                if (p[i] > mob) { mob = p[i]; m_idx = i; }
            }
        }

        int s_idx = (d[m_idx] == 0) ? m_idx - 1 : m_idx + 1;
        
        int t = p[m_idx]; p[m_idx] = p[s_idx]; p[s_idx] = t;
        t = d[m_idx]; d[m_idx] = d[s_idx]; d[s_idx] = t;

        for (int i = 0; i < numsSize; i++) {
            if (p[i] > mob) d[i] = !d[i];
        }
    }
    return res;
}
