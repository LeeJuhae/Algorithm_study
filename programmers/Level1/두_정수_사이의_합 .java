class Solution {
 public long solution(int a, int b){
        long answer = 0;
        int temp;
        if (a>b){
            temp = a;
            a = b;
            b = temp;
        }
        else if (a == b)
            return a;
        for (;a<=b;a++){
            answer += a;
        }
        return answer;
     }
}
