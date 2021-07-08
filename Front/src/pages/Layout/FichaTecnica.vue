<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Ficha Técnica Paciente</h4>
            <p class="category">Ingrese los datos necesarios para su Ficha Técnica</p>
          </md-card-header>
          <md-card-content>
            
            <!-- declaracion de los radio buttons Enfermedad -->
            <div class="md-layout-item md-medium-size-100  md-size-50">
              <p class="category">¿Usted Presenta Alguna Enfermedad?</p>
              <md-radio v-model="radio" value="accent">Si</md-radio>
              <md-radio v-model="radio" value="Primary" class="md-primary">No</md-radio>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-35">
                <md-field :class="vuelidate('name')">
                  <label>¿Que Tipo de Enfermedad?</label>
                  <md-input v-model="name" type="text"></md-input>
                </md-field>
              </div>
            </div>

            <!-- declaracion de los radio buttons Alergias-->
            <div class="md-layout-item md-medium-size-100  md-size-50">
              <p class="category">¿Usted Presenta Alguna Alergia?</p>
              <md-radio v-model="radio" value="accent">Si</md-radio>
              <md-radio v-model="radio" value="Primary" class="md-primary">No</md-radio>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-35">
                <md-field :class="vuelidate('name')">
                  <label>¿Que Tipo de Alergia?</label>
                  <md-input v-model="name" type="text"></md-input>
                </md-field>
              </div>
            </div>

              <!-- declaracion Más de una Alergia-->
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-35">
                <md-field :class="vuelidate('name')">
                  <label>Escriba si tiene más de una alergia</label>
                  <md-input v-model="name" type="text"></md-input>
                </md-field>
              </div>
            </div>

              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="colorboton"
                  class="md-primary md-block"
                  v-on:click="submit"
                  :disabled="sending"
                  >Enviar</md-button
                >
              </div>

          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import backend from "@/services/backend.js";
import cut from "@/services/cut.js";
import rules from "@/services/validations.js";
import config from "@/config/app";

export default {

    name: 'RadioHueColors',
    data: () => ({
      radio: 'accent'
    }),

  validations: () =>
    rules([
      "occupation",
      "name",
      "lastname",
      "run",
      "username",
      "phone",
      "birthdate",
      "gender",
      "region",
      "city",
      "district",
      "address",
      "house",
      "password",
      "confirmPassword"
    ]),

  methods: {
    submit() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos requeridos");
        return;
      }

      const { regions, cities, districts } = this;

      const iregion = regions.find(item => item.code === this.region);
      const icity = cities.find(item => item.code === this.city);
      const idistrict = districts.find(item => item.code === this.district);

      this.sending = true;
      backend
        .registerUser(
          {
            nombre: this.name,
            apellido: this.lastname,
            rut: this.run,
            email: this.username,
            contacto: this.phone,
            fecha_nacimiento: this.birthdate,
            sexo: this.gender,
            region: iregion.name,
            ciudad: icity.name,
            comuna: idistrict.name,
            direccion: this.address,
            numero: this.house,
            password: this.password,
            password_confirmation: this.confirmPassword
          },
          this.occupation
        )
        .then(response => {
          this.sending = false;

          this.occupation = null;
          this.name = null;
          this.lastname = null;
          this.run = null;
          this.username = null;
          this.phone = null;
          this.birthdate = null;
          this.gender = null;
          this.region = null;
          this.city = null;
          this.district = null;
          this.address = null;
          this.house = null;
          this.password = null;
          this.confirmPassword = null;

          this.$v.$reset();
          this.showNotificationMessage("Usuario registrado con exito", {
            type: "success"
          });
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    onChangeLoadCities(event) {
      this.cities = cut.city(event);
      this.citiesDisabled = event === null;
      this.city = null;
    },

    onChangeLoadDistricts(event) {
      this.districts = cut.district(event);
      this.districtsDisabled = event === null;
      this.district = null;
    }
  },

  props: {
    themeColor: {
      type: String
    }
  },

  data: () => ({
    activities: [
      { code: config.USER_TYPE_ADMIN, name: "Administrador" },
      { code: config.USER_TYPE_SPECIALIST, name: "Especialista" },
      { code: config.USER_TYPE_PROVIDER, name: "Proovedor" },
      { code: config.USER_TYPE_RECEPTIONIST, name: "Recepcionista" }
    ],
    sending: false,
    occupation: null,
    name: null,
    lastname: null,
    run: null,
    username: null,
    phone: null,
    ocupation: null,
    birthdate: null,

    gender: null,
    genders: [
      { code: "M", name: "Masculino" },
      { code: "F", name: "Femenino" },
      { code: "O", name: "Otro" }
    ],

    region: null,
    regions: cut.regions,

    city: null,
    cities: cut.city(null),
    citiesDisabled: true,

    district: null,
    districts: cut.district(null),
    districtsDisabled: true,

    address: null,
    house: null,
    password: null,
    confirmPassword: null
  })
};

</script>

<style lang="scss" scoped>
  .md-radio {
    display: flex;
  }
</style>