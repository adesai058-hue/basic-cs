# Basic CS Curriculum - 80 Practice Questions & Answers (Java Edition)

This document contains a comprehensive bank of 80 practice questions and answers designed around the curriculum, fully adapted for **Java**.

---

## 🐶 Session 1: Karel (Commands & Functions)

### Q1. What does the `move();` command do in Java Karel?
**Answer:** It moves Karel forward one space in the direction it is currently facing.

### Q2. What does the `turnLeft();` command do?
**Answer:** It rotates Karel 90 degrees counter-clockwise (to the left) in its current position.

### Q3. What does the `putBall();` command do?
**Answer:** It places one tennis ball on Karel's current intersection (street and avenue).

### Q4. What does the `takeBall();` command do?
**Answer:** It picks up one tennis ball from Karel's current intersection.

### Q5. How do you write a method `turnAround()` in Java Karel?
**Answer:** Since Karel has no built-in `turnAround()` method, you define a method that calls `turnLeft();` twice:
```java
public void turnAround() {
    turnLeft();
    turnLeft();
}
```

### Q6. How do you write a method `turnRight()` in Java Karel?
**Answer:** You turn left three times:
```java
public void turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

### Q7. What is a syntax error in Java?
**Answer:** A syntax error is a violation of the language's grammatical rules (e.g., forgetting a semicolon `;`, mismatching curly braces `{}`, or spelling a command wrong) that prevents the code from compiling.

### Q8. How do you define a helper method in a Java Karel program?
**Answer:** You define it inside the class, using the `public void` keywords followed by the name, parentheses, and curly braces:
```java
public void pickRow() {
    // Method body
}
```

### Q9. What is the entry point method for a Java Karel program?
**Answer:** The `run()` method. When the program starts, execution begins inside:
```java
public void run() {
    // code starts here
}
```

### Q10. What is "Top-Down Design"?
**Answer:** A programming strategy where you break a large, complex problem into smaller, named sub-problems (implemented as helper methods in Java).

### Q11. What is "Stepwise Refinement"?
**Answer:** The process of gradually developing a program by writing and testing helper methods one at a time, moving from the high-level logic to specific details.

### Q12. Why is code indentation and formatting critical in Java?
**Answer:** While the Java compiler doesn't require indentation, it is essential for human readability to show the structure of blocks (classes, methods, loops) and find errors easily.

### Q13. Which condition checks if Karel has a clear path forward?
**Answer:** The `frontIsClear()` method, which returns `true` if there is no wall directly in front of Karel, and `false` if there is.

### Q14. What are some of Karel's sensory conditions in Java?
**Answer:**
- `frontIsClear()` / `frontIsBlocked()`
- `leftIsClear()` / `leftIsBlocked()`
- `rightIsClear()` / `rightIsBlocked()`
- `ballsPresent()` / `noBallsPresent()`
- `facingNorth()`, `facingSouth()`, `facingEast()`, `facingWest()`

### Q15. What happens if Karel moves into a wall in Java?
**Answer:** The program crashes at runtime, throwing an error indicating that Karel crashed into a wall.

### Q16. What happens if Karel tries to pick up a ball when none are present?
**Answer:** The program crashes at runtime because there is no ball to take.

### Q17. Why do we write helper methods instead of putting all code in `run()`?
**Answer:** It makes the code reusable, avoids duplication, and keeps the program organized and easier to read and debug.

### Q18. Give an example of a good descriptive method name for picking up a row of balls in Java.
**Answer:** `cleanRow()` or `pickUpRow()` (camelCase, starting with an active verb).

### Q19. What is the difference between a method declaration and a method call in Java?
**Answer:**
- **Declaration:** Defining the method: `public void walk() { move(); }`
- **Call:** Instructing the program to execute it: `walk();`

### Q20. True or False: A Java Karel class must extend `Karel` or `SuperKarel`.
**Answer:** True. This inheritance allows your class to use Karel's built-in commands and conditions.

---

## 🔄 Session 2: Variables & Loops

### Q21. What is a variable in Java?
**Answer:** A named memory location used to store a value of a specific data type.

### Q22. How do you declare a variable in Java?
**Answer:** In Java, you must specify the data type before the variable name:
```java
int count;
```

### Q23. How do you declare a constant (read-only) variable in Java?
**Answer:** You use the `final` keyword:
```java
final double PI = 3.14159;
```

### Q24. Explain the difference between variable declaration and variable initialization in Java.
**Answer:**
- **Declaration:** Declares the type and name: `int score;`
- **Initialization:** Assigns the first value: `score = 0;`

### Q25. What is a primitive data type? Name three in Java.
**Answer:** Basic data types built into Java. Examples:
1. `int` (for integers)
2. `double` (for decimal numbers)
3. `boolean` (for `true`/`false`)

### Q26. Can you assign a decimal value (like `5.5`) to an `int` variable in Java?
**Answer:** No. Doing so will cause a compilation error (type mismatch) unless you explicitly cast it: `int num = (int) 5.5;` (which truncates it to `5`).

### Q27. How do you print something to the console in Java?
**Answer:** Using `System.out.println()`:
```java
System.out.println("Hello, World!");
```

### Q28. What is a `String` in Java?
**Answer:** A `String` is an object representing a sequence of characters, wrapped in double quotes: `"Hello"`.

### Q29. How do you concatenate two strings in Java?
**Answer:** Using the `+` operator:
```java
String fullName = "Karel" + " the Robot";
```

### Q30. How do you find the length of a `String` in Java?
**Answer:** Using the `.length()` method:
```java
String word = "Java";
System.out.println(word.length()); // Prints: 4
```

### Q31. How do you access a specific character at index `i` in a Java String?
**Answer:** Using the `.charAt(i)` method:
```java
String name = "Karel";
char firstLetter = name.charAt(0); // 'K'
```

### Q32. What is a `for` loop in Java?
**Answer:** A control structure used to repeat a block of code a predetermined number of times.

### Q33. Write a Java `for` loop that prints numbers from 1 to 5.
**Answer:**
```java
for (int i = 1; i <= 5; i++) {
    System.out.println(i);
}
```

### Q34. What is a `while` loop in Java?
**Answer:** A loop that repeats a block of code as long as a specified boolean condition remains `true`.

### Q35. What is a loop counter variable?
**Answer:** A variable declared in a loop control statement (usually `i`, `j`, or `k`) that tracks the current iteration.

### Q36. What is an infinite loop and how does it happen in Java?
**Answer:** A loop that never terminates because its condition is always `true` (e.g., `while (true) { }`).

### Q37. What does the `break;` statement do inside a loop?
**Answer:** It immediately terminates the loop, jumping to the first line of code following the loop block.

### Q38. What is the increment operator (`++`)?
**Answer:** It increases the value of a numeric variable by 1: `x++;` is shorthand for `x = x + 1;`.

### Q39. What is the decrement operator (`--`)?
**Answer:** It decreases the value of a numeric variable by 1: `x--;` is shorthand for `x = x - 1;`.

### Q40. How do you add 5 to a variable `y` in Java using shorthand?
**Answer:**
```java
y += 5;
```

---

## 🔀 Session 3: Control Structures

### Q41. What values can a `boolean` variable hold in Java?
**Answer:** Only `true` or `false`.

### Q42. What are the Java comparison operators for equality and inequality?
**Answer:**
- Equality: `==`
- Inequality: `!=`

### Q43. How do you check if two Strings are identical in Java?
**Answer:** You must use the `.equals()` method rather than `==`:
```java
String s1 = "hello";
String s2 = "hello";
if (s1.equals(s2)) { ... }
```

### Q44. What does the `>` operator check?
**Answer:** If the value on the left is strictly greater than the value on the right.

### Q45. What does the `<=` operator check?
**Answer:** If the value on the left is less than or equal to the value on the right.

### Q46. What is the logical AND (`&&`) operator?
**Answer:** It returns `true` only if both boolean conditions on its left and right are `true`.

### Q47. What is the logical OR (`||`) operator?
**Answer:** It returns `true` if at least one of the conditions is `true`.

### Q48. What is the logical NOT (`!`) operator?
**Answer:** It negates a boolean value: `!true` becomes `false`, and `!false` becomes `true`.

### Q49. Write a basic `if` statement in Java.
**Answer:**
```java
if (score > 90) {
    System.out.println("A!");
}
```

### Q50. What does the `else` block do?
**Answer:** It defines a block of code to run only when the preceding `if` condition evaluates to `false`.

### Q51. When do you use `else if` instead of multiple independent `if` statements?
**Answer:** When you want only one block of code to run out of multiple conditions (mutually exclusive choices).

### Q52. How do you write a Java method that accepts parameters?
**Answer:** You define the parameter types and names inside the method parentheses:
```java
public void printDouble(int number) {
    System.out.println(number * 2);
}
```

### Q53. What is the difference between a parameter and an argument in Java?
**Answer:**
- **Parameter:** The variable declared in the method definition (e.g., `int number`).
- **Argument:** The actual value passed when calling the method (e.g., `5` in `printDouble(5);`).

### Q54. What is the purpose of the `return` keyword in a Java method?
**Answer:** It terminates method execution and sends a value back to the caller. The method must declare a return type matching this value instead of `void`.

### Q55. Can code be written in a method after a `return` statement?
**Answer:** No. Code directly following a return statement in the same block is unreachable and will cause a compiler error.

### Q56. What is class scope (instance variables) in Java?
**Answer:** Variables declared inside a class but outside any method. They are accessible by any method in that class.

### Q57. What is local/method scope in Java?
**Answer:** Variables declared inside a method. They can only be accessed within that method.

### Q58. What is block scope in Java?
**Answer:** Variables declared inside curly braces `{}` (like in an `if` block or `for` loop). They are only accessible inside those braces.

### Q59. Write a method signature for a method `calculateSum` that returns an `int` and takes two `int` parameters.
**Answer:**
```java
public int calculateSum(int num1, int num2) {
    return num1 + num2;
}
```

### Q60. Write a method `isEven` that returns `true` if an integer parameter is even, and `false` otherwise.
**Answer:**
```java
public boolean isEven(int n) {
    return n % 2 == 0;
}
```

---

## 📊 Session 4: Arrays & Lists

### Q61. What is an array in Java?
**Answer:** A fixed-size container that holds a collection of values of the same data type.

### Q62. How do you declare and instantiate a new integer array of size 5 in Java?
**Answer:**
```java
int[] nums = new int[5];
```

### Q63. What index is the first element in a Java array?
**Answer:** Index `0`.

### Q64. How do you access the element at index 3 in a Java array `arr`?
**Answer:**
```java
int value = arr[3];
```

### Q65. How do you change the first element of a String array named `names` to "Alice"?
**Answer:**
```java
names[0] = "Alice";
```

### Q66. How do you get the number of elements in a Java array?
**Answer:** Using the `.length` property (Note: no parentheses for arrays):
```java
int size = arr.length;
```

### Q67. What is an `ArrayList` in Java?
**Answer:** A resizable list class in Java (`java.util.ArrayList`) that grows dynamically as elements are added.

### Q68. How do you declare an `ArrayList` that holds Strings?
**Answer:**
```java
ArrayList<String> list = new ArrayList<String>();
```

### Q69. How do you add an element to the end of a Java `ArrayList` named `list`?
**Answer:** Using the `.add()` method:
```java
list.add("Karel");
```

### Q70. How do you remove an element at index 2 from a Java `ArrayList` named `list`?
**Answer:** Using the `.remove()` method:
```java
list.remove(2);
```

### Q71. How do you find the size of a Java `ArrayList`?
**Answer:** Using the `.size()` method:
```java
int total = list.size();
```

### Q72. How do you get an element at index 4 from an `ArrayList` named `list`?
**Answer:** Using the `.get()` method (not bracket notation `[]`):
```java
String value = list.get(4);
```

### Q73. Write a Java `for` loop to iterate through an integer array `nums`.
**Answer:**
```java
for (int i = 0; i < nums.length; i++) {
    System.out.println(nums[i]);
}
```

### Q74. Write a Java `for-each` loop to print all strings in an `ArrayList<String> names`.
**Answer:**
```java
for (String name : names) {
    System.out.println(name);
}
```

### Q75. How do you find the index of an element in an `ArrayList`?
**Answer:** Using the `.indexOf(element)` method, which returns the index of the first occurrence or `-1` if not found.

### Q76. What is the index of the last element in an array `arr`?
**Answer:** `arr.length - 1`.

### Q77. What happens if you try to access an index out of bounds in Java (e.g. `arr[5]` on an array of size 5)?
**Answer:** Java throws an `ArrayIndexOutOfBoundsException` at runtime and the program crashes.

### Q78. How do you set/replace the element at index 1 of an `ArrayList`?
**Answer:** Using the `.set(index, newValue)` method:
```java
list.set(1, "New Value");
```

### Q79. Can a primitive type (like `int`) be stored directly in an `ArrayList`?
**Answer:** No. `ArrayList` only stores objects. You must use Java wrapper classes like `Integer` (e.g., `ArrayList<Integer>`). Java will automatically convert `int` to `Integer` (autoboxing).

### Q80. What is the difference between a Java array and an `ArrayList`?
**Answer:** An **array** has a fixed size set at creation and can hold primitive types directly. An **`ArrayList`** has a dynamic size that changes automatically and can only hold objects (using wrappers for primitives).
