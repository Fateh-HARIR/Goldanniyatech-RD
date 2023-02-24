/**************************************************
 *         Java Pocket Card 01 The Basics         *
 *                                                *
 *                Yoann AMAR ASSOULINE            *
 *                                                *
 **************************************************/

import java.io.*;

public class Main {

    // Variables: Primitive Data Types
    boolean boolean_one = true; // Only two states: true | false
    byte byte_one = 127; // Storing numbers from -128 to 127
    int int_one = 35; // Storing large number up to 2,147 billion
    long long_one = 4587; // Storing very large number up to 9 quintillion
    float float_one = 603.35f; // Storing fractional numbers for 6/7 decimal digits
    double double_one = 305.304576f; // Storing fractional numbers for 15 decimal digits
    char character_one = 'F';

    // Variables: Non-Primitive Data Types
    String string_one = "Hi there!";
    String[] string_array =  {"array element 1", "Array Element 2", "Array Element 3"};

    // Type Conversion/ Widening Conversion (converting smaller type to larger type)
    double old_int = int_one;

    String old_float = Float.toString(float_one);

    // Type Casting/ Narrowing Casting (converting large type to smaller type)
    int old_float_int = (int) float_one;

    public static void main(String[] args) {

        System.out.println("Hello world!");

        // Create a new object from Main
        Main Main_Instance_One = new Main();
        System.out.println(Main_Instance_One.double_one);

        // Creating another object from Basics
        Basics Basics_Instance_One = new Basics();
        Basics_Instance_One.Basics_Method_One();
        int result = Basics_Instance_One.CheckNumber(4);
        System.out.println("Result of Basics CheckNumber: " + result); 
    }

}


class Basics {
    Basics() {
        System.out.println("test");
    }

    void Basics_Method_One() {
        System.out.println("another test");
    }

    public static int CheckNumber(int my_int) {
        return 20 + my_int;
    }
}



