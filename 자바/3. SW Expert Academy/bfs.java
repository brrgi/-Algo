import java.io.*;
import java.util.*;

class pair {
    int row, col;

    public pair(int row, int col) {
        super();
        this.row = row;
        this.col = col;
    }
}

public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int[][] maps;
    static int[][] visit;
    static int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    static int length;
    static Queue<pair> queue = new LinkedList<>();

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TestCase = Integer.parseInt(st.nextToken());
        for (int j = 0; j < TestCase; j++) {
            st = new StringTokenizer(br.readLine());
            length = Integer.parseInt(st.nextToken());
            maps = new int[length][length];
            visit = new int[length][length];

            for (int i = 0; i < length; i++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < length; k++) {
                    int x = Integer.parseInt(st.nextToken());
                    maps[i][k] = x;
                    visit[i][k] = -1;
                }
            }
            visit[0][0] = 0;
            queue.add(new pair(0, 0));
            bfs();
            bw.write("#" + (j + 1) + " " + visit[length - 1][length - 1] + "\n");
        }
        bw.flush();
    }

    static void bfs() {
        while (!queue.isEmpty()) {
            pair temp = queue.poll();
            if (maps[temp.row][temp.col] == 1 || visit[length - 1][length - 1] != -1) break;
            for (int[] direction : dir) {
                int newRow = temp.row + direction[0];
                int newCol = temp.col + direction[1];
                if (0 <= newRow && newRow < length && 0 <= newCol && newCol < length) {
                    if (visit[newRow][newCol] == -1 && maps[newRow][newCol] == 0) {
                        queue.add(new pair(newRow, newCol));
                        visit[newRow][newCol] = visit[temp.row][temp.col] + 1;
                    }
                }
            }
        }
    }
}
