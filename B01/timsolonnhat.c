#include <stdio.h>
 
int main() 
{
    int a, b, c;
 
    printf("Enter a, b and c\n");
    scanf("%d%d%d", &a, &b, &c);
 
    int max = a;
    if(max < b) 
    {
        max = b;
    }
 
    if(max < c) {
        max = c;
    }
 
    printf("Max is %d\n", max);
 
    return 0;
}

