import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] maps;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int check=0;
        for (int i = 0; i < a; i++) {
            check=0;
            maps=new int[9][9];
            for (int j=0; j<9; j++){
                st = new StringTokenizer(br.readLine());
                for (int k=0; k<9; k++){
                    maps[j][k]=Integer.parseInt(st.nextToken());
                }
            }
            for (int j=0; j<9; j++){
                HashSet<Integer> set1 = new HashSet<Integer>();
                HashSet<Integer> set2 = new HashSet<Integer>();
                for (int q=0; q<9; q++){
                    set1.add(maps[j][q]);
                    set2.add(maps[q][j]);
                }

                if(set1.size()!=9 || set2.size()!=9) {
                    check=1;
                    break;
                }
            }
            if (check==1){
                System.out.println("#"+(i+1)+" "+0);
                continue;
            }
            for (int j=0; j<9; j=j+3){
                HashSet<Integer> set1 = new HashSet<Integer>();
                for (int q=0; q<9; q=q+3){
                    set1.clear();
                    set1.add(maps[j][q]);
                    set1.add(maps[j][q+1]);
                    set1.add(maps[j][q+2]);
                    set1.add(maps[j+1][q]);
                    set1.add(maps[j+1][q+1]);
                    set1.add(maps[j+1][q+2]);
                    set1.add(maps[j+2][q]);
                    set1.add(maps[j+2][q+1]);
                    set1.add(maps[j+2][q+2]);
                }

                if(set1.size()!=9) {
                    check=1;
                    break;
                }
            }
            if (check==1){
                System.out.println("#"+(i+1)+" "+0);
            }else{
                System.out.println("#"+(i+1)+" "+1);
            }

        }


    }
}
