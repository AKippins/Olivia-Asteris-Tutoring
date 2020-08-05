class HelloWorld {
    public static void main(String args[]){
        // This is a string. 
        var Name = "Hello Olivia";
        var Age = 16;
        var DifferentNumber = 0.0000000;

        String NameExplicit = "This is a string";
        Integer IntExplicit = 3;
        Boolean BooleanExplicit = true;

        if (BooleanExplicit){
            System.out.println("Why aren't you yelling at me?");
        }



        // Java wants to make effective use of storage. 
        // I wanna be more efficent than Python

        for (int i = 0; i <= 5; i++) {
            if (i % 2 == 1){
                System.out.println("Odd");
            } else if (i % 2 == 0) {
                System.out.println("Even");
            } else {
                System.out.println("Idk how we got here???");
            }
        }

    }
}