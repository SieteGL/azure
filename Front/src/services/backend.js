import axios from "axios";
import config from "@/config/app.js";
import storage from "@/services/storage.js";
import Token from "@/services/Token.js";
import ValidationException from "@/exceptions/ValidationException.js";

const backend = {
  /**
   * Verifica si el usuario es del tipo administrador
   *
   * @param {string} token
   *
   * @returns {boolean}
   */
  async isAdmin(token, email) {
    return axios
      .get(config.API_LOCATION_IS_ADMIN, { headers: { Authorization: token } })
      .then(({ data: { results: admins } }) =>
        admins.some(item => item.email === email)
      )
      .catch(() => false);
  },

  /**
   * Verifica si el usuario es del tipo especilista
   * @param {*} token
   * @returns
   */
  async isSpecialist(token, email) {
    return axios
      .get(config.API_LOCATION_IS_SPECIALIST, {
        headers: { Authorization: token }
      })
      .then(({ data: { results: specialists } }) =>
        specialists.some(item => item.email === email)
      )
      .catch(() => false);
  },

  /**
   *
   * @param {string} email
   * @param {string} password
   *
   * @returns {Promise}
   */
  async login(email, password) {
    if (email === null || !email.length) throw new Error("Empty value");
    if (password === null || !password.length) throw new Error("Empty value");

    return axios
      .post(`${config.API_LOCATION}/token/`, { email, password })
      .then(({ data }) => data);
  },

  /**
   *
   * @param {Object} user
   *
   * @returns {Promise}
   */
  async register(user) {
    if (user.password !== user.password_confirmation)
      throw new ValidationException("Password not match");
    if (user.fecha_nacimiento === null)
      throw new ValidationException("The date of birth cannot be null");

    return axios.post(`${config.API_LOCATION}/register/cli/`, {
      ...user,
      fecha_nacimiento: user.fecha_nacimiento
        .split("-")
        .reverse()
        .join("-")
    });
  },

  /**
   *
   * @param {Object} user
   * @param {string} occupation
   *
   * @returns {Promise}
   */
  async registerUser(user, occupation) {
    if (user.password !== user.password_confirmation)
      throw new ValidationException("Password not match");
    if (user.fecha_nacimiento === null)
      throw new ValidationException("The date of birth cannot be null");
    if (!storage.has("token"))
      throw new ValidationException(
        "No se encontro el token en el almacenamiento"
      );

    const token = Token.load();
    const authorization = await token.authorization();

    return axios.post(
      `${config.API_LOCATION}/register/users/${config.USER_TYPE_IDS[occupation]}/`,
      {
        ...user,
        fecha_nacimiento: user.fecha_nacimiento
          .split("-")
          .reverse()
          .join("-")
      },
      {
        headers: {
          Authorization: authorization
        }
      }
    );
  },

  async specialties() {
    return [
      { code: 0, name: "Odontologo" },
      { code: 1, name: "Ortodoncista" },
      { code: 2, name: "Radiologo" },
      { code: 3, name: "Prostodoncista" }
    ];
  },

  async doctors() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios
      .get(`${config.API_LOCATION}/listar/especialistas`, {
        headers: { Authorization: authorization }
      })
      .then(({ data: { results: specialists } }) => specialists);
  },

  /**
   * Recupera las horas disponibles de un especilista utilizando el email.
   *
   * @param {string} speciality
   * @param {string} doctor
   *
   * @returns {Promise}
   */
  async doctorsSchedule(speciality, doctor) {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(
      `${config.API_LOCATION}/listar/agenda/especialista/${doctor}`,
      {
        params: {
          limit: 1000
        },
        headers: {
          Authorization: authorization
        }
      }
    );
  },

  /**
   * Crea una hora en la agenda del doctor
   *
   * { "fecha": "2021-07-03", "hora": [{ "hora": "12:00" }] }
   *
   * @param {string} date
   * @param {string} hour
   *
   * @returns {Promise}
   */
  async doctorsScheduleEvent(date, hour) {
    if (date === null)
      throw new ValidationException("Debe seleccionar la fecha del evento");
    if (hour === null || hour === false)
      throw new ValidationException("Debe seleccionar la hora del evento");

    const token = Token.load();
    const authorization = await token.authorization();

    return axios.post(
      `${config.API_LOCATION}/crear/agenda`,
      {
        fecha: date,
        hora: [{ hora: hour }]
      },
      {
        headers: {
          Authorization: authorization
        }
      }
    );
  },

  /**
   * Recupera las horas disponible del mismo especilista
   *
   * @returns {Promise}
   */
  async doctorsScheduleEvents() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/agenda`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  /**
   * Elimina una hora de la agenda
   */
  async doctorsScheduleEventDrop(event) {
    if (event === null)
      throw new ValidationException("Debe seleccionar el evento a eliminar");

    // const token = Token.load();
    // const authorization = await token.authorization();

    return axios.delete(
      `${config.API_LOCATION}/eliminar/agenda/hora/${event.id}`
    );
  },

  /**
   * Recupera las horas disponible del mismo especilista
   *
   * @returns {Promise}
   */
  async doctorsScheduleClientEvents() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/hora`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  /**
   * { "agenda": [{ "pk": 1 }] }
   *
   * @param {number} specialist
   * @returns
   */
  async doctorsScheduleTake(schedule) {
    // TODO
    // Validar posibles valores

    const token = Token.load();
    const authorization = await token.authorization();

    return axios.post(
      `${config.API_LOCATION}/tomar/hora`,
      {
        agenda: [{ pk: schedule }]
      },
      {
        headers: {
          Authorization: authorization
        }
      }
    );
  },

  async clientDataSheet(data) {
    // TODO
    // Validar posibles valores

    const token = Token.load();
    const authorization = await token.authorization();

    return axios.post(
      `${config.API_LOCATION}/agregar/ficha`,
      {
        alergia: data.alergia ? "S" : "N",
        alergias: data.alergias || "NO",
        enfermedad: data.enfermedad ? "S" : "N",
        enfermedades: data.enfermedades || "NO"
      },
      {
        headers: {
          Authorization: authorization
        }
      }
    );
  }
};

export default backend;
