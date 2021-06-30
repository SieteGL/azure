import config from "@/config/app.js";
import storage, { local } from "@/services/storage.js";

class Settings {
  static load() {
    const permanent =
      Settings.parse(local.get(config.STORAGE_KEY_SETTINGS)) || {};
    const properties =
      Settings.parse(storage.get(config.STORAGE_KEY_SETTINGS)) || {};

    return new Settings({
      merged: Object.assign({}, permanent, properties),
      permanent,
      session: properties
    });
  }

  static parse(text) {
    try {
      return JSON.parse(text);
    } catch (error) {
      return null;
    }
  }

  constructor(container = {}) {
    this.container = container;
  }

  get(key, defaultValue = null) {
    const {
      container: { merged }
    } = this;
    const value = merged[key];

    return typeof value !== "undefined" ? value : defaultValue;
  }

  set(key, value, permanent = false) {
    const { container: cnt } = this;

    if (permanent && this.specific(key) && cnt.session[key] !== value) {
      // No se actualiza el valor de merged ya que existe el valor en session storage
      // y esta tiene prioridad
    } else {
      cnt.merged[key] = value;
    }

    if (permanent) {
      cnt.permanent[key] = value;
    } else {
      cnt.session[key] = value;
    }

    this.store(permanent);

    return this;
  }

  store(permanent) {
    const { container: cnt } = this;
    const key = config.STORAGE_KEY_SETTINGS;

    if (permanent) {
      local.set(key, JSON.stringify(cnt.permanent));
    } else {
      storage.set(key, JSON.stringify(cnt.session));
    }

    return this;
  }

  specific(key, permanent = false) {
    return permanent
      ? this.container.permanent[key] !== null
      : this.container.session[key] !== null;
  }
}

export default Settings;
