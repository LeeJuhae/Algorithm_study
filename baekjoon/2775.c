#include <stdio.h>
#include <stdlib.h>
int main(){
    int apt[15][14];
    int input;
    int * info;
    scanf("%d",&input);

    info = (int *)calloc(input*2,sizeof(int));
    for(int i = 0 ; i < input*2 ; i++)
        scanf("%d",&info[i]);

    for(int i = 0 ; i < 15 ; i++)
        apt[i][0] = 1;
    for(int i = 1 ; i < 14 ; i++)
        apt[0][i] = i+1;
    
    for(int i = 1 ; i < 15 ; i++)
        for(int j = 1 ; j < 14 ; j++)
            apt[i][j] = apt[i-1][j] + apt[i][j-1];
    
    for(int i = 0 ; i < input*2 ;){
        printf("%d\n",apt[info[i]][info[i+1]-1]);
        i += 2;
    }
    return 0;
}