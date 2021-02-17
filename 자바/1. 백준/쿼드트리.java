import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<boolean[]> visit = new ArrayList<boolean[]>();
    static char[][] maps;
    static int n;
    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        maps = new char[n][n];
        for (int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            for (int j=0; j<n; j++){
                maps[i][j]=a.charAt(j);
            }
        }

        dc(0,0,n,n);
    }

    static void dc(int x, int y, int a, int b){
        if(x==a && y==b){
            System.out.print(maps[x][y]);
            return ;
        }

        for (int i=x; i<a; i++){
            for (int j=y; j<b; j++){
                if (maps[i][j]!=maps[x][y]){
                    System.out.print("(");
                    dc(x, y, (x + a) / 2, (y + b) / 2);
                    dc(x, (y + b) / 2, (x + a) / 2, b);
                    dc((x + a) / 2, y, a, (y + b) / 2);
                    dc((x + a) / 2, (y + b) / 2, a, b);
                    System.out.print(")");
                    return ;
                }
            }
        }
        System.out.print(maps[x][y]);
    }

}
