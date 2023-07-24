// Q1: Adding numbers to strings
// Create a variable of type string and try to add a number to it.
var a_sring = "hello ";
var number = 10;
answer = a_sring + number;
console.log(answer);
// Q2: Using typeof
// Use the typeof keyword to see the data type of the variables in the previous question.
typeof number;
// Q3: Const objects
// Create a constant object in JavaScript and then try to change its value to another data type.
const person = {
    name :"jay",
};
name = 1;
console.log(name);
// Q4: Modifying const objects
// Try to add a new key to the previous const object.
person.age = 28;
console.log(person);
// Q5: Month dictionary
// Create a JavaScript program to make a month dictionary like 1 = January, 2 = February, and so on.
const monthDictionary = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
  };
// Q6:Declaring variables
// In this exercise, you will practice declaring variables. Tasks
// Declare a new variable named petDog and give it the name Rex.
var petDog = "Rex";
// Declare a new variable named petCat and give it the name Pepper.
var petCat = "Pepper";
// Console.log the petDog variable.
console.log(petDog);
// Console.log the petCat variable.
console.log(petCat);
// Console.log the text "My pet dog's name is: " and the petDog variable.
console.log("My pet dog's name is: " + petDog);
// Console.log the text "My pet cat's name is: " and the petCat variable.
 console.log("My pet cat's name is: " + petCat);
// Declare another variable and name it catSound. Assign the string of "purr" to it.
 catSound = "purr";
// Declare another variable and name it dogSound. Assign the string of "woof" to it.
 dogSound = "woof";
// Console.log the variable petDog, then the string "says", then the variable dogSound.
console.log(petDog + " says " + dogSound);
// Console.log the variable petCat, then the string "says", then the variable catSound.
 console.log(petCat + " says " + catSound);
// Reassign the value stored in catSound to the string "meow".
 catSound = "meow";
// Console.log the variable petCat, then the string "now says", then the variable catSound. M ake sure to output all your variables. Feel free to play.
 console.log(petCat + " now says " + catSound);