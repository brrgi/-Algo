import java.io.*;
import java.util.*;


class Solution {
    static int maxVal;
    static int a;
    static int b;
    static int[][] maps;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int TestCase = Integer.parseInt(br.readLine());
        for (int t = 0; t < TestCase; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            maps = new int[a][a];

            for (int i = 0; i < a; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < a; j++) {
                    maps[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            maxVal = 0;
            for (int i = 0; i <= a - b; i++) {
                for (int j = 0; j <= a - b; j++) {
                    calcultateMaxArea(i, j);
                }
            }
            bw.write("#" + (t+1) + " " + maxVal+"\n");
        }
        bw.flush();
    }

    static void calcultateMaxArea(int x, int y) {
        int sum = 0;
        for (int i = x; i < x + b; i++) {
            for (int j = y; j < y + b; j++) {
                sum += maps[i][j];
            }
        }
        if (maxVal < sum) maxVal = sum;
    }
}
