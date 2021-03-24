import java.io.*;
import java.util.*;

public class sdfk {
    public static int n, m;
    public static int[][] maps;
    public static int dx[] = {0, 0, 1, -1};
    public static int dy[] = {1, -1, 0, 0};
    public static int time = 0, nums = 0;
    public static boolean visit[][];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        init(br, st);


        while (true) {
            visit = new boolean[n][m];
            cal(0, 0);
            boolean check = true;
            time += 1;
            nums = 0;


            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (maps[i][j] == 1) {
                        check = false;
                    } else if (maps[i][j] == -1) {
                        maps[i][j] = 0;
                        nums++;
                    }
                }
            }

            if (check) {
                break;
            }
        }

        System.out.println(time);
        System.out.println(nums);
    }

    private static void init(BufferedReader br, StringTokenizer st) throws IOException {
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maps = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static void cal(int row, int col) {
        for (int i = 0; i < 4; i++) {
            int newRow = row + dx[i];
            int newCol = col + dy[i];
            if (0 <= newRow && 0 <= newCol && newRow < n && newCol < m) {
                if (visit[newRow][newCol]) {
                    continue;
                }

                if (maps[newRow][newCol] == 1) {
                    maps[newRow][newCol] = -1;
                    continue;
                } else if (maps[newRow][newCol] == -1) {
                    continue;
                }

                visit[row][col] = true;
                cal(newRow, newCol);
            }
        }
    }
}
