import java.util.Scanner;

class Variable{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        

        char op;
        double num1, num2, answer;

        System.out.println("Choose An operator \n1)+  2)-\n3)*  4)/");
        op = input.next().charAt(0);

        System.out.println("Enter FirstNumber: ");
        num1 = input.nextInt();

        System.out.println("Enter SecondNumber: ");
        num2 = input.nextInt();
        
        if(op == '+'){
            answer = num1 + num2;
            System.out.println(num1 + " + " + num2 + " = " + answer );
        }else if(op == '-'){
            answer = num1 - num2;
            System.out.println(num1 + " - " + num2 + " = " + answer );
        }else if(op == '*'){
            answer = num1 * num2;
            System.out.println(num1 + " * " + num2 + " = " + answer );
        }else if(op == '/'){
            answer = num1 / num2;
            System.out.println(num1 + " / " + num2 + " = " + answer );
        }else{
            System.out.println(op + " not accepted.");
        }
        input.close();  
    }
}
