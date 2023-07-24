// Practice Set 4
// Time to practice what you've learned! This practice set will help you get comfortable with the concepts you've learned in previous lessons.
// Question 1
// What will the following code print in JavaScript?

console.log("har\"".length) // 4

// Question 2
// Explore the includes, startsWith, and endsWith functions in a string.
const str1 = "Hello, world!";

console.log(str1.includes("Hello")); // Output: true
console.log(str1.includes("world")); // Output: true
console.log(str1.includes("foo"));   // Output: false

const str2 = "Hello, world!";

console.log(str2.startsWith("Hello")); // Output: true
console.log(str2.startsWith("world")); // Output: false

const str3 = "Hello, world!";

console.log(str3.endsWith("world!")); // Output: true
console.log(str3.endsWith("Hello"));  // Output: false
// Question 3
// Write a program to convert a given string into lowercase.

let sentance = prompt("Enter a sentence: ").toUpperCase(); // Console
console.log(sentance); // Output:

// Question 4
// Extract the numerical amount from this string "Total: Rupees 2907".

const str = "Total: Rupees 2907";

console.log(str.match(/\d+/g)); // Output: 2907

// Question 5
// Try to change the 4th character of a given string. Would you be able to do it?

let str5 = "Hello, world!";

// Create a new string with the 4th character replaced
let newStr5 = str5.substring(0, 3) + "!" + str5.substring(4);

console.log(newStr5); // Output: Hel!o, world!