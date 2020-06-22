/*
 * @lc app=leetcode id=9 lang=cpp
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
public:
    bool isPalindrome(int x) {
        // overflow
    //     if(x<0)
    //         return false;
    //     if(x==0)
    //         return true;
        
    //     int reverse = 0;
    //     int temp = x;
    //     while(temp){
    //         reverse = reverse*10 + temp%10;
    //         temp /= 10;
    //     }

    //     if(reverse==x)
    //         return true;
    //     else
    //         return false;
        
    // }
    // https://leetcode.com/problems/palindrome-number/discuss/5165/An-easy-c%2B%2B-8-lines-code-(only-reversing-till-half-and-then-compare)
    // half space
        if(x==0)
            return true;
        if(x<0 || x%10 == 0) // end with 0 makes head error
            return false;
        
        
        int reverse = 0;
        int temp = x;
        while(temp>reverse){
            reverse = reverse*10 + temp%10;
            temp /= 10;
        } // end when reverse is greater than temp

        if(temp == reverse || temp == reverse/10)
            return true;
        else
            return false;
        
    }

};
// @lc code=end

