import java.io.*;
import java.util.*;


class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TestCase = Integer.parseInt(st.nextToken());
        for (int i = 0; i < TestCase; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            int first, second;
            if (n%2==0){
                first=n/2;
                second=n/2;
            }else{
                first=n/2+1;
                second=n/2;
            }
            String[] firstStr=new String[first];
            String[] secondStr = new String[second];
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<first; j++){
                firstStr[j]=st.nextToken();
            }
            for (int j=0; j<second; j++){
                secondStr[j]=st.nextToken();
            }

            String result="";
            if(first==second){
                for (int j=0; j<first; j++){
                    result=result.concat(firstStr[j]+" ");
                    result=result.concat(secondStr[j]+" ");
                }
            }else{
                for (int j=0; j<second; j++){
                    result=result.concat(firstStr[j]+" ");
                    result=result.concat(secondStr[j]+" ");
                }
                result=result.concat(firstStr[second]);
            }


            bw.write("#"+(i+1)+" "+result+"\n");
        }
        bw.flush();
    }
}
