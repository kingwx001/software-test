package learning.java;


import java.util.Scanner;
public class P1003 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
        int[][] rect = new int[n][4];
        
        for (int i = 0; i < n; i++) {
            rect[i] = new int[]{sc.nextInt(),sc.nextInt(),sc.nextInt(),sc.nextInt()};
        }
        
        int x = sc.nextInt(),y = sc.nextInt();

        for(int i = n - 1;i >= 0;i--){
            if(x >= rect[i][0] && y >= rect[i][1] && x <= rect[i][0] + rect[i][2] && y <= rect[i][1] + rect[i][3]){
                System.out.println(i + 1);
                return;
            }
        }

        System.out.println(-1);
		
	}
}  