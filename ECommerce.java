// public class Function {
//       public static void main(String[] args){
//             System.out.println("function executed successfully!");
//             printArguments(args); // This line of code calls the printArguments method and passes the args parameter to it```java
//       }
//       public static void printArguments(String[] args) {
//             System.out.println("num of arguments: " + args.length);
//             for (int i = 0; i < 10; i++) {
//                   System.out.println("args[" + i + "]: "+args[i]);
//             }
            
//       }
// }
import java.util.*;

public class ECommerce {

    public static double calculateTotalAmount(List<Integer> cartItems, double taxRate) {
        int totalItem = 0;
        for (int item : cartItems) {
            totalItem += item;
        }
        double taxPrice = totalItem * taxRate;
        double totalAmount = totalItem + taxPrice;
        return totalAmount;
    }

    public static void main(String[] args) {
        List<Integer> cartItems = Arrays.asList(20, 30, 40, 564, 654, 74, 54, 54, 54, 64);
        double taxRate = 0.05;
        double total = calculateTotalAmount(cartItems, taxRate);
        System.out.println("Total amount after tax: " + total);
    }
}
