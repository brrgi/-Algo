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
        int d = Integer.parseInt(st.nextToken());
        int result=-1;
        ArrayList<Integer[]> enem = new ArrayList<Integer[]>();
        int[] combs = new int[m];
        int[][] maps = new int[n][n];
        for (int i = 0; i < m; i++) {
            combs[i]=i;
        }
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
                if (maps[i][j]==1){
                    enem.add(new Integer[]{i,j});
                }
            }
        }

        boolean[] newVisit=new boolean[m];
        combination(newVisit, 0, m, 3);

        for (boolean[] comb : visit){
//            for (boolean f : comb) {
//                System.out.print(f+" ");
//            }
//            System.out.println();
            int how=0;
            ArrayList<Integer[]> enemy = new ArrayList<Integer[]>();
            for (int i=0; i<enem.size();i++){
                enemy.add(enem.get(i));
            }
//            for (Integer[] f : enemy) {
//                System.out.print("["+f[0]+", "+f[1]+"] ");
//            }
//            System.out.println();
            while (!enemy.isEmpty()){

                ArrayList<Integer[]> remov = new ArrayList<Integer[]>();
                for (int i=0; i<m; i++){
                    if (comb[i]){
                        int row=n;
                        int col=combs[i];

                        int[] target = {-1,-1};
                        int distance =33;
                        int left =16;
                        for (Integer[] j : enemy){
                            int nowDist=Math.abs(row-j[0])+Math.abs(col-j[1]);
                            if (d>=nowDist){
                                if (nowDist<distance){
                                    distance=nowDist;
                                    target[0]=j[0];
                                    target[1]=j[1];
                                    left=j[1];
                                }else if(nowDist == distance){
                                    if (j[1]<left){
                                        target[0]=j[0];
                                        target[1]=j[1];
                                        left=j[1];
                                    }
                                }
                            }
                        }
                        int toggle=0;
                        if (!(target[0]==-1 || target[1]==-1)){
                            for (int q=0; q<remov.size();q++){
                                if (remov.get(q)[0]==target[0] && remov.get(q)[1]==target[1]){
                                    toggle=1;
                                    break;
                                }
                            }
                            if(toggle==0){
                                Integer[] temps = new Integer[2];
                                temps[0]=target[0];
                                temps[1]=target[1];
                                remov.add(temps);
                            }
                        }
                    }
                }

                for (int e=0; e<remov.size();e++){
                    Iterator<Integer[]>itr=enemy.iterator();
                    while(itr.hasNext()){
                        Integer[] temps = itr.next();
                        if(temps[0]==remov.get(e)[0] && temps[1]==remov.get(e)[1]){
                            itr.remove();
                            how++;
                            break;
                        }
                    }
                }
//                System.out.println("enemysize : "+enemy.size());
                ArrayList<Integer[]> delete = new ArrayList<Integer[]>();
                for (int e=0; e<enemy.size();e++){
                    Integer[] temps = new Integer[2];
                    temps[0]=enemy.get(e)[0]+1;
                    temps[1]=enemy.get(e)[1];
                    if (temps[0]==n) delete.add(temps);
                    enemy.set(e, temps);
                }

                for (int e=0; e<delete.size();e++){
                    Iterator<Integer[]>itr=enemy.iterator();
                    while(itr.hasNext()){
                        Integer[] temps = itr.next();
                        if(temps[0]==n){
                            itr.remove();
                            break;
                        }
                    }
                }
//                System.out.println("enemysize : "+enemy.size());
//                for (Integer[] f : enemy) {
//                    System.out.print("["+f[0]+", "+f[1]+"] ");
//                }
//                System.out.println(how);
//                System.out.println();
            }
//            System.out.println();
            if (result<how){
                result=how;
            }
//            System.out.println(enemy);
        }

        System.out.println(result);
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
