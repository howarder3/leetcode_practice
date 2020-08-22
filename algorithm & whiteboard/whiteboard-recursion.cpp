#include <iostream>

using namespace std;

void e(int n)
{
    if(n > 0)
    {
        e(--n);
        cout<<n<<endl;
        e(--n);
    }
}

int main()
{
    e(3);
    return 0;
}

// 0120


