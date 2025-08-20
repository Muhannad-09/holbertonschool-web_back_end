export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    // Create a new instance of the same class as this object
    const clone = new this.constructor();

    // Copy all underscore properties
    for (const key of Object.keys(this)) {
      clone[key] = this[key];
    }

    return clone;
  }
}
