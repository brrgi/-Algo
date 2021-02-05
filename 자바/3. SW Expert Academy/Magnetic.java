import java.io.*;
import java.util.*;


class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, result;

    public static void main(String args[]) throws Exception {
        for (int i = 0; i < 10; i++) {
            result = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            int[][] maps = new int[n][n];
            for (int j = 0; j < 100; j++) {
                st = new StringTokenizer(br.readLine());
                for (int q = 0; q < 100; q++) {
                    maps[j][q] = Integer.parseInt(st.nextToken());
                }
            }

            for (int j = 0; j < 100; j++) {
                int check = 0;
                for (int q = 0; q < 100; q++) {
                    if (maps[q][j] == 1) {
                        check = 1;
                    }
                    if (check == 1 && maps[q][j] == 2) {
                        result++;
                        check = 0;
                    }
                }
            }
            bw.write("#" + (i + 1) + " " + result + "\n");
        }
        bw.flush();
    }
}
