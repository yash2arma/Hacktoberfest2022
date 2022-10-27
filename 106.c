#include<stdio.h>
#include<string.h>
int main()
{
    char str[50], c, d; int i, l, count=0;
    printf("enter a string :");
    gets(str);
    printf("enter character to be removed: ");
    scanf("%c",d);
    printf("enter the string to be replaced: ");
    scanf("%c",&c);
    l=strlen(str);
    for(i=0;i<1;i++)
    {
        if(str[i]==d)
        {
            str[i]=c;
        }
    }
    printf("result = %s\n",str);
    return 0;
}