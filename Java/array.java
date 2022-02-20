import java.util.Scanner;
import java.text.DecimalFormat;

class array {
    private static final DecimalFormat df = new DecimalFormat("0.00");
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        float qp_sum = 0;
        float unit_sum = 0;
        float[] unit_arr = new float[3];
        float[] grade_point = new float[3];
        float[] qaulity_point = new float[unit_arr.length];

        for(int i = 0; i < unit_arr.length; i++){
            System.out.println("Enter unit: ");
            int user_input = input.nextInt();
            unit_arr[i] = user_input;

            System.out.println("Enter grade point: ");
            user_input = input.nextInt();
            grade_point[i] = user_input;
        }
        
        for(int i = 0; i < unit_arr.length; i++){
            qaulity_point[i] = unit_arr[i] * grade_point[i];
        }

        for(int j = 0; j < unit_arr.length; j++){
            qp_sum = qp_sum + qaulity_point[j];
            unit_sum = unit_sum + unit_arr[j];
        }
        float cgpa = qp_sum / unit_sum;
        System.out.println("Your Cgpa is: " + df.format(cgpa));

        input.close();
    }
}
