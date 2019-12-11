"use strict";


/** 1. printIndices */
function printIndices(items) {
	// Replace this with your code
  for (const i in items) {
    console.log(items[i], i);
  }
}


/** 2. everyOtherItem */
function everyOtherItem(items) {
	// Replace this with your code
  let result = []
  for (const i in items) {
    if (i % 2 === 0) {
      result.push(items[i]);
    }
  }
  console.log(result);
}


/** 3. smallestNItems */
function smallestNItems(items, n) {
	// Replace this with your code
  let sortedItems = items.sort((a, b) => a - b);
  let sortedNItems = sortedItems.slice(0, n);
  sortedNItems.reverse();
  console.log(sortedNItems);
}


