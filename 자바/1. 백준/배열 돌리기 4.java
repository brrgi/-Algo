import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] maps;
    static int n;
    static int m;
    static int r;
    static int floor;
    static int[][] op;
    static int[] visit;
    static int minV=100000;
    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());



        int[][] maps= new int[n][m];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++){
                maps[i][j]=Integer.parseInt(st.nextToken());
            }
        }


        op = new int[r][3];
        visit = new int[r];

        for (int i=0; i<r; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<3; j++){
                op[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        dfs(visit, 0, r, maps);
        System.out.println(minV);
    }
    public static void dfs(int[] visits, int check, int max, int[][] map){
        if (check==max){
            //최솟값 구하기
//            for (int x[] : map) {
//                for (int y : x) {
//                    System.out.print(y + " ");
//                }
//                System.out.println();
//            }
//            System.out.println();
            for (int[] x: map){
                int sum=0;
                for (int xx: x){
                    sum+=xx;
                }
                if (minV>sum){
                    minV=sum;
                }
//                System.out.println(sum);

            }
            return;
        }

        for (int i=0; i<max; i++) {
            if (visits[i] == 0) {
                int[][] copy = arrayCopy(map);
                visits[i] = 1;
                floor = op[i][2];
                for (int j = 0; j < floor; j++) {
                    int up = op[i][0] - op[i][2] - 1+j;
                    int down = op[i][0] + op[i][2] - 1-j;
                    int right = op[i][1] + op[i][2] - 1-j;
                    int left = op[i][1] - op[i][2] - 1+j;
                    int temp = copy[up][left];
//                    System.out.println("위,왼쪽  아래,오른쪽"+up+" "+left+" "+down+" "+right);
                    //왼쪽 아래 ->왼쪽 위
                    for (int k = up; k < down; k++) {            // 오른쪽 아래 -> 오른쪽 위
                        copy[k][left] = copy[k + 1][left];
//                        System.out.println("3 : "+k+" "+left);
                    }
                    //오른쪽 아래 -> 왼쪽 아래
                    for (int k = left; k < right; k++) {         //오른쪽 위->왼쪽 위
                        copy[down][k] = copy[down][k + 1];
//                        System.out.println("2: "+down+" "+k);
                    }
                    //오른쪽 위 -> 오른쪽 아래
                    for (int k = down; k > up; k--) {
                        copy[k][right] = copy[k - 1][right];    //왼쪽 위 -> 왼쪽 아래
//                        System.out.println("1: "+k+" "+right);
                    }
                    //왼쪽 위 -> 오른쪽 위
                    for (int k = right; k > left; k--) {
                        copy[up][k] = copy[up][k - 1];    //왼쪽 아래 -> 오른쪽 아래
//                        System.out.println("4 : "+up+" "+k);
                    }
                    copy[up][left + 1] = temp;


                }
                dfs(visits, check + 1, max, copy);

                visits[i] = 0;
            }
        }
    }

    static int[][] arrayCopy(int[][] arr){
        int[][] ret = new int[arr.length][];

        for(int i = 0; i < arr.length; i++){
            ret[i] = arr[i].clone();
        }
        return ret;
    }
}
