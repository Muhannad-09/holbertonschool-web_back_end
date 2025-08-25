export default function cleanSet(set, startString) {
  const result = [];

  for (const value of set) {
    if (startString && value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    } else if (!startString) {
      result.push(value);
    }
  }

  return result.join('-');
}
