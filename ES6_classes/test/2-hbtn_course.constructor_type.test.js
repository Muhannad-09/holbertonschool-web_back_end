import HolbertonCourse from "../2-hbtn_course.js";

test("HolbertonCourse checks constructor types", () => {
  // Name must be a string
  expect(() => {
    new HolbertonCourse(10, 20, ["Lucie", "Guillaume"]);
  }).toThrow();

  // Length must be a number
  expect(() => {
    new HolbertonCourse("PHP", "20", ["Lucie", "Guillaume"]);
  }).toThrow();

  // Students must be an array of strings
  expect(() => {
    new HolbertonCourse("PHP", 20, [10, 20]);
  }).toThrow();
});
