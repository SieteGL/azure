<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Procedimientos</h4>
            <p class="category">Ingrese información de sus Procedimientos</p>
          </md-card-header>
          <md-card-content>
            
            <div class="md-layout">     
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker
                  v-model="birthdate"
                  :class="vuelidate('birthdate')"
                  :md-model-type="String"
                  md-immediately
                >
                  <label>Fecha Procedimiento</label>
                </md-datepicker>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('gender')">
                  <label>Tipo De Procedimiento</label>
                  <md-select v-model="procedimiento">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in procedimientos"
                      :key="idx"
                      :value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
            </div>
            <br>
            <div class="md-layout-item md-medium-size-100  md-size-50">
                  <p class="category">Descripción del o los Procedimientos</p>
                </div>
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                    <md-field :class="vuelidate('name')">
                      <label>Ingrese Descripción</label>
                      <md-input v-model="name" type="text"></md-input>
                    </md-field>
                  </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="colorboton"
                  class="md-primary md-block"
                  v-on:click="submit"
                  :disabled="sending"
                  >Crea cliente</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="" v-on:click="clear" class="md-danger md-block">Limpiar Formulario</md-button>
              </div>
              <div
                v-if="sending"
                class="md-layout-item md-medium-size-100 md-size-100"
              >
                <md-progress-bar md-mode="indeterminate"></md-progress-bar>
              </div>
            </div>
            <div class="md-layout">
              <div
                class="md-layout-item md-medium-size-100 ls--create-account"
              ></div>
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
  validations: () =>
    rules([
      "occupation",
      "userManagerSpeciality as speciality",
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

  mounted() {
    backend
      .specialties()
      .then(specialties => {
        this.specialties = specialties;
      })
      .catch(error => {});
  },

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
            especialidades: this.speciality,
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

          this.clear();

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

    clear() {
      this.occupation = null;
      this.speciality = null;
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
    },

    onChangeOccupation(event) {
      if (event === config.USER_TYPE_SPECIALIST) {
        this.specialityDisplay = true;
      } else {
        this.speciality = null;
        this.specialityDisplay = false;
      }
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

    speciality: null,
    specialityDisplay: false,
    specialties: [],

    procedimiento: null,
    procedimientos: [
      { code: "F", name: "FRENILLOS" },
      { code: "R", name: "REVISION" },
      { code: "T", name: "TAPADURA" },
      { code: "E", name: "EXTRACCION" },
      { code: "C", name: "CORONA" },
      { code: "T", name: "TRATAMIENTO CONDUCTO" }

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
