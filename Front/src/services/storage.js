class Storage {
  constructor(service) {
    this.service = service;
  }

  get(key, defaultValue = null) {
    return this.service.getItem(key) || defaultValue;
  }

  set(key, value) {
    this.service.setItem(key, value);

    return this;
  }

  has(key) {
    return this.get(key) !== null;
  }

  clear() {
    this.service.clear();
  }
}

export default new Storage(sessionStorage);
export const local = new Storage(localStorage);
