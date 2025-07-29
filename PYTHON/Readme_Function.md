In python without "main" function can run
what is  function
A function is a reusable block of code that performs a specific task. It allows you to encapsulate a set of instructions and execute them whenever needed. Functions can take input parameters, perform calculations or operations, and return a result. They help in organizing code, making it modular, and improving code readability and maintainability.
main 3 parts of function
<Return Type> <Function Name> <input arguments>
1. Return Type: The return type specifies the type of value that the function will return. It can be any valid data type such as int, float, char, void, etc.
2. Function Name: The function name is an identifier that uniquely identifies the function. It should be descriptive of the function's purpose.
3. Input Arguments: The input arguments are the values that are passed to the function when it is called. They allow the function to perform different tasks based on the input values. The input arguments are enclosed in parentheses and separated by commas if there are multiple arguments.

Example:
int get sum(int number 1, int number2)
{
    return number1 + number2;
}
int is return type, get sum is function name, number1 and number2 are input arguments
4. Function Body: The function body contains the code that is executed when the function is called.
 
void print(String message)
 void no return type, print  is function name, message is Input arguments

- Declaration : The declaration of a function provides the necessary information about the function, such as its name, return type, and input arguments. It is used to define the function's interface and make it available for use in other parts of the code.
- Definition : The definition of a function provides the actual code that is executed when the function is called
- Call or invocation : The call of a function is when the function is invoked or executed. It is don
by passing the required arguments to the function and using the function name followed by the parentheses containing the arguments
- Overloading : Function overloading is a feature of programming languages that allows multiple functions with the same name to be defined, but with different parameters. This allows a function to perform different tasks based

Example:
Declaration:
int getSum(int number 1, int number2); 
    ";" is used to declaration the function

Definition
    int getSum(int number 1, int number2){
        int sum = number1 + number2;
        return sum;     
    }
    "{" and "}" is used to definition the function
Call or invocation
    int result = getSum(5, 10);
    "result" is the variable that stores the return value of the function
    "getSum(5, 10)" is the call of the function, passing the arguments 5 and 10 to the function
    "int result" is the variable that stores the return value of the function 

