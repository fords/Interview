/*
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate
the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
*/
class CountingBits {
    public int bruteforce(int[] nums){

    }

    public int missingNumber(int[] nums) {
      int i = 0;
      int b = 1;
      int[] dp = new int[num+1];
      while(b <= num){
        while (i < b && i + B <= num){
          dp[i+b] = dp[i] + 1;
          i ++;
        }
        i = 0;
        b = b << 1;
      }
    }

}
