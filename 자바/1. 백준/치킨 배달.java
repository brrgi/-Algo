import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static ArrayList<boolean[]> visit = new ArrayList<boolean[]>();

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<Integer[]> home = new ArrayList<Integer[]>();
        ArrayList<Integer[]> chiken = new ArrayList<Integer[]>();
        int[][] maps = new int[n][n];


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
                if (maps[i][j]==1){
                    home.add(new Integer[]{i,j});
                }else if(maps[i][j]==2){
                    chiken.add(new Integer[]{i,j});
                }
            }
        }

        boolean[] newVisit=new boolean[chiken.size()];
        combination(newVisit, 0, chiken.size(), m);

        int ans=10000;
        for (int i=0; i<visit.size(); i++){
            int tmp=0;
            for (int q=0; q<home.size(); q++){
                int minVal=10000;
                for (int j=0; j<visit.get(i).length; j++){
                    if (visit.get(i)[j]){
//                        System.out.println("home : "+home.get(q)[0]+" "+home.get(q)[1]);
//                        System.out.println("chieken : "+chiken.get(j)[0]+" "+chiken.get(j)[1]);
                        int distance=Math.abs(chiken.get(j)[0]-home.get(q)[0])+Math.abs(chiken.get(j)[1]-home.get(q)[1]);
//                        System.out.println(distance);
//                        System.out.println();
                        minVal=Math.min(minVal,distance);
                    }
                }
                tmp+=minVal;
            }
            ans=Math.min(ans,tmp);
        }

        System.out.println(ans);
    }

    //visited 0 n r
    static void combination(boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            boolean[] temp = new boolean[visited.length];
            for (int i=0; i<visited.length; i++){
                temp[i]=visited[i];
            }
            visit.add(temp);
            return;
        }

        for (int i = start; i < n; i++) {
            visited[i] = true;
            combination(visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }
}
