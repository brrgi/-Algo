import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;


class Solution {
    public static int[][] maps;
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int T = Integer.parseInt(st.nextToken());
            maps = new int[100][100];
            int[] start = new int[2];
            for (int j = 0; j < 100; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < 100; k++) {
                    maps[j][k] = Integer.parseInt(st.nextToken());
                    if (maps[j][k] == 2) {
                        start[0] = j;
                        start[1] = k;
                    }
                }
            }
            System.out.format("#%d %d\n", i + 1, go(start));
        }
    }

    public static int go(int[] starts) {
        if (starts[0] == 0) return starts[1];
        boolean visit[][] = new boolean[100][100];
        int a = starts[0];
        int b = starts[1];
        while (true) {
            if (a == 0) return b;
            visit[a][b] = true;
            if (b - 1 >= 0 && maps[a][b - 1] == 1 && !visit[a][b - 1]) {
                b--;
            } else if (b + 1 < 100 && maps[a][b + 1] == 1 && !visit[a][b + 1]) {
                b++;
            } else {
                a--;
            }
        }
    }
}
