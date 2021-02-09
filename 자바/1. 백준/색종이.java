import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] maps = new int[102][102];

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        for (int i = 0; i < a; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            for (int j=x; j<x+10; j++){
                for (int q=y; q<y+10; q++){
                    maps[j][q]=1;
                }
            }
        }

        int result=0;
        for (int i=0; i<102; i++){
            for (int j=0; j<102; j++){
                if (maps[i][j]==1){
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}
