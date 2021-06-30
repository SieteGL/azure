<template>
  <div class="ls--login-background ls--login-background-3">
    <div class="ls--login-wrapper">
      <notifications class="ls--fixed-on-screen"></notifications>
      <div class="content">
        <div class="md-layout md-alignment-top-center">
          <div class="md-layout-item md-medium-size-100 md-size-33">
            <md-card>
              <md-card-header data-background-color="green">
                <h4 class="title">Registro</h4>
                <p class="category">Completa tu registro</p>
              </md-card-header>
              <md-card-content>
                <div class="md-layout">
                  <div class="md-layout-item md-small-size-100 md-size-100">
                    <md-field :class="vuelidate('username')">
                      <label>Email</label>
                      <md-input v-model="username" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-field :class="vuelidate('password')">
                      <md-tooltip md-direction="top"
                        >Debe contener numero, <br />
                        mayuscula, minuscula <br />y un caracter
                        !@#$%^&#38;*</md-tooltip
                      >
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
                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <md-field :class="vuelidate('name')">
                      <label>Nombre</label>
                      <md-input v-model="name" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <md-field :class="vuelidate('lastname')">
                      <label>Apellido</label>
                      <md-input v-model="lastname" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-33">
                    <md-field :class="vuelidate('run')">
                      <label>Rut</label>
                      <md-input v-model="run" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-33">
                    <md-tooltip md-direction="top"
                      >Fecha de nacimiento</md-tooltip
                    >
                    <md-datepicker
                      v-model="birthdate"
                      :class="vuelidate('birthdate')"
                      :md-model-type="String"
                      md-immediately
                    >
                      <label>Fecha De Nac.</label>
                    </md-datepicker>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-33">
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
                  <div class="md-layout-item md-medium-size-100 md-size-100">
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
                  <div class="md-layout-item md-medium-size-100 md-size-70">
                    <md-field :class="vuelidate('address')">
                      <label>Dirección</label>
                      <md-input v-model="address" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-30">
                    <md-field :class="vuelidate('house')">
                      <label>Número</label>
                      <span class="md-prefix">#</span>
                      <md-input v-model="house" type="text"></md-input>
                    </md-field>
                  </div>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100">
                    <md-button
                      class="md-primary md-block"
                      v-on:click="submit"
                      :disabled="sending"
                      >Crea tu cuenta</md-button
                    >
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
                  >
                    <router-link
                      :to="{ name: 'login' }"
                      class="ls--create-account-size"
                      >volver a iniciar sesión</router-link
                    >
                  </div>
                </div>
              </md-card-content>
            </md-card>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import backend from "@/services/backend.js";
import cut from "@/services/cut.js";
import rules from "@/services/validations.js";

export default {
  validations: () =>
    rules([
      "name",
      "lastname",
      "run",
      "username",
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
    onChangeLoadCities(event) {
      this.collection.cities = cut.city(event);
      this.collection.disabledCities = event === null;
      this.city = null;
    },

    onChangeLoadDistricts(event) {
      this.collection.districts = cut.district(event);
      this.collection.disabledDistricts = event === null;
      this.district = null;
    },

    submit() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos seleccionados");
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
        .register({
          email: this.username,
          rut: this.run,
          password: this.password,
          password_confirmation: this.confirmPassword,
          nombre: this.name,
          apellido: this.lastname,
          sexo: this.gender,
          fecha_nacimiento: this.birthdate,
          region: iregion.name,
          ciudad: icity.name,
          comuna: idistrict.name,
          direccion: this.address,
          numero: this.house
        })
        .then(response => {
          this.sending = false;

          this.username = null;
          this.password = null;
          this.confirmPassword = null;
          this.name = null;
          this.lastname = null;
          this.run = null;
          this.birthdate = null;
          this.gender = null;
          this.region = null;
          this.city = null;
          this.district = null;
          this.address = null;
          this.house = null;

          this.$v.$reset();
          this.showNotificationMessage("Usuario registrado con exito", {
            type: "success"
          });
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    }
  },
  data() {
    return {
      collection: {
        regions: cut.regions,
        cities: cut.city(null),
        disabledCities: true,
        districts: cut.district(null),
        disabledDistricts: true,
        genders: [
          { code: "M", name: "Masculino" },
          { code: "F", name: "Femenino" },
          { code: "O", name: "Otro" }
        ]
      },
      sending: false,
      username: null,
      password: null,
      confirmPassword: null,
      name: null,
      lastname: null,
      run: null,
      birthdate: null,
      gender: null,
      region: null,
      city: null,
      district: null,
      address: null,
      house: null
    };
  }
};
</script>
