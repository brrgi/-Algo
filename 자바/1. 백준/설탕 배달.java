import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int count = 0;

        while (a > 0) {
            count++;
            if (a % 5 == 0) {
                a = a - 5;
            } else {
                a = a - 3;
            }
        }

        if (a < 0) {
            System.out.println(-1);
        } else {
            System.out.println(count);
        }
    }
}
