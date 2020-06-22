/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // https://leetcode.com/problems/add-two-numbers/discuss/997/c%2B%2B-Sharing-my-11-line-c%2B%2B-solution-can-someone-make-it-even-more-concise
        // ListNode preHead(0), *p = &preHead; //store head address
        // int carry = 0;
        // while(l1 || l2 || carry){ // have something
        //     int sum = 0;
        //     if(l1)
        //         sum += l1->val;
        //     else
        //         sum += 0;
        //     if(l2)
        //         sum += l2->val;
        //     else
        //         sum += 0;
        //     if(carry)
        //         sum += carry;
        //     else
        //         sum += 0;
        //     carry = sum / 10;
        //     p->next = new ListNode(sum%10);
        //     p = p->next; // move next

        //     if(l1)
        //         l1 = l1->next;
        //     else
        //         l1 = l1;

        //     if(l2)
        //         l2 = l2->next;
        //     else
        //         l2 = l2;
        // }

        // return preHead.next;        

        ListNode preHead(0), *p = &preHead; // ListNode *p (p value = preHead value)
        
        int a = 10;
        int *pa;
        pa = &a;
        cout<<pa<<endl; // 0x7fffb7b2ebe0
        cout<<*pa<<endl; // 10
        cout<<&pa<<endl; // 0x7fffb7b2ebf0

        int b = 10;
        int *pb = &b;
        cout<<pb<<endl; // 0x7fffb7b2ec10
        cout<<*pb<<endl; // 10
        cout<<&pb<<endl; // 0x7fffb7b2ec20

        int c = 10;
        int *pc;
        *pc = c;
        cout<<pc<<endl; // 0x7fffb7b2eca0
        cout<<*pc<<endl; // 10
        cout<<&pc<<endl; // 0x7fffb7b2ec40

        int d = 10;

        int *pda;
        pda = &d;

        int *pdb = &d;
        
        // int *pdc;
        // *pdc = d;

        cout<<pda<<endl; // 0x7ffd1a07b6e0
        cout<<*pda<<endl; // 10
        cout<<&pda<<endl; // 0x7ffd1a07b6f0
        cout<<pdb<<endl; // 0x7ffd1a07b6e0
        cout<<*pdb<<endl; // 10
        cout<<&pdb<<endl; // 0x7ffd1a07b710
        // cout<<pdc<<endl; 
        // cout<<*pdc<<endl; 
        // cout<<&pdc<<endl; 


        
        int carry = 0;
        while(l1 || l2 || carry){
            int ans = 0;
            ans += (l1 ? l1->val : 0);
            ans += (l2 ? l2->val : 0);
            ans += carry;

            carry = ans / 10;
            p->next = new ListNode(ans % 10); // next pointer
            p = p->next;

            l1 = l1? l1->next : l1; 
            l2 = l2? l2->next : l2; 
            
        }
        return preHead.next;
    }
};





// @lc code=end

