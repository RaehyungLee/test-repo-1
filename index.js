const { add, multiply } = require("test-repo-2");
const _ = require("lodash");

const numbers = [1, 2, 3, 4];

function aggregate(values) {
  return {
    total: _.reduce(values, (acc, n) => add(acc, n), 0),
    product: _.reduce(values, (acc, n) => multiply(acc, n), 1),
    max: _.max(values),
  };
}

const { total, product, max } = aggregate(numbers);

console.log("sum:", total);
console.log("product:", product);
console.log("max:", max);
