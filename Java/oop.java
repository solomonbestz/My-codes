import java.util.Scanner;

class Animal{

    String make_sound(){
        return "Makes sound";
    }

    String walk(){
        return "Walking";
    }
}

class Dog extends Animal{

    void bark(){
        System.out.println("Wo Wo Wo Wo");
    }
}
public class oop{

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        
        input.close();

    }
}
