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
        System.out.println(Name);
    }
}