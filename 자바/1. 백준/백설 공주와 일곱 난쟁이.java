import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int[] visited;
    static int[] numbers;
    public static void main(String args[]) throws Exception {

        numbers = new int[9];
        visited = new int[9];


        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            numbers[i] = Integer.parseInt(st.nextToken());
        }


        dfs(visited, 0, 0, 7);


    }

    static void dfs(int[] visit, int select, int cur, int choice) {
        if (select == choice) {
            int result=0;
            for (int i = 0; i < 9; i++) {
                if (visit[i]==1){
                    result+=numbers[i];
                }
            }

            if (result==100){
                for (int i = 0; i < 9; i++) {
                    if (visit[i]==1){
                        System.out.println(numbers[i]);
                    }
                }
                System.exit(0);
            }
            return;
        }

        for (int i = cur; i < 9; i++) {
            visit[i] = 1;
            dfs(visit, select + 1, i + 1, choice);
            visit[i] = 0;
            dfs(visit, select, i+1, choice);
        }
    }

}
