#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct queue{
    int input;
    struct stack* pre_ptr;
    struct stack* post_ptr;
}queue;

// stack * push(queue * top_ptr, int num){
//     stack * new = (stack *)calloc(1, sizeof(stack));
//     new->on_ptr = NULL;
//     new->under_ptr = top_ptr;
//     new->input = num;
//     if(top_ptr != NULL)
//         top_ptr->on_ptr = new;
//     top_ptr = new;
//     return top_ptr;
// }
// stack * pop(stack * top_ptr, int size){
//     if(size != 0){
//         printf("%d\n",top_ptr->input);
//         if(size != 1){
//             top_ptr = top_ptr->under_ptr;
//             free(top_ptr->on_ptr);
//             top_ptr->on_ptr = NULL;
//         }
//         else{
//             free(top_ptr);
//             top_ptr = NULL;
//         }
//     }
//     else
//         printf("-1\n");
//     return top_ptr;
// }
// void size(int stack_size){
//     printf("%d\n",stack_size);
// }
// void empty(int stack_size){
//     if(stack_size == 0)
//         printf("1\n");
//     else
//         printf("0\n");
// }
// void front(stack * top_ptr, int size){
//     if(size != 0)
//         printf("%d\n",top_ptr->input);
//     else
//         printf("-1\n");
// }
// void end(stack * top_ptr, int size){
//     if(size != 0)
//         printf("%d\n",top_ptr->input);
//     else
//         printf("-1\n");
// }

// int main(){
//     queue * front_ptr = (queue *)calloc(1, sizeof(queue));
//     queue * end_ptr = (queue *)calloc(1, sizeof(queue));
//     front_ptr = NULL;
//     end_ptr = NULL;
//     int queue_size = 0;
//     int queue_input = -1;  
//     int inst_cnt = 0;
//     char * instruction = (char *)calloc(20, sizeof(char));

//     printf("명령어의 수와 명령어를 입력하세요\n");
//     scanf("%d%*c",&inst_cnt);
    
//     char ** inst_ptr = (char **)calloc(inst_cnt, sizeof(char *));

//     for(int i = 0 ; i < inst_cnt ; i++)
//         inst_ptr[i] = (char *)calloc(20,sizeof(char));

//     for(int i = 0 ; i < inst_cnt ; i++)
//         fgets(inst_ptr[i],20,stdin);

//     for(int i = 0 ; i < inst_cnt ; i++){
//         if(strchr(inst_ptr[i],' ') == NULL)
//             instruction = strtok(inst_ptr[i],"\n");
//         else{
//             instruction = strtok(inst_ptr[i]," ");
//             queue_input = atoi(strtok(NULL," "));
//         }

//         if(!strcmp(instruction,"push")){
//             top_ptr = push(*front_ptr,end_ptr,queue_input);
//             queue_size ++;
//         }
//         else if(!strcmp(instruction,"pop")){
//             top_ptr = pop(top_ptr,stack_size);
//             if (stack_size >0)
//                 stack_size --;
//         }
//         else if(!strcmp(instruction,"size"))
//             size(stack_size);  
//         else if(!strcmp(instruction,"empty"))
//             empty(stack_size);
//         else if(!strcmp(instruction,"front"))
//             front(top_ptr,stack_size);
//         else if(!strcmp(instruction,"end"))
//             end(top_ptr,stack_size);
//     }
//     return 0;
// }