import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static char[][] maps;
    static boolean[] check = new boolean[26];
    static int answer=0;
    static int[][] dir ={{-1,0},{1,0},{0,-1},{0,1}};
    static int testcase;
    static int p;
    static int q;
    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        testcase= Integer.parseInt(st.nextToken());
        for (int i=0; i<testcase; i++){
            st = new StringTokenizer(br.readLine());
            p= Integer.parseInt(st.nextToken());
            q= Integer.parseInt(st.nextToken());

            int start=1;
            int result=1;

            int pVal=1;
            int qVal=1;
            int[] line={1,1};
            int[] line2={1,1};
            while (true){
                if (pVal<p){
                    pVal+=start;
                    start++;
                    line[0]+=1;
                }else if(pVal==p){
                    break;
                }else{
                    start--;
                    pVal-=start;
                    line[0]-=1;
                    while(true){
                        if (pVal==p){
                            break;
                        }
                        line[0]-=1;
                        line[1]+=1;
                        pVal++;
                    }
                    break;
                }
            }
            start=1;
            while (true){
                if (qVal<q){
//                    System.out.println("qkf"+qVal+" ");
//                    System.out.println(line2[0]+" "+line2[1]);
                    qVal+=start;
                    start++;
                    line2[0]+=1;
                }else if(qVal==q){

                    break;
                }else{

                    start--;
                    qVal-=start;
                    line2[0]-=1;
                    while(true){
//                        System.out.println("Qhwk"+qVal+" ");
//                        System.out.println(line2[0]+" "+line2[1]);
                        if (qVal==q){
                            break;
                        }
                        line2[0]-=1;
                        line2[1]+=1;
                        qVal++;
                    }
                    break;
                }
            }
            int[] line3={line[0]+line2[0],line[1]+line2[1]};
            int k = line3[0]+line3[1];

            start=1;
            int[] line4={1,1};
            while (true){
                if ((line4[0]+line4[1])==k){
                    result+=line4[0]-line3[0];
                    break;
                }else{
                    line4[0]+=1;
                    result+=start;
                    start++;
                }
            }
            System.out.println("#"+(i+1)+" "+result);
        }



    }

}
