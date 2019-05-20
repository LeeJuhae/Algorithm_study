def solution(loc):
    if [loc[0][0]+loc[2][0],loc[0][1]+loc[2][1]] == [loc[1][0]*2,loc[1][1]*2]:
        print("WHERE IS MY CHICKEN?")
    else:
        print("WINNER WINNER CHICKEN DINNER!")

solution([[12,10],[24,20],[36,30]])
solution([[1,1],[1,2],[2,1]])
