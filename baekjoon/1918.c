#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stack{
    char input;
    struct stack* under_ptr;
}stack;

void push(stack ** top_ptr, char operator){
    stack * new = (stack *)calloc(1,sizeof(stack));
    new->under_ptr = *top_ptr;
    new->input = operator;
    *top_ptr = new;  
}
void pop(stack ** top_ptr, int size){
    if(size != 0){
        printf("%c",(*top_ptr)->input);
        *top_ptr = (*top_ptr)->under_ptr;
    }
    else
        printf("-1\n");
}

int main(){
    stack * top_p= (stack *)calloc(1, sizeof(stack));
    top_p = NULL;
    int stack_size = 0;
    int i=0;
    char * notation = (char *)calloc(100, sizeof(char));

    //printf("중위표기식을 입력하세요\n");
    scanf("%s",notation);

    while(1){
        if(notation[i]=='\0'){
            break;    
        }else if((notation[i] == '+')||(notation[i] == '-')||(notation[i] == '*')||(notation[i] == '/')){
            push(&top_p,notation[i]);
            stack_size ++;
        }else if(notation[i] == ')'){
            pop(&top_p,stack_size);
            stack_size --;
        }else if(('A'<=notation[i]) && (notation[i]<='Z')){
            printf("%c",notation[i]);
        }
        i++;
    }
    if(stack_size != 0){
        for(;stack_size!=0;stack_size--)
            pop(&top_p,stack_size);
    }
    return 0;
}