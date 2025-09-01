const fs = require('fs').promises;

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.trim().split('\n');
      const [header, ...rows] = lines;

      const students = rows
        .filter((line) => line.trim() !== '')
        .map((line) => {
          const [firstname, lastname, age, field] = line.split(',');
          return { firstname, lastname, age, field };
        });

      console.log(`Number of students: ${students.length}`);

      const fields = {};
      students.forEach((student) => {
        if (!fields[student.field]) fields[student.field] = [];
        fields[student.field].push(student.firstname);
      });

      for (const [field, names] of Object.entries(fields)) {
        console.log(
          `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`
        );
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
