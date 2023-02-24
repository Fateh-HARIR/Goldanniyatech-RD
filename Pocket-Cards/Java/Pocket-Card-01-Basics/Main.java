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

    public static void main(String[] args) {

        System.out.println("Hello world!");

        // Create a new object
        Main object_one = new Main();
        System.out.println(object_one.double_one);
    }
}



