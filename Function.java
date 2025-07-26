public class Function {
      public static void main(String[] args){
            System.out.println("function executed successfully!");
            printArguments(args);
      }
      public static void printArguments(String[] args) {
            System.out.println("num of arguments: " + args.length);
            for (int i = 0; i < 10; i++) {
                  System.out.println("args[" + i + "]: "+args[i]);
            }
            
      }
}