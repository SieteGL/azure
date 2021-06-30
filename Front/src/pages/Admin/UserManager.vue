<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header :data-background-color="themeColor">
            <h4 class="title">Employees Stats</h4>
            <p class="category">New employees on 15th September, 2016</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field :class="vuelidate('occupation')">
                  <label>Usuario</label>
                  <md-select v-model="occupation">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in collection.activities"
                      v-bind:key="idx"
                      :value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                  <span class="md-helper-text"
                    >Seleccione el tipo de usuario del sistema</span
                  >
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field :class="vuelidate('name')">
                  <label>Nombre</label>
                  <md-input v-model="name" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field :class="vuelidate('lastname')">
                  <label>Apellido</label>
                  <md-input v-model="lastname" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('run')">
                  <label>Rut</label>
                  <md-input v-model="run" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-50">
                <md-field :class="vuelidate('username')">
                  <label>Email</label>
                  <md-input v-model="username" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-50">
                <md-field :class="vuelidate('phone')">
                  <label>Contacto</label>
                  <span class="md-prefix">+56</span>
                  <md-input v-model="phone" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker
                  v-model="birthdate"
                  :class="vuelidate('birthdate')"
                  :md-model-type="String"
                  md-immediately
                >
                  <label>Fecha De Nacimiento</label>
                </md-datepicker>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('gender')">
                  <label>Genero</label>
                  <md-select v-model="gender">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in collection.genders"
                      v-bind:key="idx"
                      :value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('region')">
                  <label>Región</label>
                  <md-select
                    v-model="region"
                    @md-selected="onChangeLoadCities($event)"
                  >
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in collection.regions"
                      v-bind:key="idx"
                      :value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('city')">
                  <label>Provincia</label>
                  <md-select
                    v-model="city"
                    @md-selected="onChangeLoadDistricts($event)"
                    :disabled="collection.disabledCities"
                  >
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in collection.cities"
                      v-bind:key="idx"
                      :value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('district')">
                  <label>Comuna</label>
                  <md-select
                    v-model="district"
                    :disabled="collection.disabledDistricts"
                  >
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in collection.districts"
                      v-bind:key="idx"
                      :value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('address')">
                  <label>Dirección</label>
                  <md-input v-model="address" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('house')">
                  <label>Numero</label>
                  <span class="md-prefix">#</span>
                  <md-input v-model="house" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('password')">
                  <label>Password</label>
                  <md-input v-model="password" type="password"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field :class="vuelidate('confirmPassword')">
                  <label>Confirm Password</label>
                  <md-input
                    v-model="confirmPassword"
                    type="password"
                  ></md-input>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button
                  class="md-primary md-block"
                  v-on:click="submit"
                  :disabled="sending"
                  >Crea cliente</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-danger md-block">Cancelar</md-button>
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

      const {
        collection: { regions, cities, districts }
      } = this;

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
      this.collection.cities = cut.city(event);
      this.collection.disabledCities = event === null;
      this.city = null;
    },

    onChangeLoadDistricts(event) {
      this.collection.districts = cut.district(event);
      this.collection.disabledDistricts = event === null;
      this.district = null;
    }
  },

  props: {
    themeColor: {
      type: String
    }
  },

  data: () => ({
    collection: {
      regions: cut.regions,
      cities: cut.city(null),
      disabledCities: true,
      districts: cut.district(null),
      disabledDistricts: true,
      activities: [
        { code: config.USER_TYPE_ADMIN, name: "Administrador" },
        { code: config.USER_TYPE_SPECIALIST, name: "Especialista" },
        { code: config.USER_TYPE_PROVIDER, name: "Proovedor" },
        { code: config.USER_TYPE_RECEPTIONIST, name: "Recepcionista" }
      ],
      genders: [
        { code: "M", name: "Masculino" },
        { code: "F", name: "Femenino" },
        { code: "O", name: "Otro" }
      ]
    },
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
    region: null,
    city: null,
    district: null,
    address: null,
    house: null,
    password: null,
    confirmPassword: null
  })
};
</script>
