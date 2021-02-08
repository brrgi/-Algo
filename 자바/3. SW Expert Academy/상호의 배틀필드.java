import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

class Solution {
    static String[] see = {">", "v", "<", "^"};     //오른쪽, 아래, 왼쪼끄, 위
    static int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    public static String[][] maps;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int dirIndex = 0;
    static int row;
    static int col;
    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TestCase = Integer.parseInt(st.nextToken());
        for (int i = 0; i < TestCase; i++) {
            st = new StringTokenizer(br.readLine());
            row = Integer.parseInt(st.nextToken());
            col = Integer.parseInt(st.nextToken());
            maps = new String[row][col];
            int[] start = new int[2];
            dirIndex = 0;

            for (int j = 0; j < row; j++) {
                st = new StringTokenizer(br.readLine());
                String str = st.nextToken();
                for (int k = 0; k < col; k++) {
                    maps[j][k] = Character.toString(str.charAt(k));
                    for (int q = 0; q < 4; q++) {
                        if (see[q].equals(maps[j][k])) {
                            start[0] = j;
                            start[1] = k;
                            dirIndex = q;
                        }
                    }
                }
            }

            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            moveTank(start, n, command);
            System.out.format("#%d ", i + 1);
            for (String[] t : maps) {
                for (String tt : t) {
                    System.out.print(tt);
                }
                System.out.println();
            }
        }
    }

    public static void moveTank(int[] start, int n, String comm) {//오른쪽, 아래, 왼쪼끄, 위 0 1 2 3
        int nowRow=start[0];
        int nowCol=start[1];
        for (int i = 0; i < n; i++) {
            if (Character.toString(comm.charAt(i)).equals("U")) {       //위
                dirIndex=3;
                maps[nowRow][nowCol]="^";
                int nextRow=nowRow+dir[dirIndex][0];
                int nextCol=nowCol+dir[dirIndex][1];
                if (0<=nextRow && nextRow<row && 0<=nextCol && nextCol<col && maps[nextRow][nextCol].equals(".")){
                    maps[nowRow][nowCol]=".";
                    nowRow=nextRow;
                    nowCol=nextCol;
                    maps[nowRow][nowCol]="^";
                }
            } else if (Character.toString(comm.charAt(i)).equals("D")) {//아래
                dirIndex=1;
                maps[nowRow][nowCol]="v";
                int nextRow=nowRow+dir[dirIndex][0];
                int nextCol=nowCol+dir[dirIndex][1];
                if (0<=nextRow && nextRow<row && 0<=nextCol && nextCol<col && maps[nextRow][nextCol].equals(".")){
                    maps[nowRow][nowCol]=".";
                    nowRow=nextRow;
                    nowCol=nextCol;
                    maps[nowRow][nowCol]="v";
                }
            } else if (Character.toString(comm.charAt(i)).equals("L")) {//왼
                dirIndex=2;
                maps[nowRow][nowCol]="<";
                int nextRow=nowRow+dir[dirIndex][0];
                int nextCol=nowCol+dir[dirIndex][1];
                if (0<=nextRow && nextRow<row && 0<=nextCol && nextCol<col && maps[nextRow][nextCol].equals(".")){
                    maps[nowRow][nowCol]=".";
                    nowRow=nextRow;
                    nowCol=nextCol;
                    maps[nowRow][nowCol]="<";
                }
            } else if (Character.toString(comm.charAt(i)).equals("R")) {//오
                dirIndex=0;
                maps[nowRow][nowCol]=">";
                int nextRow=nowRow+dir[dirIndex][0];
                int nextCol=nowCol+dir[dirIndex][1];
                if (0<=nextRow && nextRow<row && 0<=nextCol && nextCol<col && maps[nextRow][nextCol].equals(".")){
                    maps[nowRow][nowCol]=".";
                    nowRow=nextRow;
                    nowCol=nextCol;
                    maps[nowRow][nowCol]=">";
                }
            } else {      //S
                int nextRow=nowRow+dir[dirIndex][0];
                int nextCol=nowCol+dir[dirIndex][1];
                while (0<=nextRow && nextRow<row && 0<=nextCol && nextCol<col){
                    if (maps[nextRow][nextCol].equals("#")){
                        break;
                    }else if (maps[nextRow][nextCol].equals("*")){
                        maps[nextRow][nextCol]=".";
                        break;
                    }
                    nextRow=nextRow+dir[dirIndex][0];
                    nextCol=nextCol+dir[dirIndex][1];
                }
            }
        }
    }
}


//1
//4 6
//*.*..*
//*.....
//..-...
//^.*#..
//10
//SRSSRRUSSR
