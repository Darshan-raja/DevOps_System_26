public class Function {
      public static void main(String[] args){
            System.out.println("function executed successfully!");
            printArguments(args); // This line of code calls the printArguments method and passes the args parameter to it```java
      }
      public static void printArguments(String[] args) {
            System.out.println("num of arguments: " + args.length);
            for (int i = 0; i < 10; i++) {
                  System.out.println("args[" + i + "]: "+args[i]);
            }
            
      }
}