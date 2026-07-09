const { add, multiply } = require("test-repo-2");

const numbers = [1, 2, 3, 4];

// Aggregate with the native Array.prototype.reduce instead of lodash.
const total = numbers.reduce((acc, n) => add(acc, n), 0);
const product = numbers.reduce((acc, n) => multiply(acc, n), 1);

console.log("sum:", total);
console.log("product:", product);
