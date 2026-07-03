const { add, multiply } = require("test-repo-2");
const _ = require("lodash");

const numbers = [1, 2, 3, 4, 5, 6];

const total = _.reduce(numbers, (acc, n) => add(acc, n), 0);
const product = _.reduce(numbers, (acc, n) => multiply(acc, n), 1);

console.log("sum:", total);
console.log("product:", product);

