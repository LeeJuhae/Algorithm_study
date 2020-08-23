#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct queue{
    int input;
    struct queue * next;
}queue;

void push(queue ** front_ptr, queue ** end_ptr, int size, int num){
    queue * new = (queue *)calloc(1,sizeof(queue));
    if(size == 0)
        *front_ptr = new;
    else
        (*end_ptr)->next = new; 
    *end_ptr = new;
    new->next = NULL;
    new->input = num;
}
void pop(queue ** end_ptr, int size){
    if(size != 0){
        printf("%d\n",(*end_ptr)->input);
        *end_ptr = (*end_ptr)->next;
    }
    else
        printf("-1\n");
}
void size(int queue_size){
    printf("%d\n",queue_size);
}
void empty(int queue_size){
    if(queue_size == 0)
        printf("1\n");
    else
        printf("0\n");
}
void front(queue ** front_ptr, int size){
    if(size != 0)
        printf("%d\n",(*front_ptr)->input);
    else
        printf("-1\n");
}
void back(queue ** end_ptr, int size){
    if(size != 0)
        printf("%d\n",(*end_ptr)->input);
    else
        printf("-1\n");
}

int main(){
    queue * front_p= (queue *)calloc(1, sizeof(queue));
    queue * end_p= (queue *)calloc(1, sizeof(queue));
    front_p = NULL;
    end_p = NULL;
    int queue_size = 0;
    int queue_input = -1;
    
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
            queue_input = atoi(strtok(NULL," "));
        }

        if(!strcmp(instruction,"push")){
            push(&front_p, &end_p, queue_size, queue_input);
            queue_size ++;
        }
        else if(!strcmp(instruction,"pop")){
            pop(&front_p,queue_size);
            if (queue_size >0)
                queue_size --;
        }
        else if(!strcmp(instruction,"size"))
            size(queue_size);  
        else if(!strcmp(instruction,"empty"))
            empty(queue_size);
        else if(!strcmp(instruction,"front"))
            front(&front_p,queue_size);
        else if(!strcmp(instruction,"back"))
            back(&end_p,queue_size);
    }
    return 0;
}