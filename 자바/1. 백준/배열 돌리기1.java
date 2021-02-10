import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] maps;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        int floor= Math.min(n,m)/2;

        int[][] maps= new int[n][m];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                maps[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0; i<r; i++){
            for (int j=0; j<floor; j++){
                int up = j;
                int down = n-(j+1);
                int right = m-(j+1);
                int left = j;
                int temp = maps[j][j];
                for (int k=left; k<right; k++){
                    maps[up][k]=maps[up][k+1];
                }
                for (int k=up; k<down; k++){
                    maps[k][right]=maps[k+1][right];
                }
                for (int k=right; k>left; k--){
                    maps[down][k]=maps[down][k-1];
                }
                for (int k=down; k>up; k--){
                    maps[k][left]=maps[k-1][left];
                }
                maps[up+1][left]=temp;
            }
        }

        for (int x[] : maps){
            for (int y : x){
                System.out.print(y+" ");
            }
            System.out.println();
        }
    }
}
