import java.io.*;
import java.util.*;



public class jngcfd {
    static class Pair {
        int x;
        int y;

        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[][] maps;
    static int test;
    static int n;
    static int result = 100000;
    static Pair company;
    static Pair home;
    static Pair[] location;
    static int[] arr;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());

        test = Integer.parseInt(st.nextToken());
        for (int q=0; q<test; q++){
            result=100000;
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());

            arr=new int[n];
            maps = new int[100][100];
            location = new Pair[n];
            st = new StringTokenizer(br.readLine());
            company=(new Pair(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            home=(new Pair(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            for (int i=0; i<n; i++){
                arr[i]=i;
                location[i]=(new Pair(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            }

            permutation(arr, 0, n, n);
            System.out.println("#"+(q+1)+" "+result);
        }
    }

    static void permutation(int[] arr, int depth, int n, int r) {
        if (depth == r) {
            int temp=0;
            int x=company.x;
            int y=company.y;

            for (int a: arr){
                temp+=Math.abs(x-location[a].x)+Math.abs(y-location[a].y);
                x=location[a].x;
                y=location[a].y;
            }
            temp+=Math.abs(x-home.x)+Math.abs(y-home.y);
            if (result>temp){
                result=temp;
            }
            return;
        }

        for (int i=depth; i<n; i++) {
            swap(arr, depth, i);
            permutation(arr, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }
}
