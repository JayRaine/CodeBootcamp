// Practice Set 2
// Ok everyone, now lets put our knowledge to the test. and try to solve the following questions.
// Q1: Using Logical Operators
// Create a JavaScript program to check if a age is between 10 and 20.
let age = prompt("Enter your age");
age = Number.parseInt(age);
if (age < 10 ){
    alert("Invalid age");
}
else if (age >= 10 && age <= 20){
    alert("This is a valid age");
}

// Q2: Using Switch Case
// Demonsrate the use of switch case in JavaScript.
const month = 3;

switch (month) {
  case 1:
    console.log("It's Jan!");
    break;
  case 2:
    console.log("It's Feb!");
    break;
  case 3:
    console.log("It's March!");
    break;
  case 4:
    console.log("It's April!");
    break;
  case 5:
    console.log("It's May!");
    break;
  case 6:
    console.log("It's June!");
    break;
  case 7:
    console.log("It's July!");
    break;
  case 8:
    console.log("It's August!");
    break;
  case 9:
    console.log("It's September!");
    break;
  case 10:
    console.log("It's October!");
    break;
  case 11:
    console.log("It's November!");
    break;
  case 12:
    console.log("It's December!");
    break;      
  default:
    console.log("Invalid day!");
}
// Q3: Divisible by 2 and 3
// Create a JavaScript program to check if a number is divisible by 2 and 3.
function isDivisibleBy2And3(number) {
    return number % 2 === 0 && number % 3 === 0;
  }
  
  // Test the function
  const number1 = 12; // divisible by both 2 and 3
  const number2 = 8;  // divisible by 2 but not by 3
  const number3 = 9;  // divisible by 3 but not by 2
  const number4 = 7;  // not divisible by both 2 and 3
  
  console.log(`${number1} is divisible by 2 and 3: ${isDivisibleBy2And3(number1)}`);
  console.log(`${number2} is divisible by 2 and 3: ${isDivisibleBy2And3(number2)}`);
  console.log(`${number3} is divisible by 2 and 3: ${isDivisibleBy2And3(number3)}`);
  console.log(`${number4} is divisible by 2 and 3: ${isDivisibleBy2And3(number4)}`);
  

// Q4: Divisible by 2 or 3
// Create a JavaScript program to check if a number is divisible by 2 or 3.

// Q5: Using Ternary Operator
// Print "you can drive" if the age is greater than or equal to 18, otherwise print "you cannot drive". Use the ternary operator.

let a = prompt("Hey whats you age?");
a = Number.parseInt(a); // Converting the string to a number
if(a<0){
  alert("This is an invalid age");
}
else if(a<9){
  alert("You are a kid and you cannot even think of driving");
}
else if(a<18 && a>=9){
  alert("You are a kid and you can think of driving after 18");
}
else{
  alert("You can now drive as you are above 18");
}
console.log("Done")
// HomeWork - Explore switch statement and write a basic program in the comments
console.log("You can", (a<18? "not drive" :"drive"))

// Congratulations! You have completed the practice set. Now you can move on to the next chapter.