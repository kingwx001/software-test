
import java.util.Scanner;
public class P1002 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(),m =sc.nextInt();
		int a = sc.nextInt(),b =sc.nextInt();
		int[][] matrix = new int[n + 1][m + 1];
		matrix[a][b] = 1;
		
		for(int i = 0;i <= n;i++){
			for(int j = 0;j <= m;j++){
				if(Math.abs(i - a) == 1 && Math.abs(j - b) == 2 || Math.abs(i - a) == 2 && Math.abs(j - b) == 1){
					matrix[i][j] = 1;
				}
			}
		}
		
		int[][] dp = new int[n + 2][m + 2];
		dp[0][1] = 1;
		
		for(int i = 0;i <= n;i++){
			for(int j = 0;j <= m;j++){
				if(matrix[i][j] != 1){
					dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j];
				}
				else{
					dp[i + 1][j + 1] = 0;
				}
			}
		}
		System.out.println(dp[n + 1][m + 1]);
	}
}  