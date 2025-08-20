import HolbertonCourse from "../2-hbtn_course.js";

test("HolbertonCourse checks constructor types", () => {
  // name must be string
  expect(() => {
    new HolbertonCourse(10, 20, ["Lucie", "Guillaume"]);
  }).toThrow();

  // length must be number
  expect(() => {
    new HolbertonCourse("PHP", "20", ["Lucie", "Guillaume"]);
  }).toThrow();

  // students must be array of strings
  expect(() => {
    new HolbertonCourse("Python", 20, [10, "Guillaume"]);
  }).toThrow();
});
