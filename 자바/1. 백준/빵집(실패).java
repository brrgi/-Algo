import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static char[][] maps;
    static int[][] binary;
    static int r;
    static int c;
    static int[][] dir = {{0,1},{1,1},{-1,1}};
    static boolean[][] visit;
    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        maps = new char[r][c];
        binary = new int[r][c];    //마지막 칸 안 봄

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            for (int j = 0; j < c; j++) {
                maps[i][j] = a.charAt(j);
            }
        }

        int compareValue = 0;
        for (int i = 0; i < r; i++) {
//          String bin = Integer.toBinaryString(1 << i);
            binary[i][0] = 1 << i;
            compareValue |= 1 << i;
//            int len = bin.length();
//            if (len < r) {
//                for (int j = 0; j < 5 - len; j++) {
//                    bin = "0" + bin;
//                }
//            }
//            System.out.println(bin);
        }

        visit = new boolean[r][c];
        for (int i = 0; i < r; i++) {
            visit[i][0] = true;
        }


        for (int i = 0; i < c - 2; i++) {
            for (int j = 0; j < r; j++) {
                if (visit[j][i] && maps[j][i] == '.') {
//                    System.out.println("보기 j i : "+j+" "i);
                    for (int[] direction : dir) {
                        if (0 <= j + direction[0] && j + direction[0] < r && 0 <= i + direction[1] && i + direction[1] < c) {
                            if (maps[j + direction[0]][i + direction[1]] == '.') {
//                                System.out.println("보기 nextj nexti : "+(j+direction[0])+" "());
                                binary[j + direction[0]][i + direction[1]] |= (binary[j][i]);
                                visit[j + direction[0]][i + direction[1]] = true;
                            }
                        }
                    }
                }
            }
        }

        int result1=0;
        int result2=0;
        int result3=0;
        for (int i=0; i<r; i++){
            if (binary[i][c-2]!=0){
                result1++;
                result2|=binary[i][c-2];
            }
        }
        String t = Integer.toBinaryString(result2);

        for (int i=0; i<t.length(); i++){
            if (t.charAt(i)=='1') result3++;
        }

        System.out.println(Math.min(result1, result3));
    }

}
