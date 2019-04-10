#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stack{
    int input;
    struct stack* ptr;
}stack;

int main(){
    struct* top_ptr = NULL;
    int stack_size = 0;

    int inst_cnt = 0;
    char * instruction = (char *)calloc(20, sizeof(char));

    printf("명령어의 수와 명령어를 입력하세요\n");
    scanf("%d%*c",&inst_cnt);
    
    char ** inst_ptr = (char **)calloc(inst_cnt, sizeof(char *));
    for(int i = 0 ; i < inst_cnt ; i++)
        inst_ptr[i] = (char *)calloc(20,sizeof(char));

    for(int i = 0 ; i < inst_cnt ; i++){
        fgets(inst_ptr[i],20,stdin);
    }

    for(int i = 0 ; i < inst_cnt ; i++){
        if(strchr(inst_ptr[i],' ') == NULL)
            instruction = strtok(inst_ptr[i],"\n");
        else
            instruction = strtok(inst_ptr[i]," ");

        if(!strcmp(instruction,"push")){
            push(top_ptr);
        }
        else if(!strcmp(instruction,"pop")){
            pop();
        }
        else if(!strcmp(instruction,"size")){
            size(stack_size);
        }       
        else if(!strcmp(instruction,"empty")){
            empty(stack_size);
        }
        else if(!strcmp(instruction,"top")){
            top();
        }
    }
    return 0;

}
void push(int num){

}
void pop(){

}
void size(int stack_size){
    printf("%d\n",stack_size);
}
void empty(int stack_size){
    if(stack_size == 0)
        printf("1\n");
    else
        printf("0"\n);
}
void top(){

}