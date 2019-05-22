def solution(loc):
    if [loc[0][0]+loc[2][0],loc[0][1]+loc[2][1]] == [loc[1][0]*2,loc[1][1]*2]:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")

solution([[12,10],[24,20],[36,30]])
solution([[1,1],[1,2],[2,1]])

###Question
##입력
#프로그램의 입력은 표준 입력으로 받는다.
#스쿼드는 총 4명으로 구성되며 준서는 멀리서 저격을 하기 때문에 좌표가 주어지지 않는다.
#따라서 첫 번째 줄부터 세 번째 줄까지 x, y (1 ≤ x, y ≤ 1000) 두 개의 자연수가 각각 주어진다.
#각 줄의 x, y는 한 명의 팀원이 상대방 화면에서 어떤 위치인지 나타낸다.
#그리고 팀원들은 항상 서로 다른 위치에 있다.

##출력
#프로그램의 출력은 표준 출력으로 한다. 
#팀원의 위치가 직선이 될 때 ‘WHERE IS MY CHICKEN?’ 을, 아닌 경우 ‘WINNER WINNER CHICKEN DINNER!’ 를 출력한다.
