import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

class Main {

    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        int b;
        sc.nextLine();
        String[] arr = sc.nextLine().split(" ");
        for (int i=0; i<n; i++){
            a[i]=Integer.parseInt(arr[i]);
        }
        b=sc.nextInt();
        sc.nextLine();
        for (int i=0; i<b; i++){
            String[] arr2 = sc.nextLine().split(" ");
            int[] c=new int[2];
            for (int j=0; j<2; j++){
                c[j]=Integer.parseInt(arr2[j]);
            }
            if (c[0]==1){       //남학생
                for (int j=0; j<n; j++){
                    if ((j+1)%c[1]==0) {
                        if (a[j]==1) a[j]=0;
                        else a[j]=1;
                    }
                }
            }
            else{               //여학생
                int g=1;
                if (a[c[1]-1]==1) a[c[1]-1]=0;
                else a[c[1]-1]=1;
                while (true){
                    if ((c[1]-1-g)>=0&&(c[1]-1+g)<n){
                        if (a[(c[1]-1-g)]==a[c[1]-1+g]){
                            if (a[(c[1]-1-g)]==1) {
                                a[(c[1]-1-g)]=0;
                                a[(c[1]-1+g)]=0;
                            }else{
                                a[(c[1]-1-g)]=1;
                                a[(c[1]-1+g)]=1;
                            }
                        }else{
                            break;
                        }
                        g++;
                    }
                    else{
                        break;
                    }
                }
            }
        }
        for(int i=0; i<n; i++) {
            if(i!=0 && i%20==0) {
                System.out.println();
            }
            System.out.print(a[i]+" ");
        }
    }
}
