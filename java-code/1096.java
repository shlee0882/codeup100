import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String cnt = sc.nextLine();
        List<List> list1 = new ArrayList();
        for(int i=0; i<Integer.valueOf(cnt); i++){
            String val = sc.nextLine();
            list1.add(Arrays.asList(val.split(" ")));
        }

        List<List> pan1 = new ArrayList();
        List<Integer> pan2 = new ArrayList();

        for(int i=0; i<19; i++){
            for(int j=0; j<19; j++){
                pan2.add(0);
            }
            pan1.add(pan2);
            pan2 = new ArrayList();
        }

        System.out.println(pan1);

        for(int i=0; i < list1.size(); i++){
            List<String> data1 = list1.get(i);
            String first = data1.get(0);
            String second = data1.get(1);
            System.out.println("첫째값 : "+first);
            System.out.println("둘째값 : "+second);

            List<Integer> garo = pan1.get(Integer.valueOf(first));
            int findVal = garo.get(Integer.valueOf(second));
            
            System.out.println("가로값 : "+first);
            System.out.println("찾은값 : "+second);
            
            garo.set(Integer.valueOf(second), findVal);
        }

        System.out.println(pan1);
    }
}
