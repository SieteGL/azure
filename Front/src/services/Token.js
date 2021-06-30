import axios from "axios";
import config from "@/config/app.js";
import storage from "@/services/storage.js";

class Token {
  static load() {
    const tokens = Token.parse(storage.get(config.STORAGE_KEY_TOKEN));

    return new Token(tokens);
  }

  static parse(text) {
    try {
      return JSON.parse(text);
    } catch (error) {
      return null;
    }
  }

  constructor({ access, refresh }) {
    this.access = access;
    this.expirationTime = this.expireOn();
    this.refresh = refresh;
  }

  /**
   * @private
   *
   * @returns {string}
   */
  _atob() {
    return atob(this.access.split(".")[1]);
  }

  /**
   * @private
   *
   */
  async _refresh() {
    const { refresh } = this;

    return axios
      .post(config.API_LOCATION_TOKEN_REFRESH, { refresh })
      .then(({ data: { access } }) => access);
  }

  expireOn() {
    const time = Token.parse(this._atob()).exp;
    const seconds = 3;

    return new Date((time - seconds) * 1000);
  }

  inTime() {
    return this.expirationTime > new Date();
  }

  setAccess(access) {
    this.access = access;
    this.expirationTime = this.expireOn();

    this.store();
  }

  async authorization() {
    if (!this.inTime()) {
      this.setAccess(await this._refresh());
    }

    return `Bearer ${this.access}`;
  }

  store() {
    const { access, refresh } = this;

    storage.set(config.STORAGE_KEY_TOKEN, JSON.stringify({ access, refresh }));

    return this;
  }
}

export default Token;
