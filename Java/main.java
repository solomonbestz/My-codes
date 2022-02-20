import java.text.DecimalFormat;
import java.util.Scanner;

class Main{
    // private static final DecimalFormat df = new DecimalFormat("0.00");
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        //Collecting User Input
        System.out.println("Enter GP for CSC301");
        int CSC301 = input.nextInt();
        System.out.println("Enter unit for CSC301");
        int csc301_unit = input.nextInt();
        System.out.println("Enter GP for CSC335");
        int CSC335 = input.nextInt();
        System.out.println("Enter unit for CSC335");
        int csc335_unit = input.nextInt();
        System.out.println("Enter GP for CSC311");
        int CSC311 = input.nextInt();
        System.out.println("Enter unit for CSC311");
        int csc311_unit = input.nextInt();
        //Calculation of CGPA
         int QP_CSC301 = CSC301 * csc301_unit;
        int QP_CSC335 = CSC335 * csc335_unit;
        int QP_CSC311 = CSC311 * csc311_unit;
        int total_QP = QP_CSC301 + QP_CSC311 + QP_CSC335;
        int total_unit = csc301_unit + csc311_unit + csc335_unit;
        float CGPA = total_QP/total_unit;
        //Printing CGPA
        System.out.println("Your CGPA is "+ CGPA);

    }
 }
    
    