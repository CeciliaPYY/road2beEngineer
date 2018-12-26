#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <queue>
#include <string.h>
using namespace std;


typedef struct CSNode 
{
    char data;
    struct CSNode *firstChild;
    struct CSNode *nextSibling;
}CSNode, *CSTree 

void createTree(CSTree &T)
{
    queue<CSTree> Q;
    char buffChild[20];
    memset(buffChild, 0, 20);
    printf("请输入根结点（字符，以#代表空）：\n");
    scanf("%c", buffChild[0]);
    if (buffChild[0] != '#')
    {
        T = (CSTree)malloc(sizeof(CSNode));
        T->data = buffChild[0];
        T->nextSibling = NULL;
        Q.push(T);
        while(!Q.empty())
        {
            CSTree e;
            e = Q.front();
            Q.pop();
            printf("请按长幼顺序输入结点%c的孩子（输入的字符以#结束）：\n", e->data);
            scanf("%s", buffChild);
            if (buffChild[0] != '#')
            {
                CSTree q;
                q = (CSTree)malloc(sizeof(CSNode));
                q->data = buffChild[0];
                e->firstChild = q;
                Q.push(q);
                CSTree p = q;
                for (int i=1; i < strlen(buffChild) - 1; i++)
                {
                    q = (CSTree)malloc(sizeof(CSNode));
                    q->data = buffChild[i];
                    p->nextSibling = q;
                    Q.push(q);
                    p = q;
                }
                p->nextSibling = NULL;
            }
            else
            {
                e->firstChild = NULL;
            }

        }
    }
    else
    {
        T = NULL; // 空树
    }
}
