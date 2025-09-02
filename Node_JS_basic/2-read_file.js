const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8').trim();
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    lines.shift(); // remove header

    console.log(`Number of students: ${lines.length}`);

    const fields = {};
    lines.forEach((line) => {
      const details = line.split(',');
      const firstname = details[0];
      const field = details[3];
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    for (const [field, students] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
