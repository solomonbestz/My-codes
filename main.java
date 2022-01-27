import java.text.DecimalFormat;

class Main{
    private static final DecimalFormat df = new DecimalFormat("0.00");
    public static void main(String[] args) {
        double point_sum = 0;
        double unit_sum = 0;
        double first_sum = 0;
        double second_sum = 0;
        int[] grade_point = {2, 1, 2, 5, 3, 3, 4, 2, 5};
        int[] units = {3, 2, 1, 4, 3, 3, 4, 2, 2};
        double[] total_quality_point = new double[units.length];


        for(int i = 0; i < grade_point.length; i++){
            double quality_point = grade_point[i] * units[i];
            total_quality_point[i] = quality_point;
        }   

        for(int j = 0; j < total_quality_point.length; j++){
            point_sum = first_sum + total_quality_point[j];
            first_sum = point_sum;
            unit_sum = second_sum + units[j];
            second_sum = unit_sum;   
        }
        System.out.println("EMIABATA WASILAT");
        System.out.println("19/5498");
        System.out.println("YOUR CGPA IS " + df.format(point_sum / unit_sum));
    }
}