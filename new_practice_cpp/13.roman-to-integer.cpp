/*
 * @lc app=leetcode id=13 lang=cpp
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
public:
    // int romanToInt(string s) {

    //     map<char,int> mydict = {
    //         {'I', 1},
    //         {'V', 5},
    //         {'X', 10},
    //         {'L', 50},
    //         {'C', 100},
    //         {'D', 500},
    //         {'M', 1000}
    //     };
    //     // map<string, int> mydict2 = {
    //     //     {'IV', 4},
    //     //     {'IX', 9},
    //     //     {'XL', 40},
    //     //     {'XC', 90},
    //     //     {'CD', 400},
    //     //     {'CM', 900}
    //     // };
    //     int ans = 0;
    //     int idx = 0;
    //     while(idx < s.length()){
    //         char now_s = s[idx];
    //         if(idx+1 < s.length() && now_s == 'I'){
    //             if(s[idx+1] == 'V'){ans += 4; idx += 2;}
    //             else if(s[idx+1] == 'X'){ans += 9; idx += 2;}
    //             else{ans += 1; idx += 1;}
    //         }
    //         else if(idx+1 < s.length() && now_s == 'X'){
    //             if(s[idx+1] == 'L'){ans += 40; idx += 2;}
    //             else if(s[idx+1] == 'C'){ans += 90; idx += 2;}
    //             else{ans += 10; idx += 1;}
    //         }
    //         else if(idx+1 < s.length() && now_s == 'C'){
    //             if(s[idx+1] == 'D'){ans += 400; idx += 2;}
    //             else if(s[idx+1] == 'M'){ans += 900; idx += 2;}
    //             else{ans += 100; idx += 1;}
    //         }
    //         else{ans += mydict[now_s]; idx += 1;}
    //     };
    // return ans;
    // }


    // https://leetcode.com/problems/roman-to-integer/discuss/6547/Clean-O(n)-c%2B%2B-solution
    int romanToInt(string s) {

        map<char,int> mydict = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        if(s.length() == 0){return 0;}
        if(s.length() == 1){return mydict[s[0]];}

        int sum = mydict[s[s.length()-1]];
        for(int i = s.length()-2; i>=0 ;i--){
            if(mydict[s[i+1]] > mydict[s[i]]){ // bigger than before 
            // I V
            // 0 1
            // V(5) > I(1)
                sum -= mydict[s[i]];
            }
            else{
                sum += mydict[s[i]];
            }
        }
        return sum;    
    }
};
// @lc code=end

