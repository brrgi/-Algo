import java.io.*;
import java.util.*;
 
 
class Solution {
 
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] maps;
    static boolean[][] visit;
    static int[][] dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    static int n=0;
    static int result;
    static int roomNumber;
    public static void dfs(int row, int col) {
        visit[row][col] = true;
        result++;
        for (int[] a : dir) {
            int newRow = row + a[0];
            int newCol = col + a[1];
            if (0<=newRow && newRow<n && 0<=newCol && newCol<n && visit[newRow][newCol] == false) {
                if ((maps[row][col] - maps[newRow][newCol]) == 1 || (maps[row][col] - maps[newRow][newCol]) == -1) {
                    if (roomNumber > maps[newRow][newCol]){
                        roomNumber = maps[newRow][newCol];
                    }
                    dfs(newRow, newCol);
                }
            }
        }
    }
 
    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TestCase = Integer.parseInt(st.nextToken());
        for (int i = 0; i < TestCase; i++) {
            roomNumber=0;
 
            int maxValue=0;
            result=0;
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            maps = new int[n][n];
            visit = new boolean[n][n];
 
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int q = 0; q < n; q++) {
                    maps[j][q] = Integer.parseInt(st.nextToken());
                }
            }
            int roomResult=maps[0][0];
            for (int j = 0; j < n; j++) {
                for (int q = 0; q < n; q++) {
                    if (visit[j][q]==false){
                        roomNumber=maps[j][q];
                        result=0;
                        dfs(j,q);
                        if (result>maxValue){
                            roomResult = roomNumber;
                            maxValue=result;
                        }
                        else if (result==maxValue){
                            if (roomResult>roomNumber) {
                                roomResult = roomNumber;
                            }
                            maxValue=result;
                        }
                    }
                }
            }
            bw.write("#"+(i+1)+" "+roomResult+" "+ maxValue+"\n");
        }
 
        bw.flush();
    }
}
