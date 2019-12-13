// Arrays
// const greeting = 'this is a phrase!'
// const greetSplit = greeting.split('');
// const greetCreate = greetSplit.join();
// const greetAssemble = greetSplit.join('');

// const randIndex = Math.floor(Math.random() * 17)
// greetSplit[randIndex]

// const randIndex2 = Math.floor(Math.random() * 17)
// const holding_space = greetSplit[randIndex]
// greetSplit[randIndex] = greetSplit[randIndex2]
// greetSplit[randIndex2] = holding_space

// Maps
const candy = {}
candy.purple = 'grape'
candy.red = 'cherry'
candy.green = 'kumquat'
candy.orange = 'persimmon'
candy.black = 'marshmellow'
for (const color in candy){
  console.log(`The ${candy[color]} flavor is colored ${color}`);
}

function candyFlavor(color, map) { 
  if (map[color]) {
    console.log(map[color]);
  } else {
    console.log('Sorry, that color doesn’t have a flavor');
  }
}

const colorArray = [];
for (const color in candy) {
  colorArray.push(color);
}

function colorToFlavor(colors) {
  const flavors = [];
  for (const color of colors) {
    if (candy[color]) {
      flavors.push(candy[color]);
    } else {
      flavors.push(null);
    }
  }
  return flavors;
}