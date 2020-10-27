import java.util.ArrayList;
import java.util.LinkedList;

public class App {
    public static void main(String[] args) throws Exception {
        // Remember data types for the variables
        int example = 0;

        // Our new friend ++ adds one to the variable
        // Our new friend -- subtracts one to the variable
        int plusplus = example++;

        // Stupid Fixed Length Arrays - Can't change the length once you make it. 
        int[] exampleArray = {4, 5, 6, 7};
        String[] stringArray = new String[4];
        boolean[] booleanArray = new boolean[5];

        // Better but still annoying arrays. More python like but way too many words to make them. 

        // List with pointers (Will explain pointers later)
        LinkedList Soda = new LinkedList<String>();
        
        // List without pointers (Will explain pointers later)
        ArrayList Candy = new ArrayList<String>();

        // Soda.push("Coca Cola");
        // Soda.add("Sprite");
        // System.out.println(Soda);

        // Candy.add("Twix");
        // System.out.println(Candy);
        
        // // For Loops - For In
        // for (int number:exampleArray) {
        //     System.out.println(number);
        // }
        
        // // For Loops - Iterating
        // for (int index = 0; index < 10; index++) {
        //     System.out.println(index);
        // }

        // // While Loops
        // while (example != 10) {
        //     System.out.println("Fudge");
        // }

        // Start Here
        // We run nextInt()
        // 42\n
        // 3.1415\n
        // Whatever\n
        
        // Next int processing
        // Capturing (42)\n
        // 3.1415\n
        // Whatever\n
        // Put int the variable i
        
        // Next double processing
        // Captured by i (42) (Next double starts here) \n (Not a double so I skip)
        // Capturing (3.1415) \n
        // Whatever\n
        // Put int the variable i
        // Put double the variable d
        
        // Next Line processing
        // Captured by i (42) (Next double starts here) \n (Not a double so I skip)
        // Capturing (3.1415) (Next Line starts here) Capturing (\n)
        // Whatever\n
        // Put int the variable i
        // Put double the variable d
        // Put line the variable s


        // 42\n
        // 3.1415\n
        // Whatever\n


        String name = "Liv";
        String location = "Existence";

        int number = 20;

        System.out.printf("%s is %0dnt the smartest person in the %s", name, number, location);
    }
}
