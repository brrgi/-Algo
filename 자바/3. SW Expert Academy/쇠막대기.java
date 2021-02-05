import java.io.*;
import java.util.*;


class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static String n;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TestCase = Integer.parseInt(st.nextToken());
        int cnt=0;
        for (int i = 0; i < TestCase; i++) {
            cnt=0;
            st = new StringTokenizer(br.readLine());
            n = st.nextToken();
            Stack<Character> stack=new Stack<Character>();
            int stackLength=0;
            for (int j=0; j<n.length(); j++){
                if (n.charAt(j)=='('){
                    if(n.charAt(j+1)=='('){
                        stack.push('(');
                        stackLength++;
                    }else{
                        cnt+=stackLength;
                    }
                }else{
                    if (!stack.empty() && n.charAt(j-1)==')'){
                        cnt++;
                        stack.pop();
                        stackLength--;
                    }
                }
            }
            bw.write("#"+(i+1)+" "+cnt+"\n");
        }
        bw.flush();
    }
}
