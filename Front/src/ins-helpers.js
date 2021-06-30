const privateMethods = {
  transformError(error) {
    const keys = Object.keys(error);

    if (keys.length > 1) {
      return `Los siguientes campos tienen errores: <b>${keys.join(", ")} </b>`;
    }

    const key = keys[0];
    return `El campo <b>${key}</b> tiene el siguiente error <b>${error[key][0]}</b>`;
  }
};

const methods = {
  chooseColorClass: function(color) {
    const values = {
      purple: "md-primary",
      blue: "md-info",
      green: "md-success",
      orange: "md-warning",
      red: "md-danger"
    };

    return { [values[color] || values.green]: true };
  },

  chooseNotificationMessage: function(error) {
    if (error.name === "ValidationException") {
      return error.message;
    }

    if (error.response && error.response.data) {
      return privateMethods.transformError(error.response.data);
    }

    return "Error al realizar la operación";
  },

  /**
   * Muestra un mensaje de notificación en la pantalla
   *
   * @param {string} message
   * @param {Object} [settings]
   * @param {string} [settings.horizontal]
   * @param {string} [settings.icon]
   * @param {string} [settings.type]
   * @param {string} [settings.vertical]
   */
  showNotificationMessage(
    message,
    {
      horizontal = "center",
      icon = "add_alert",
      type = "danger",
      vertical = "bottom"
    } = {}
  ) {
    this.$notify({
      horizontalAlign: horizontal,
      icon,
      message,
      type,
      verticalAlign: vertical
    });
  },

  vuelidate(key) {
    if (this.$v[key].$error) {
      return {
        "ls--md-invalid": true
      };
    }
  }
};

/**
 * You can register global components here and use them as a plugin in your main Vue instance
 */
const GlobalHelpers = {
  install(Vue, options) {
    Vue.mixin({ methods });
  }
};

export default GlobalHelpers;
