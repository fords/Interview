/*
Reverse bits of 32 bits unsigned integers
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
*/


public class ReverseBits {

    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; ++i) {
            res = res << 1  | (n & 1);
            n >>= 1;
        }
        return res;
    }

}
