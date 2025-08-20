import Car from './10-car.js';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    // Return a new Car instance instead of EVCar
    const clone = new Car();
    // Copy only the Car properties (exclude _range)
    for (const key of Object.keys(this)) {
      if (key !== '_range') {
        clone[key] = this[key];
      }
    }
    return clone;
  }
}
