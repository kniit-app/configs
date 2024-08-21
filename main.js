// Generate a random number between 1 and 100
const randomNumber = Math.floor(Math.random() * 100) + 1;

// Create an array of random colors
const colors = ["red", "blue", "green", "yellow", "purple"];
const randomColor = colors[Math.floor(Math.random() * colors.length)];

// Define a function to reverse a string
function reverseString(str) {
  return str.split("").reverse().join("");
}

// Create an object with random properties
const randomObject = {
  id: Math.random().toString(36).substr(2, 9),
  value: Math.random() * 1000,
  isActive: Math.random() < 0.5,
};

// Generate a random date within the last year
const randomDate = new Date(
  Date.now() - Math.floor(Math.random() * 31536000000),
);

console.log(`Random number: ${randomNumber}`);
console.log(`Random color: ${randomColor}`);
console.log(`Reversed 'Hello': ${reverseString("Hello")}`);
console.log("Random object:", randomObject);
console.log(`Random date: ${randomDate.toISOString()}`);

// Simulate an asynchronous operation
setTimeout(() => {
  console.log("Async operation completed!");
}, Math.random() * 1000);
