class Solution {
  public String solution(int a, int b) {
      String[] days = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" };
      int[] month_days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
      int sum_day = 0;
      for(int i = 0; i < a - 1 ; i++){
          sum_day += month_days[i];
      }
      sum_day += b;
      return days[sum_day % 7];
  }
}
