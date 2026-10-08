import java.util.Arrays;

class Solution {
    public int minCost(int n, int[] cuts) {
        int m = cuts.length;
        // Create a new array with the endpoints 0 and n included
        int[] c = new int[m + 2];
        for (int i = 0; i < m; i++) {
            c[i + 1] = cuts[i];
        }
        c[0] = 0;
        c[m + 1] = n;
        
        // Sort the cuts so we can process them as ordered segments
        Arrays.sort(c);
        
        // dp[i][j] will store the minimum cost to cut the stick from c[i] to c[j]
        int[][] dp = new int[m + 2][m + 2];
        
        // len is the number of segments between i and j
        for (int len = 2; len < m + 2; len++) {
            for (int i = 0; i < m + 2 - len; i++) {
                int j = i + len;
                dp[i][j] = Integer.MAX_VALUE;
                
                // Try making the first cut at every possible position k between i and j
                for (int k = i + 1; k < j; k++) {
                    int cost = dp[i][k] + dp[k][j] + (c[j] - c[i]);
                    dp[i][j] = Math.min(dp[i][j], cost);
                }
            }
        }
        
        // The answer is the cost to process the entire stick from the 0th index to the last
        return dp[0][m + 1];
    }
}
