/*
 * @lc app=leetcode id=7 lang=cpp
 *
 * [7] Reverse Integer
 */

// @lc code=start
class Solution {
public:
    // https://leetcode.com/problems/reverse-integer/discuss/4057/Shortest-code-possible-in-c%2B%2B
    int reverse(int x) {
        long long int res = 0;
        while(x)
        {
            res = res * 10 + x % 10;
            x /= 10;
        }
        return (INT_MAX < res || INT_MIN > res) ? 0 : res;
    }


    // https://leetcode.com/problems/reverse-integer/discuss/4124/8-ms-simple-C%2B%2B-solution-which-checks-overflow
    // *overflow crash*
    // int reverse(int x) {
    //     int ans = 0;
    //     while (x){
    //         int temp = ans * 10 + x % 10;
    //         x /= 10;
    //         if(temp /10 != ans) // overflow
    //             return 0;
    //         else
    //             ans = temp;       
    //     }
    //     return ans;
    // }


    // int reverse(int x) {
    //     if(x == 0){
    //         return 0;
    //     }
    //     long long int max = pow(2, 31)-1;
    //     // cout << max;
    //     // if(x >= max){return 0;}

    //     bool flag = true;
    //     if(x < 0){
    //         x = -x;
    //         flag = false;
    //     }
    //     string str_x = to_string(x);
    //     string ans = "";
    //     // vector<char> vec;
        
    //     for(int i=0;i<str_x.length();i++){
    //         // vec.push_back(str_x[str_x.length()-i]);
    //         ans += str_x[str_x.length()-1-i];
    //     }
    //     // cout << ans;
    //     // printf("%s",ans.c_str());
    //     // cout << atoi(ans.c_str());

    //     long long int ans_x = atoi(ans.c_str());

    //     if(flag){ // > 0
    //         if(ans_x <= max){
    //             return ans_x;
    //         }
    //         else{
    //             return 0;
    //         }
    //     }
    //     else{ // <0
    //         if(-ans_x >= -max+1){
    //             return -ans_x;
    //         }
    //         else{
    //             return 0;
    //         }
    //     }
    // }
};
// @lc code=end

