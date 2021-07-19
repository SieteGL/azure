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
      .get(`${config.API_LOCATION}/listar/especialistas`, {
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

  async uploadDocument() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/documentos/usuario`, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async uploadDocumentRemove(document) {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.delete(
      `${config.API_LOCATION}/eliminar/documento/${document.id}`,
      {
        headers: { Authorization: authorization }
      }
    );
  },

  async uploadDocumentSave(document) {
    console.log(document);

    if (document.documento === null)
      throw new ValidationException("Debe seleccionar el tipo de documento");
    if (document.valor === null || !document.valor.length)
      throw new ValidationException("Debe seleccionar el valor de documento");
    if (document.imagen === null || typeof document.imagen === "undefined")
      throw new ValidationException("Debe subir una imagen");

    console.log(document);

    const formData = new FormData();
    const token = Token.load();
    const authorization = await token.authorization();

    for (const key in document) {
      if (Object.hasOwnProperty.call(document, key)) {
        formData.append(key, document[key]);
      }
    }

    // formData.append('file', this.file);

    return axios.post(`${config.API_LOCATION}/agregar/documento`, formData, {
      headers: {
        Authorization: authorization,
        "Content-Type": "multipart/form-data"
      }
    });
  },

  async clients() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios
      .get(`${config.API_LOCATION}/cliente/sistema`, {
        headers: { Authorization: authorization }
      })
      .then(({ data: { results: clients } }) => clients);
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
  },

  async clientDataSheetLoadAll() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/ficha`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  async procedureDelete(procedure) {
    // const token = Token.load();
    // const authorization = await token.authorization();

    return axios.delete(
      `${config.API_LOCATION}/eliminar/Procedimiento/${procedure.id}`
    );
  },

  /**
   * { "proceder": [{"pk": 2}], "tipo_procedimiento": 2, "descripcion_procedimiento": "esto es un ejemplo de procedimiento 2" }
   *
   * @param {Objeect} procedure
   */
  async procedureSave(procedure) {
    if (procedure.client === null)
      throw new ValidationException("Debe seleccionar un cliente");
    if (procedure.procedure === null)
      throw new ValidationException("Debe seleccionar el procedimiento");
    if (procedure.description === null || !procedure.description.length)
      throw new ValidationException(
        "Debe ingresar la descripción del procedimiento"
      );

    const token = Token.load();
    const authorization = await token.authorization();

    const body = {
      proceder: [{ pk: procedure.client }],
      tipo_procedimiento: procedure.procedure,
      descripcion_procedimiento: procedure.description
    };

    return axios.post(`${config.API_LOCATION}/agregar/procedimiento`, body, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async procedureEdit(procedure) {
    if (procedure.client === null)
      throw new ValidationException("Debe seleccionar un cliente");
    if (procedure.procedure === null)
      throw new ValidationException("Debe seleccionar el procedimiento");
    if (procedure.description === null || !procedure.description.length)
      throw new ValidationException(
        "Debe ingresar la descripción del procedimiento"
      );

    const token = Token.load();
    const authorization = await token.authorization();

    const body = {
      // TODO
      // Validar
      Especialista_Procedimiento: procedure.id,
      cliente: procedure.client,
      tipo_procedimiento: procedure.procedure,
      descripcion_procedimiento: procedure.description
    };

    return axios.put(
      `${config.API_LOCATION}/editar/Procedimiento/${procedure.id}`,
      body,
      {
        headers: {
          Authorization: authorization
        }
      }
    );
  },

  async procedureSaved() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/procedimiento`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  async products() {
    return axios.get(`${config.API_LOCATION}/almacen/list`, {
      params: {
        limit: 1000
      }
    });
  },

  async providers() {
    return axios.get(`${config.API_LOCATION}/proveedores/sistema`, {
      params: {
        limit: 1000
      }
    });
  },

  async orders() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/ordenes`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  async receptions() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/listar/no/agregados`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  async makeOrder(order, details) {
    if (order === null || !order.length)
      throw new ValidationException("Debe ingresar en nombre de la orden");
    if (!details.length)
      throw new ValidationException("Debe ingresar los productos");

    const token = Token.load();
    const authorization = await token.authorization();

    const body = {
      name: order,
      detalle: details.map(item => ({
        cantidad: item.quantity,
        precio_unitario: item.price,
        nombre_producto: item.name,
        familia: item.family,
        descripcion: item.description,
        recepcionado: "False",
        fecha_vencimiento: item.vigency,
        pk: item.provider.id
      }))
    };

    return axios.post(`${config.API_LOCATION}/pedido/p`, body, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async makeReception(product) {
    const token = Token.load();
    const authorization = await token.authorization();

    const body = {
      detalles: [{ pk: product.id }]
    };

    return axios.post(`${config.API_LOCATION}/crear/recepcion`, body, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async storeReception(product) {
    const token = Token.load();
    const authorization = await token.authorization();

    const body = {
      almacen: [{ pk: product.id }]
    };

    return axios.post(`${config.API_LOCATION}/cargar/almacen`, body, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async serviceCreate(service) {
    if (service.name === null || !service.name.length)
      throw new ValidationException("Debe ingresar el nombre del servicio");
    if (service.amount === null || !service.amount.length)
      throw new ValidationException("Debe ingresar el valor del servicio");
    if (!service.collection.length)
      throw new ValidationException("Debe ingresar el paquete de servicios");
    const token = Token.load();
    const authorization = await token.authorization();
    const body = {
      name: service.name,
      valor_paquete: service.amount,
      servicios_lista: service.collection.map(item => ({ servicio: item }))
    };
    return axios.post(`${config.API_LOCATION}/crear/servicios`, body, {
      headers: {
        Authorization: authorization
      }
    });
  },

  async serviceList() {
    return axios.get(`${config.API_LOCATION}/list/servicios`, {
      params: {
        limit: 1000
      }
    });
  },

  async serviceListDelete(service) {
    if (
      service === null ||
      service.id === null ||
      typeof service.id === "undefined"
    )
      throw new ValidationException("Debe ingresar el servicio a eliminar");

    // const token = Token.load();
    // const authorization = await token.authorization();

    return axios.delete(
      `${config.API_LOCATION}/eliminar/list-servicios/${service.id}`
    );
  },

  async serviceListCreated() {
    const token = Token.load();
    const authorization = await token.authorization();

    return axios.get(`${config.API_LOCATION}/servicios/lista`, {
      params: {
        limit: 1000
      },
      headers: {
        Authorization: authorization
      }
    });
  },

  async serviceListDeleteCreated(service) {
    if (
      service === null ||
      service.id === null ||
      typeof service.id === "undefined"
    )
      throw new ValidationException("Debe ingresar el servicio a eliminar");

    // const token = Token.load();
    // const authorization = await token.authorization();

    return axios.delete(
      `${config.API_LOCATION}/eliminar/servicios/${service.id}`
    );
  },

  async serviceNew(service) {
    if (service === null || !service.length)
      throw new ValidationException("Debe ingresar el nombre del servicio");

     const token = Token.load();
     const authorization = await token.authorization();

    const body = {
      servicio_nombre: service
    };

    return axios.post(`${config.API_LOCATION}/crear/lista/servicios`, body, { headers: {
      Authorization: authorization
    }});
  },

  async warehouseFilterList() {
    return axios.get(`${config.API_LOCATION}/filtrar/disponibles`, {
      params: {
        limit: 1000
      }
    });
  }
};

export default backend;
