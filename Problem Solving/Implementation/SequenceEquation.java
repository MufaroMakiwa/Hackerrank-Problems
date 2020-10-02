import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;


public class Solution {

    // Complete the permutationEquation function below.
    static int[] permutationEquation(int[] p) {

        int[] values = new int[p.length];
        Map <Integer, Integer> val_ind = new HashMap<>();

        for (int i = 0; i < p.length; i++){
            val_ind.put(p[i], i+1);
        }
        
        for (int i = 1; i <= p.length; i++){
            int x = val_ind.get(i);
            int y = val_ind.get(x);
            values[i-1] = y;
        }
        return values;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] p = new int[n];

        String[] pItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int pItem = Integer.parseInt(pItems[i]);
            p[i] = pItem;
        }

        int[] result = permutationEquation(p);

        for (int i = 0; i < result.length; i++) {
            bufferedWriter.write(String.valueOf(result[i]));

            if (i != result.length - 1) {
                bufferedWriter.write("\n");
            }
        }

        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
