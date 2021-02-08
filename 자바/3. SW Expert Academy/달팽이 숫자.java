import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
    static int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int num;
        int dirIndex;
        int startVal;
        int row, col;
        int sqr;
        for (int i = 0; i < T; i++) {
            dirIndex = 0;
            startVal = 1;
            row = 0;
            col = 0;
            st = new StringTokenizer(br.readLine());
            num = Integer.parseInt(st.nextToken());
            if (num == 1) {
                System.out.format("#%d\n", i + 1);
                System.out.println(1);
                continue;
            }
            int[][] maps = new int[num][num];
            sqr = (int) Math.pow(num, 2);
            while (sqr >= startVal) {
                maps[row][col] = startVal++;
                int nextRow = row + dir[dirIndex][0];
                int nextCol = col + dir[dirIndex][1];
                if (0 <= nextRow && nextRow < num && 0 <= nextCol && nextCol < num) {
                    if (maps[nextRow][nextCol] == 0) {
                        row = nextRow;
                        col = nextCol;
                    } else {
                        if (dirIndex == 3) {
                            dirIndex = 0;
                        } else {
                            dirIndex++;
                        }
                        row = row + dir[dirIndex][0];
                        col = col + dir[dirIndex][1];
                    }
                } else {
                    if (dirIndex == 3) {
                        dirIndex = 0;
                    } else {
                        dirIndex++;
                    }
                    row = row + dir[dirIndex][0];
                    col = col + dir[dirIndex][1];
                }
                if (maps[row][col] != 0) {
                    if (dirIndex == 3) {
                        dirIndex = 0;
                    } else {
                        dirIndex++;
                    }
                    row = row + dir[dirIndex][0];
                    col = col + dir[dirIndex][1];
                }
            }

            System.out.format("#%d\n", i + 1);
            for (int[] t : maps) {
                for (int tt : t) {
                    System.out.print(tt + " ");
                }
                System.out.println();
            }
        }
    }
}
