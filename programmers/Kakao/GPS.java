package programmers.Kakao;
import java.util.*;

class GPS {
	public int solution(int n, int m, int[][] edge_list, int k, int[] gps_log) {
		int answer = 0;
		int inf = 987654321;
		int dp[][] = new int [k][n+1];
		ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

		for (int i = 0 ; i < n + 1 ; i++)
			graph.add(new ArrayList<Integer>());

		for (int i = 0 ; i < edge_list.length ; i++) {
			int start = edge_list[i][0];
			int end = edge_list[i][1];
			graph.get(start).add(end);
			graph.get(end).add(start);
		}

		for (int i = 0 ; i < dp.length ; i++) {
			Arrays.fill(dp[i], inf);
		}
		dp[0][gps_log[0]] = 0;

		for (int i = 1 ; i < k ; i++) {
			for (int j = 1 ; j < n+1 ; j++) {
				dp[i][j] = Math.min(dp[i][j], dp[i-1][j]);

				for (int node : graph.get(j)) {
					dp[i][j] = Math.min(dp[i-1][node], dp[i][j]);
				}
				dp[i][j] += gps_log[i] == j ? 0 : 1;
			}
		}
		if (dp[k-1][gps_log[k-1]] >= inf)
			answer = -1;
		else {
			answer = dp[k-1][gps_log[k-1]];
		}
		return answer;
	}
	// public static void main(String[] args) {
	// 	int[][] edge_list = {{1, 2}, {1, 3}, {2, 3}, {2, 4}, {3, 4}, {3, 5}, {4, 6}, {5, 6}, {5, 7}, {6, 7}};
	// 	int [] gps_log = {1,2,3,3,6,7};
	// 	GPS g = new GPS();
	// 	int ans = g.solution(7,10,edge_list, 6, gps_log);
	// 	System.out.println(ans);
	// }
}
