import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static int k;
    public static int w, h;
    public static int[][] maps;
    public static int dx[] = {1, -1, 0, 0};
    public static int dy[] = {0, 0, -1, 1};
    public static int d1[] = {-2, -1, 1, 2, 2, 1, -1, -2};
    public static int d2[] = {1, 2, 2, 1, -1, -2, -2, -1};
    public static Queue<Node> queue = new LinkedList<>();

    static class Node {
        int row;
        int col;
        int z;

        Node(int a, int b, int c) {
            this.row = a;
            this.col = b;
            this.z = c;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        k=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        init(br, st);

        int[][][] visit = new int[h][w][31];
        int check=0;
        Node first = new Node(0,0,k);
        queue.add(first);
        while (!queue.isEmpty()){
            Node temp = queue.poll();
            int x=temp.row;
            int y=temp.col;
            int z=temp.z;

            if (x==h-1 && y==w-1){
                System.out.println(visit[x][y][z]);
                check++;
                break;
            }

            for (int i=0; i<4; i++){
                int newRow=x+dx[i];
                int newCol=y+dy[i];
                if ( 0 <= newRow && newRow < h && 0 <= newCol && newCol< w && maps[newRow][newCol] != 1 && visit[newRow][newCol][z] == 0){
                    visit[newRow][newCol][z] = visit[x][y][z] + 1;
                    queue.add(new Node(newRow, newCol, z));
                }
            }
            if (z>0){
                for (int i=0; i<8; i++){
                    int newRow=x+d1[i];
                    int newCol=y+d2[i];
                    if ( 0 <= newRow && newRow < h && 0 <= newCol && newCol< w && maps[newRow][newCol] != 1 && visit[newRow][newCol][z-1] == 0){
                        visit[newRow][newCol][z-1] = visit[x][y][z] + 1;
                        queue.add(new Node(newRow, newCol, z-1));
                    }
                }
            }
        }
        if (check==0){
            System.out.println(-1);
        }

    }

    private static void init(BufferedReader br, StringTokenizer st) throws IOException {
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());
        maps = new int[h][w];
        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}
