<<<<<<< HEAD:0-constants.js
=======
// 0-constants.js

>>>>>>> e0c0b3ac249917b51549e5090bcafe33a3822fe6:ES6_basic/0-constants.js
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
