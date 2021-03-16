import java.io.*;
import java.util.*;

public class sdfk {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static char[] a = {'a', 'e', 'i', 'o', 'u'};
    static int l;
    static int c;

    public static void main(String[] args) throws Exception {

        StringTokenizer st = new StringTokenizer(br.readLine());
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        List<String> b = new ArrayList<>();
        boolean[] visit = new boolean[c];
        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < c; j++) {
            b.add(st.nextToken());
        }
        Collections.sort(b);

        combination(b, visit, 0, c, l);


    }
    static void combination(List<String> arr, boolean[] visited, int start, int n, int r) {
        if(r == 0) {
            int count=0;
            for (int i=0; i<c; i++){
                if (visited[i]){
                    for (char x : a){
                        if (x==arr.get(i).charAt(0)){
                            count++;
                            break;
                        }
                    }
                }
            }

            if (count>=1 && count<=l-2){
                String s = "";
                for (int i=0; i<c; i++){
                    if (visited[i]){
                        s=s.concat(arr.get(i));
                    }
                }
                System.out.println(s);
            }
        }

        for(int i=start; i<n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }
}
