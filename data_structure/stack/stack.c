#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stack{
    int input;
    struct stack* on_ptr;
    struct stack* under_ptr;
}stack;

void push(stack ** top_ptr, int num){
    stack new;
    new.on_ptr = (stack *)calloc(1, sizeof(stack));
    new.under_ptr = (stack *)calloc(1, sizeof(stack));
    new.on_ptr = NULL;
    new.under_ptr = *top_ptr;
    new.input = num;
    *top_ptr = &new;
}
void pop(stack ** top_ptr, int size){
    if(size != 0){
        printf("%d\n",(*top_ptr)->input);
        if(size != 1){
            *top_ptr = ((*top_ptr)->under_ptr);
            (*top_ptr)->on_ptr = NULL;
        }
        else{
            *top_ptr = NULL;
        }
    }
    else
        printf("-1\n");
}
void size(int stack_size){
    printf("%d\n",stack_size);
}
void empty(int stack_size){
    if(stack_size == 0)
        printf("1\n");
    else
        printf("0\n");
}
void top(stack ** top_ptr, int size){
    if(size != 0)
        printf("%d\n",(*top_ptr)->input);
    else
        printf("-1\n");
}

int main(){
    stack * top_ptr = (stack *)calloc(1, sizeof(stack));
    top_ptr = NULL;
    int stack_size = 0;
    int stack_input = -1;
    
    int inst_cnt = 0;
    char * instruction = (char *)calloc(20, sizeof(char));

    printf("명령어의 수와 명령어를 입력하세요\n");
    scanf("%d%*c",&inst_cnt);
    
    char ** inst_ptr = (char **)calloc(inst_cnt, sizeof(char *));

    for(int i = 0 ; i < inst_cnt ; i++)
        inst_ptr[i] = (char *)calloc(20,sizeof(char));

    for(int i = 0 ; i < inst_cnt ; i++)
        fgets(inst_ptr[i],20,stdin);

    for(int i = 0 ; i < inst_cnt ; i++){
        if(strchr(inst_ptr[i],' ') == NULL)
            instruction = strtok(inst_ptr[i],"\n");
        else{
            instruction = strtok(inst_ptr[i]," ");
            stack_input = atoi(strtok(NULL," "));
        }

        if(!strcmp(instruction,"push")){
            push(&top_ptr,stack_input);
            stack_size ++;
        }
        else if(!strcmp(instruction,"pop")){
            pop(&top_ptr,stack_size);
            if (stack_size >0)
                stack_size --;
        }
        else if(!strcmp(instruction,"size"))
            size(stack_size);  
        else if(!strcmp(instruction,"empty"))
            empty(stack_size);
        else if(!strcmp(instruction,"top"))
            top(&top_ptr,stack_size);
    }
    return 0;
}