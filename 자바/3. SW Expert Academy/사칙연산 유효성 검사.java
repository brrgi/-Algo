import java.io.*;
import java.util.*;


public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String args[]) throws Exception {
        for (int j = 0; j < 10; j++) {
            int check=0;
            int check1=0;
            int check2=0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int floor=1;
            int temp=n;
            while (temp>1){
                temp=temp/2;
                floor++;
            }
            int leaf;
            leaf=(n-(int)Math.pow(2, floor-1)+1)+((int)Math.pow(2, floor-2))-(n-(int)Math.pow(2, floor-1)+1)/2;
            if (n%2==0){
                check=1;
            }
            for (int i=0; i<n-leaf; i++){
                st = new StringTokenizer(br.readLine());
                st.nextToken();
                String h = st.nextToken();
                if (h.equals("+")){
                    continue;
                }else if(h.equals("-")){
                    continue;
                }else if(h.equals("*")){
                    continue;
                }else if(h.equals("/")){
                    continue;
                }else{
                    check1=1;
                }
            }
            for (int i=n-leaf; i<n; i++){
                st = new StringTokenizer(br.readLine());
                st.nextToken();
                String h =st.nextToken();
                if (h.equals("+")){
                    check2=1;
                }else if(h.equals("-")){
                    check2=1;
                }else if(h.equals("*")){
                    check2=1;
                }else if(h.equals("/")){
                    check2=1;
                }else{
                    continue;
                }
            }
            if (check==0 && check1==0 && check2 ==0){
                bw.write("#" + (j + 1) + " " + 1 + "\n");
            }else{
                bw.write("#" + (j + 1) + " " + 0 + "\n");
            }

        }
        bw.flush();
    }
}
