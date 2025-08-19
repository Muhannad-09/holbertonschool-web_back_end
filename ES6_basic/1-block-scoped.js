export default function taskBlock(trueOrFalse) {
  let task = false;   // use let instead of var
  let task2 = true;   // use let instead of var

  if (trueOrFalse) {
    let task = true;   // new block-scoped variable
    let task2 = false; // new block-scoped variable
  }

  return [task, task2]; // outer variables remain unchanged
}
