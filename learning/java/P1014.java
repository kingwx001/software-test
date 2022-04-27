package learning.java;

import java.util.Scanner;

public class P1014 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
        for (int i = 1; ; i++) {
            if(N <= i){
                if(i % 2 == 0){
                    System.out.println(N + "/" + (i + 1 - N));
                }else{
                    System.out.println((i + 1 - N) + "/" + N); 
                }
                break;
            }
            N -= i;
        }
		
	}
}  