import axios from "axios";
import config from "@/config/app.js";
import storage from "@/services/storage.js";
import Token from "@/services/Token.js";
import ValidationException from "@/exceptions/ValidationException.js";

const doctorsContainer = {
  "1": [
    {
      code: 1,
      name: "Dakota Rice",
      date: "2021-05-10",
      time: "15:30",
      duration: "30"
    },
    {
      code: 2,
      name: "Minerva Hooper",
      date: "2021-05-10",
      time: "15:30",
      duration: "45"
    }
  ],
  "2": [],
  "3": [
    {
      code: 3,
      name: "Sage Rodriguez",
      date: "2021-05-10",
      time: "15:30",
      duration: "30"
    },
    {
      code: 4,
      name: "Philip Chaney",
      date: "2021-05-10",
      time: "15:30",
      duration: "60"
    },
    {
      code: 5,
      name: "Doris Greene",
      date: "2021-05-10",
      time: "15:30",
      duration: "30"
    }
  ],
  "4": [
    {
      code: 6,
      name: "Mason Porter",
      date: "2021-05-10",
      time: "15:30",
      duration: "30"
    }
  ]
};

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
      { code: 1, name: "Odontologo" },
      { code: 2, name: "Ortodoncia" },
      { code: 3, name: "Radiologo" },
      { code: 4, name: "Prostodoncista" }
    ];
  },

  async doctors(speciality) {
    if (speciality === null) {
      return [
        ...doctorsContainer["1"],
        ...doctorsContainer["2"],
        ...doctorsContainer["3"],
        ...doctorsContainer["4"]
      ];
    }

    return doctorsContainer[`${speciality}`];
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

  async doctorsScheduleEvents() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/agenda`, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async doctorsSchedule(speciality, doctor) {
    const schedule =
      speciality !== null
        ? doctorsContainer[`${speciality}`]
        : [
            ...doctorsContainer["1"],
            ...doctorsContainer["2"],
            ...doctorsContainer["3"],
            ...doctorsContainer["4"]
          ];

    return doctor === null
      ? schedule
      : schedule.filter(item => item.code === doctor);
  }
};

export default backend;
