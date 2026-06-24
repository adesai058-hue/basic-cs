# Basic CS Curriculum - 80 Practice Questions & Answers

This document contains a comprehensive bank of 80 practice questions and answers categorized by the four sessions of the CS curriculum.

---

## 🐶 Session 1: Karel (Commands & Functions)

### Q1. What does the `move()` command do?
**Answer:** It moves Karel forward one space in the direction it is currently facing.

### Q2. What does the `turnLeft()` command do?
**Answer:** It rotates Karel 90 degrees counter-clockwise (to the left) in its current position.

### Q3. What does the `putBall()` command do?
**Answer:** It places one tennis ball on Karel's current street and avenue intersection.

### Q4. What does the `takeBall()` command do?
**Answer:** It picks up one tennis ball from Karel's current street and avenue intersection.

### Q5. How does Karel turn around (180 degrees) using basic commands?
**Answer:** Since Karel has no built-in `turnAround()` command, you call `turnLeft()` twice:
```javascript
function turnAround() {
    turnLeft();
    turnLeft();
}
```

### Q6. How does Karel turn right (270 degrees) using basic commands?
**Answer:** You turn left three times:
```javascript
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

### Q7. What is a syntax error in Karel?
**Answer:** A syntax error is a grammatical mistake in the code (e.g., misspelling a command like `mov();`, forgetting parentheses, or omitting curly braces) that prevents the program from running.

### Q8. How do you define a new function in Karel?
**Answer:** You use the `function` keyword followed by the function name, parentheses, and curly braces:
```javascript
function nameYourFunction() {
    // commands go here
}
```

### Q9. What is the entry point of any Karel program?
**Answer:** The `start()` function. When the program runs, the computer looks for and executes `start()` first.

### Q10. What is "Top-Down Design"?
**Answer:** It is a programming methodology where you break a big problem into smaller, simpler, and named sub-problems (helper functions).

### Q11. What is "Stepwise Refinement"?
**Answer:** The process of gradually developing a complex program by writing and testing helper functions one step at a time, moving from the most general tasks to specific details.

### Q12. Why is code indentation important in Karel?
**Answer:** It makes the code readable and helps visualize which commands belong inside which functions or loops. In JS/Karel, code inside curly braces is indented by 4 spaces.

### Q13. Which sensory condition checks if Karel can move forward?
**Answer:** `frontIsClear()`, which returns `true` if there is no wall directly in front of Karel, and `false` if there is.

### Q14. What are some of Karel's sensory conditions?
**Answer:**
- `frontIsClear()` / `frontIsBlocked()`
- `leftIsClear()` / `leftIsBlocked()`
- `rightIsClear()` / `rightIsBlocked()`
- `ballsPresent()` / `noBallsPresent()`
- `facingNorth()`, `facingSouth()`, `facingEast()`, `facingWest()`

### Q15. What happens if Karel tries to move into a wall?
**Answer:** The program crashes or throws a "Karel crashed into a wall!" runtime error.

### Q16. What happens if Karel tries to take a ball when no balls are present?
**Answer:** The program crashes with an error stating there are no balls to retrieve.

### Q17. Why do we write helper functions instead of putting all commands in `start()`?
**Answer:** It keeps the code clean, avoids repetition (makes code reusable), and makes the program easier to read, write, and debug.

### Q18. Give an example of a good descriptive function name for picking up a row of balls.
**Answer:** `cleanRow()` or `pickUpRow()` are good because they start with clear action verbs. A bad name would be `row()` or `balls()`.

### Q19. What is the difference between a function definition and a function call?
**Answer:**
- **Definition:** Writing the code that details *what* the function does: `function walk() { move(); }`
- **Call:** Instructing the computer to *run* that function: `walk();`

### Q20. True or False: Karel can move diagonally.
**Answer:** False. Karel can only move in the direction it is facing (North, South, East, or West).

---

## 🔄 Session 2: Variables & Loops

### Q21. What is a variable in programming?
**Answer:** A named container used to store data values that can be referenced and manipulated in a program.

### Q22. How do you declare a variable using `let`?
**Answer:** Use the `let` keyword, followed by the variable name:
```javascript
let count;
```

### Q23. How do you declare a variable using `const`?
**Answer:** Use the `const` keyword, followed by the name and an immediate initial value:
```javascript
const name = "Karel";
```

### Q24. Explain the difference between variable declaration and variable initialization.
**Answer:**
- **Declaration:** Creating the variable name: `let score;`
- **Initialization:** Assigning the first value to the variable: `score = 10;`

### Q25. What is a primitive data type? Name three.
**Answer:** Primitive data types are the most basic types of data in JavaScript. Examples:
1. `Number` (e.g., `5`, `3.14`)
2. `String` (e.g., `"Hello"`)
3. `Boolean` (e.g., `true`, `false`)

### Q26. What value does a variable have if it is declared but not initialized?
**Answer:** Its value is `undefined`.

### Q27. How do you print something to the console in JavaScript?
**Answer:** Using the `console.log()` command:
```javascript
console.log("Hello, World!");
```

### Q28. What is a string?
**Answer:** A sequence of characters wrapped in single quotes (`'...'`), double quotes (`"..."`), or backticks (`` `...` ``).

### Q29. How do you concatenate two strings?
**Answer:** You use the `+` operator:
```javascript
let greeting = "Hello " + "World"; // "Hello World"
```

### Q30. What is the property to find the length of a string?
**Answer:** The `.length` property:
```javascript
let word = "Java";
console.log(word.length); // 4
```

### Q31. How do you access the first character of a string?
**Answer:** Using bracket notation with index `0`:
```javascript
let name = "Karel";
let firstChar = name[0]; // "K"
```

### Q32. What is a `for` loop?
**Answer:** A loop control structure used to repeat a block of code a specific number of times.

### Q33. What are the three parts of a `for` loop control statement?
**Answer:**
1. **Initialization:** Sets the starting point (e.g., `let i = 0;`).
2. **Condition:** Checked before each loop iteration (e.g., `i < 10;`).
3. **Increment/Decrement:** Changes the counter variable after each iteration (e.g., `i++`).
*Example:* `for (let i = 0; i < 10; i++)`

### Q34. What is a `while` loop?
**Answer:** A loop control structure that continues executing a block of code as long as its condition remains `true`.

### Q35. What is a loop variable?
**Answer:** A variable (commonly named `i`, `j`, or `k`) used to count or track the iterations of a loop.

### Q36. What is an infinite loop and how does it happen?
**Answer:** A loop that never stops running because the exit condition is never met (e.g., `while(true) {}` or a loop condition that always evaluates to `true`).

### Q37. What does the `break` statement do?
**Answer:** It immediately exits the loop, jumping to the code directly after the loop block.

### Q38. What is the increment operator (`++`)?
**Answer:** An operator that adds `1` to the value of a number variable: `x++` is equivalent to `x = x + 1`.

### Q39. What is the decrement operator (`--`)?
**Answer:** An operator that subtracts `1` from the value of a number variable: `x--` is equivalent to `x = x - 1`.

### Q40. How do you change a variable `y` by adding 5 to it using shorthand notation?
**Answer:**
```javascript
y += 5; // equivalent to y = y + 5;
```

---

## 🔀 Session 3: Control Structures

### Q41. What is a boolean?
**Answer:** A data type that can only have one of two values: `true` or `false`.

### Q42. Name the comparison operators for equality and inequality.
**Answer:**
- Equality: `===` (Strict equality)
- Inequality: `!==` (Strict inequality)

### Q43. What is the difference between `==` and `===`?
**Answer:**
- `==` compares values for equality after performing type conversion (coercion).
- `===` compares both the value and the type strictly (no coercion).

### Q44. What does the `>` operator check?
**Answer:** It checks if the value on the left is strictly greater than the value on the right.

### Q45. What does the `<=` operator check?
**Answer:** It checks if the value on the left is less than or equal to the value on the right.

### Q46. What is the logical AND (`&&`) operator?
**Answer:** It combines two conditions and returns `true` only if both conditions are `true`.

### Q47. What is the logical OR (`||`) operator?
**Answer:** It combines two conditions and returns `true` if at least one of the conditions is `true`.

### Q48. What is the logical NOT (`!`) operator?
**Answer:** It negates a boolean value, changing `true` to `false` and `false` to `true`.

### Q49. How does an `if` statement work?
**Answer:** It runs a block of code if, and only if, its specified condition evaluates to `true`.

### Q50. What is the purpose of an `else` statement?
**Answer:** It provides an alternative block of code to run when the `if` condition evaluates to `false`.

### Q51. When do you use `else if` instead of multiple `if` statements?
**Answer:** When you have multiple mutually exclusive conditions (where only one block should run). In a chain of `if-else if-else`, once one condition is true, the rest are ignored.

### Q52. How do you define a function with parameters in JavaScript?
**Answer:** Place the parameter names inside the parentheses in the function declaration:
```javascript
function greetUser(name) {
    console.log("Hello, " + name);
}
```

### Q53. What is the difference between a parameter and an argument?
**Answer:**
- **Parameter:** The variable named in the function definition (e.g., `name`).
- **Argument:** The actual value passed to the function when calling it (e.g., `"Arham"` in `greetUser("Arham");`).

### Q54. What does the `return` statement do in a function?
**Answer:** It exits the function and sends a value back to the place where the function was called.

### Q55. What happens to the execution of a function after a `return` statement is run?
**Answer:** The function stops executing immediately. Any code written after the `return` statement in that block is ignored (unreachable code).

### Q56. What is global scope?
**Answer:** Variables declared outside any function or block are in the global scope and can be accessed from anywhere in the program.

### Q57. What is local/function scope?
**Answer:** Variables declared inside a function are local to that function and cannot be accessed from outside the function.

### Q58. What is block scope?
**Answer:** Variables declared with `let` or `const` inside curly braces `{}` (like in loops or conditionals) are scoped to that block and cannot be accessed outside of it.

### Q59. Can a function have multiple parameters? Show an example.
**Answer:** Yes.
```javascript
function add(num1, num2) {
    return num1 + num2;
}
```

### Q60. Write a function `multiply` that takes two numbers and returns their product.
**Answer:**
```javascript
function multiply(a, b) {
    return a * b;
}
```

---

## 📊 Session 4: Arrays & Lists

### Q61. What is an array?
**Answer:** An ordered list of values grouped together inside bracket notation `[...]`.

### Q62. How do you create an empty array in JavaScript?
**Answer:**
```javascript
let arr = [];
```

### Q63. How are elements in an array indexed?
**Answer:** Arrays are zero-indexed. The first element is at index `0`, the second is at index `1`, and so on.

### Q64. How do you access the element at index 3 of an array `arr`?
**Answer:**
```javascript
let element = arr[3];
```

### Q65. How do you change the first element of an array to "Apple"?
**Answer:**
```javascript
arr[0] = "Apple";
```

### Q66. How do you get the number of elements in an array?
**Answer:** By using the `.length` property of the array:
```javascript
let size = arr.length;
```

### Q67. What does the `push()` method do?
**Answer:** It appends a new element to the end of the array.
```javascript
let list = [1, 2];
list.push(3); // [1, 2, 3]
```

### Q68. What does the `pop()` method do?
**Answer:** It removes and returns the last element of the array.
```javascript
let list = [1, 2, 3];
let last = list.pop(); // last is 3; list is [1, 2]
```

### Q69. How does `indexOf()` work?
**Answer:** It searches the array for a specific element and returns the first index at which it is found.

### Q70. What does `indexOf()` return if the item is not found?
**Answer:** It returns `-1`.

### Q71. What does the `splice()` method do?
**Answer:** It changes the contents of an array by removing, replacing, or adding elements at a specific index:
`arr.splice(startIndex, deleteCount, item1, item2, ...)`

### Q72. How do you remove the first element of an array?
**Answer:** Using the `shift()` method:
```javascript
let list = [1, 2, 3];
list.shift(); // removes 1, list is now [2, 3]
```

### Q73. How do you write a `for` loop to iterate through an array named `scores`?
**Answer:**
```javascript
for (let i = 0; i < scores.length; i++) {
    console.log(scores[i]);
}
```

### Q74. How do you access the last element of an array dynamically?
**Answer:**
```javascript
let last = arr[arr.length - 1];
```

### Q75. Can an array store different data types at the same time in JavaScript?
**Answer:** Yes. A JavaScript array can contain numbers, strings, booleans, objects, and other arrays all at once.

### Q76. What is the index of the last element in an array of length `N`?
**Answer:** The index is `N - 1`.

### Q77. Write a loop to calculate the sum of all numbers in an array named `nums`.
**Answer:**
```javascript
let sum = 0;
for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
}
```

### Q78. What happens if you try to access an index that doesn't exist in an array (e.g., `arr[100]` on a 3-element array)?
**Answer:** It returns `undefined` instead of throwing an error.

### Q79. How do you add an element to the beginning of an array?
**Answer:** Using the `unshift()` method:
```javascript
let list = [2, 3];
list.unshift(1); // list is now [1, 2, 3]
```

### Q80. What is the difference between an array and a primitive variable?
**Answer:** A primitive variable stores a single value (e.g., `x = 5`), whereas an array is a collection/data structure that can store multiple ordered values (e.g., `list = [5, 10, 15]`).
