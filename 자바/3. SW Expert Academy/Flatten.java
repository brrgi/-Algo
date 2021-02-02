import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.io.FileInputStream;


class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 10; i++) {
            int T;
            T = sc.nextInt();
            List<Integer> list = new ArrayList<Integer>();

            for (int j = 0; j < 100; j++) {
                int w = sc.nextInt();
                list.add(j, w);
            }
            for (int test_case = 0; test_case < T; test_case++) {
                int max = Collections.max(list);
                int min = Collections.min(list);
                int maxIndex = list.indexOf(max);
                int minIndex = list.indexOf(min);
                if (min == max) {
                    break;
                } else {
                    list.set(maxIndex, max - 1);
                    list.set(minIndex, min + 1);
                }
            }
            int max = Collections.max(list);
            int min = Collections.min(list);
            System.out.format("#%d %d\n", i+1, max-min);
        }

    }
}


//solution 2
/*
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.io.FileInputStream;


class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 10; i++) {
            int T;
            T = sc.nextInt();
            int[] list = new int[100];
            for (int j = 0; j < 100; j++) {
                int w = sc.nextInt();
                list[j] = w;
            }
            for (int test_case = 0; test_case < T; test_case++) {
                int max = -1;
                int min = 101;
                int maxIndex = 0;
                int minIndex = 0;
                for (int j = 0; j < 100; j++) {
                    if (list[j] >= max) {
                        max = list[j];
                        maxIndex = j;
                    }
                    if (list[j] <= min) {
                        min = list[j];
                        minIndex = j;
                    }
                }
//                System.out.println("보자  : "+max+" "+min+" ");
                if (min == max) {
                    break;
                } else {
                    list[minIndex] = min + 1;
                    list[maxIndex] = max - 1;
                }
            }
            int max = -1;
            int min = 101;
            for (int j = 0; j < 100; j++) {
                if (list[j] > max) {
                    max = list[j];
                }
                if (list[j] < min) {
                    min = list[j];
                }
            }
            System.out.format("#%d %d\n", i + 1, max - min);
        }

    }
}
*/
