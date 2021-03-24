import java.io.*;
import java.util.*;

public class sdfk {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    static int[][] maps;
    static boolean[] visit;
    static int answer = 0;
    static int testcase;
    static int p;
    static int q;
    static int last;

    public static void main(String[] args) throws Exception {
        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            p = Integer.parseInt(st.nextToken());
            q = Integer.parseInt(st.nextToken());

            maps = new int[101][101];
            visit = new boolean[101];
            answer = q;
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < p/2; j++) {
                maps[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())]=1;
            }

            Queue<Integer> queue = new <Integer> LinkedList();
            queue.offer(q);

            while(!queue.isEmpty()){
                int checking=0;
                answer=-1;
                for (int w=0; w<queue.size(); w++){
                    int temp = queue.poll();
                    visit[temp] = true;

                    for(int j =1; j <= 100; j++){
                        if(maps[temp][j] == 1 && visit[j] == false){
                            checking=1;
                            queue.offer(j);
                            visit[j]=true;
                            if (j>answer) {
                                answer=j;
                            }
                            last=answer;
                        }
                    }
                    if (answer==-1){
                        answer=last;
                    }
                }
            }
            System.out.println("#" + (i + 1) + " " + last);
        }

    }
}
