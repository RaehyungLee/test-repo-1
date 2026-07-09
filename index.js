const { add, multiply } = require("test-repo-2");

const numbers = [1, 2, 3, 4];

let total = 0;
let product = 1;
for (const n of numbers) {
  total = add(total, n);
  product = multiply(product, n);
}

console.log("sum:", total);
console.log("product:", product);
