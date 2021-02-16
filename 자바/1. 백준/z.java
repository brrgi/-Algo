import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());       //
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        //3, 7, 7, 2^3=8, 0
        System.out.println(calculate(n,r,c, (int)Math.pow(2, n),0));
    }

    static int calculate(int n, int row, int col, int s, int result){
        if(row<2 && col<2){
            result+=(row*2+col);        //1*2 + 1 = 3
            return result;
        }

        s/=2;           //  4 -> 2
        int i=(row/s);    //  7/4 = 1 -> 3/2 = 1
        int j=(col/s);    //  7/4 = 1 -> 3/2 = 1
        System.out.println(i+" "+j);
        result+=(i*2+j)*((int)Math.pow(s, 2));  //48 -> 12
        System.out.println(result);
        row-=i*s;         
        col-=j*s;
        return calculate(n,row,col,s,result);
    }
}
