import { promises as fs } from 'fs';

export default function readDatabase(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => l !== '');
      lines.shift();

      const fields = {};
      for (const line of lines) {
        const [firstname, , , field] = line.split(',');
        if (!field || !firstname) continue;
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      }
      return fields;
    })
    .catch(() => {
      return Promise.reject(new Error('Cannot load the database'));
    });
}
