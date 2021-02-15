import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;
    static int[] s;
    static int[] b;
    static int result;
    static int[] visited;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        s = new int[n];
        b = new int[n];
        visited = new int[n];
        result = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            s[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= n; i++) {
            dfs(visited, 0, 0, i);
        }

        System.out.println(result);
    }

    static void dfs(int[] visit, int select, int cur, int choice) {
        if (select == choice) {
            int newS = 1;
            int newB = 0;
            for (int i = 0; i < n; i++) {
                if (visit[i]==1){
                    newS*=s[i];
                    newB+=b[i];
                }
            }


            if (Math.abs(newS-newB)<result){
                result=Math.abs(newS-newB);
            }
            return;
        }

        for (int i = cur; i < n; i++) {
            visit[i] = 1;
            dfs(visit, select + 1, i + 1, choice);
            visit[i] = 0;
        }
    }

}
