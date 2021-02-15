import java.io.*;
import java.util.*;


public class jngcfd {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int win;
    static int lose;
    static int[] firstCard;

    public static void main(String args[]) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int TestCase = Integer.parseInt(st.nextToken());

        for (int q = 0; q < TestCase; q++) {
            int[] all = new int[18];
            win = 0;
            lose = 0;
            firstCard = new int[9];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < 9; i++) {
                int a = Integer.parseInt(st.nextToken());
                firstCard[i] = a;
                all[a - 1] = 1;
            }

            dfs(all, 0, 0, 0);

            bw.write("#" + (q + 1) + " " + win + " " + lose+"\n");
        }
        bw.flush();
    }

    static void dfs(int[] all, int check, int first, int second) {
        if (check == 9) {
            if (first > second) {
                win++;
            } else if (first < second) {
                lose++;
            }
            return;
        }

        for (int i = 0; i < 18; i++) {
            if (all[i] == 0) {
                if (firstCard[check] > i + 1) {
                    all[i] = 1;
                    dfs(all, check + 1, first + firstCard[check] + i + 1, second);
                    all[i] = 0;
                } else if (firstCard[check] < i + 1) {
                    all[i] = 1;
                    dfs(all, check + 1, first, second + firstCard[check] + i + 1);
                    all[i] = 0;
                } else {
                    all[i] = 1;
                    dfs(all, check + 1, first, second);
                    all[i] = 0;
                }
            }
        }
    }

}
