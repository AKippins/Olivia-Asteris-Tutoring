import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        // Bit representation. Can either be 0 or 1. Otherwise known as true or false.
        boolean is_smart = true;
        // 0000 0000
        // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]  Hexiecimal is Base 16
        // Hundreds Tens Ones
        //    0      1    0
        // 
        // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  Decimal is Base 10
        //  10^2    10^1   10^0
        //   800  +  90  +  6    = 896
        // Hundreds Tens   Ones
        //    8      9      6
        // [0, 1, 2, 3, 4, 5, 6, 7]  Octal is Base 8
        // Hundreds Tens Ones
        //    0      1    0
        // [0, 1] Binary is Base 2
        //   2^3    2^2   2^1   2^0
        //    8  +   0  +  2  +  1  = 11
        // Eighths Fours  Twos  Ones
        //    1      0     1     1
        // 0111 1111 = 127 This holds 128 positions
        // 1111 1111 = -128 
        // 1000 0000 = 128, This is 128 in binary
        // Byte representation. Is 8 bits all together. Is a number type. Byte can hold from -128 - 127
        byte example_byte = 127;
        // 0111 1111 1111 1111 = 32,767 This holds 32,768 positions
        // 1111 1111 1111 1111 = -32,768 
        // 1000 0000 1000 0000 = 65,536, This is 65,536 in binary
        // Short representation. Is 16 bits all together. Is a number type. Short can hold from -32,768 - 32,767
        short age_as_short = 32767;
        // 0111 1111 1111 1111 1111 1111 1111 1111 = 2,147,483,647 This holds 2,147,483,648 positions
        // 1111 1111 1111 1111 1111 1111 1111 1111 = -2,147,483,648 
        // 1000 0000 0000 0000 0000 0000 0000 0000 = 4,294,967,296, This is 4,294,967,296 in binary
        // Int representation. Is 32 bits all together. Is a number type. Int can hold from -2,147,483,648 - 2,147,483,647
        int age = 2147483647;
        // 0111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 = 9.223372036854775e18 This holds x positions
        // 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 = -9.223372036854776e18 
        // 1000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 = 1.844674407370955e19, This is 1.844674407370955e19 in binary
        // Long representation. Is 64 bits all together. Is a number type. Long can hold from -2,147,483,648 - 2,147,483,647
        long age_as_long = 16;
        float gpa = 0.0f;
        double gpa_as_long = 3.9;
        char letter = 'c';

        // <DataType> VariableName = The Thing;


        
        
        Scanner exampleScanner = new Scanner(System.in);
        Scanner exampleScanner = new Scanner(System.in);
        
        System.out.print("Hello there! What's your name?: ");
        String users_name = exampleScanner.nextLine();
        System.out.println("Hello, " + users_name + "!");

        
        System.out.println(exampleScanner);
    }
}
