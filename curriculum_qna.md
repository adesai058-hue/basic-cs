# Basic CS Curriculum - Practice Questions & Answers

This document contains a comprehensive set of practice questions and detailed answers designed to test understanding of the four basic Computer Science sessions in the lesson plan.

---

## 🐶 Session 1: Karel (Commands & Functions)

### Q1. What are the four basic commands that Karel understands out of the box?
**Answer:**
Karel understands the following four basic commands:
1. `move()`: Moves Karel forward one space in the direction it is facing.
2. `turnLeft()`: Rotates Karel 90 degrees to the left.
3. `putBall()`: Places one ball on Karel's current street and avenue.
4. `takeBall()`: Picks up one ball from Karel's current street and avenue.

---

### Q2. How would you write a helper function `turnRight()` in Karel using only basic commands?
**Answer:**
Since Karel can only turn left, turning right is equivalent to turning left three times:
```javascript
function turnRight() {
    turnLeft();
    turnLeft();
    turnLeft();
}
```

---

### Q3. Explain the concept of "Top-Down Design" and how it applies to writing Karel programs.
**Answer:**
Top-down design is a problem-solving strategy where you start with a big, complex problem and break it down into smaller, more manageable sub-problems (helper functions). 
In Karel, you implement this by:
1. Writing a main `start()` function that describes the overall solution at a high level.
2. Defining clear helper functions (like `solveHurdle()`, `buildTower()`, etc.) that execute the smaller parts of the task.
3. Breaking those helper functions down further if they are still too complex.

---

### Q4. Why is it important to name functions with clear action verbs (e.g., `cleanRow()` vs `row()`)?
**Answer:**
Functions perform actions. Naming them with active verbs makes the code self-documenting, readable, and easier to debug. For example:
- `cleanRow()` tells the reader exactly *what* action the function performs.
- `row()` is ambiguous—it could represent a variable holding row data, a row count, or something else entirely.

---

### Q5. What is the role of the `start()` function in a Karel program?
**Answer:**
The `start()` function serves as the entry point of the Karel program. When the program runs, execution starts inside the `start()` function, which calls other helper functions to carry out the program's main objective.

---

## 🔄 Session 2: Variables & Loops

### Q6. What is the difference between `let` and `const` in JavaScript?
**Answer:**
- `let` is used to declare variables whose values **can** be reassigned later in the program.
- `const` is used to declare constants whose values **cannot** be reassigned once set. Attempting to do so will result in a runtime error.
*Example:*
```javascript
let score = 10;
score = 15; // Allowed

const pi = 3.14;
pi = 3.1415; // Error!
```

---

### Q7. How do you find the length of a string in JavaScript, and what property do you use?
**Answer:**
You use the `.length` property of a string.
*Example:*
```javascript
const name = "Karel";
console.log(name.length); // Outputs: 5
```

---

### Q8. Write a `for` loop that prints the numbers from 1 to 5 to the console.
**Answer:**
```javascript
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
```

---

### Q9. When would you choose to use a `while` loop instead of a `for` loop?
**Answer:**
- Use a **`for` loop** when you know the exact number of times the loop needs to run (e.g., repeating a task exactly 10 times).
- Use a **`while` loop** when you want the loop to continue running until a specific condition changes, and you don't know in advance how many iterations that will take (e.g., moving Karel forward `while (frontIsClear())`).

---

### Q10. What does the `break` statement do inside a loop? Give a code example.
**Answer:**
The `break` statement immediately terminates the loop it is inside, and program control resumes at the next statement outside the loop.
*Example:*
```javascript
for (let i = 1; i <= 10; i++) {
    if (i === 5) {
        break; // Stops the loop when i reaches 5
    }
    console.log(i); // Prints 1, 2, 3, 4
}
```

---

## 🔀 Session 3: Control Structures

### Q11. Explain what comparison operators are and list four examples.
**Answer:**
Comparison operators are used to compare two values and return a boolean value (`true` or `false`).
Examples:
1. `===` (Equal to)
2. `!==` (Not equal to)
3. `>` (Greater than)
4. `<=` (Less than or equal to)

---

### Q12. What are the three main logical operators in JavaScript and what do they do?
**Answer:**
1. `&&` (Logical AND): Returns `true` if **both** operands are true.
2. `||` (Logical OR): Returns `true` if **at least one** operand is true.
3. `!` (Logical NOT): Reverses the boolean value of the operand (turns `true` to `false` and vice versa).

---

### Q13. Write a function named `isEligible` that takes an parameter `age` and returns `true` if the age is 18 or older, and `false` otherwise.
**Answer:**
```javascript
function isEligible(age) {
    if (age >= 18) {
        return true;
    } else {
        return false;
    }
}
// Shorter equivalent version:
// function isEligible(age) { return age >= 18; }
```

---

### Q14. What is block scope, and can a variable declared with `let` inside an `if` block be accessed outside of it?
**Answer:**
Block scope means variables declared inside curly braces `{}` are only accessible within that block.
No, a variable declared with `let` inside an `if` block cannot be accessed outside the block.
*Example:*
```javascript
if (true) {
    let message = "Hello";
}
console.log(message); // ReferenceError: message is not defined
```

---

### Q15. Create a conditional structure using `if`, `else if`, and `else` that logs "Go" if a variable `light` is "green", "Slow down" if it is "yellow", and "Stop" for any other color.
**Answer:**
```javascript
let light = "yellow";

if (light === "green") {
    console.log("Go");
} else if (light === "yellow") {
    console.log("Slow down");
} else {
    console.log("Stop");
}
```

---

## 📊 Session 4: Arrays & Lists

### Q16. How do you access the first and last element of an array named `colors`?
**Answer:**
Arrays are zero-indexed, meaning the first element is at index `0`. The last element is at index `length - 1`.
- **First element:** `colors[0]`
- **Last element:** `colors[colors.length - 1]`

---

### Q17. How do you modify an element at index 2 of an array named `fruits` to be "Mango"?
**Answer:**
```javascript
fruits[2] = "Mango";
```

---

### Q18. What is the difference between `push()` and `pop()` array methods?
**Answer:**
- `push(item)`: Adds one or more elements to the **end** of the array.
- `pop()`: Removes and returns the **last** element of the array.
*Example:*
```javascript
let numbers = [1, 2];
numbers.push(3); // numbers is now [1, 2, 3]
let last = numbers.pop(); // last is 3, numbers is back to [1, 2]
```

---

### Q19. What does `indexOf()` return if the element is in the array, and what does it return if it is not?
**Answer:**
- If the element is found, it returns the **first index** at which the element exists.
- If the element is **not** found, it returns `-1`.
*Example:*
```javascript
let items = ["apple", "banana"];
console.log(items.indexOf("banana")); // Prints: 1
console.log(items.indexOf("orange")); // Prints: -1
```

---

### Q20. Write a loop that iterates through an array named `grades` and logs each grade to the console.
**Answer:**
```javascript
let grades = [85, 92, 78, 90];

for (let i = 0; i < grades.length; i++) {
    console.log(grades[i]);
}
```
