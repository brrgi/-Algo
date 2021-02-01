import java.io.BufferedReader;
import java.io.InputStreamReader;
class Solution {
    public static void main(String args[]) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(in.readLine());
        for (int i = 0; i < a; i++) {
            char first = '0';
            int check = 0;
            String b = in.readLine();
            for (int j = 0; j < b.length(); j++) {
                if (b.charAt(j) != first) {
                    check++;
                    if (first == '0') first = '1';
                    else first = '0';
                }
            }
            System.out.format("#%d %d\n", i + 1, check);
        }
    }
}