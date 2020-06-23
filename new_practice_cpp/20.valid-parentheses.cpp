/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
public:
    // bool isValid(string s) {

    //     stack<char> mystack;

    //     int idx = 0;
    //     char next = s[idx];
    //     while(next){
    //         if(next == '(' || next == '[' || next == '{'){
    //             mystack.push(next);
    //             idx++;
    //             next = s[idx];
    //         }
    //         else{
    //             if(mystack.empty()){return false;}
    //             char target = mystack.top();
    //             mystack.pop();
    //             if(target == '(' and next == ')'){idx++; next = s[idx]; }
    //             else if(target == '[' and next == ']'){idx++; next = s[idx]; }
    //             else if(target == '{' and next == '}'){idx++; next = s[idx]; }
    //             else{return false;}
    //         }
    //     }
        
    //     return (mystack.empty())? true : false;


        // https://leetcode.com/problems/valid-parentheses/discuss/9252/2ms-C%2B%2B-sloution
    bool isValid(string s) {
        stack<char> mystack;
        for(char &c : s){
            switch(c){
                case '(': mystack.push(')'); break;
                case '[': mystack.push(']'); break;
                case '{': mystack.push('}'); break;
                // case ')': case ']': case '}': {
                // case mystack.top(): mystack.pop(); break;
                // default: 
                // return false; =
                default:{
                    if(mystack.empty()){return false;}
                    if(mystack.top() == c){mystack.pop();}
                    else{return false;}
                }
                // case ')': {
                //     if(!mystack.empty() && mystack.top()=='('){mystack.pop(); break;}
                //     else{return false;}
                // }
                
                // case ']':{
                //     if(!mystack.empty() && mystack.top()=='['){mystack.pop(); break;}
                //     else{return false;}
                // }
                // case '}':{
                //     if(!mystack.empty() && mystack.top()=='{'){mystack.pop(); break;}
                //     else{return false;}
                // }
            } 
        }
        // cout << mystack.size() << endl;
        return mystack.empty();
    }
};
// @lc code=end

