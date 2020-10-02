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

    // Complete the happyLadybugs function below.
    static String happyLadybugs(String b) {

        Map <Character, ArrayList> counts = new HashMap<>();
        Boolean underscore = false;
        for (int i = 0; i < b.length(); i++) {
            Character letter = b.charAt(i);
            if (letter != '_') {
                if (!counts.containsKey(letter)){
                    counts.put(letter, new ArrayList<Integer>());
                }                 
                counts.get(letter).add(i);

            } else {
                underscore = true;
            }
        } 

        for (Map.Entry <Character , ArrayList> entry: counts.entrySet()) {
            ArrayList values = entry.getValue();

            if (values.size() == 1) {
                return "NO";
            } else {
                for (int i = 0; i < values.size() - 1; i++){
                    if ((int) values.get(i+1) != (int)values.get(i) + 1) {
                        if (underscore){
                            continue;
                        } else {
                            return "NO";
                        }
                    } 
                }
            } 
        }
        return "YES";


    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int g = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int gItr = 0; gItr < g; gItr++) {
            int n = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            String b = scanner.nextLine();

            String result = happyLadybugs(b);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}

