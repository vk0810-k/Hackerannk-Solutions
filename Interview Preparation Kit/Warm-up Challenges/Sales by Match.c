#include <stdio.h>

int main() {
 int n;
    scanf("%d",&n);
 int a[1000] = {};
 for(int i = 0; i < n; i++) {
        int c;
        scanf("%d",&c);
        a[c]++;
    }

 int res = 0;
 for(int i = 0; i <= 100; i++){
         res += a[i] / 2;
     }
 printf("%d\n",res);
 return 0;
}
