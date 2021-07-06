<template>
  <div class="ls--login-background ls--login-background-3">
    <div class="ls--login-wrapper">
      <notifications class="ls--fixed-on-screen"></notifications>
      <div class="content">
        <div class="md-layout md-alignment-center-center ls--min-height-100vh">
          <div
            class="md-layout-item md-xsmall-size-100 md-small-size-80 md-medium-size-50 md-large-size-50 md-xlarge-size-40"
          >
            <md-card>
              <md-card-header data-background-color="pruebacolor">
                <h4 class="title">Registro</h4>
                <p class="category">Completa tu registro</p>
              </md-card-header>
              <md-card-content>
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
                      <label>RUN</label>
                      <md-input v-model="run" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-field :class="vuelidate('username')">
                      <label>Email</label>
                      <md-input v-model="username" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-field :class="vuelidate('gender')">
                      <label>Genero</label>
                      <md-select v-model="gender">
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in genders"
                          v-bind:key="idx"
                          :value="item.code"
                          >{{ item.name }}</md-option
                        >
                      </md-select>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-datepicker
                      v-model="birthdate"
                      :class="vuelidate('birthdate')"
                      :md-model-type="String"
                      :md-disabled-dates="disabledDates"
                      md-immediately
                    >
                      <label>Fecha De Nacimiento</label>
                    </md-datepicker>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-field :class="vuelidate('phone')">
                      <label>Contacto</label>
                      <span class="md-prefix">+56</span>
                      <md-input v-model="phone" type="text"></md-input>
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
                          v-for="(item, idx) in regions"
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
                        :disabled="citiesDisabled"
                      >
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in cities"
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
                        :disabled="districtsDisabled"
                      >
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in districts"
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
                      <label>Número</label>
                      <span class="md-prefix">#</span>
                      <md-input v-model="house" type="text"></md-input>
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
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100">
                    <md-button data-background-color="colorboton"
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

    disabledDates(date) {
      const current = new Date();

      date.setHours(0, 0, 0, 0);
      current.setHours(0, 0, 0, 0);

      return date > current;
    },

    submit() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos seleccionados");
        return;
      }

      const { regions, cities, districts } = this;

      const iregion = regions.find(item => item.code === this.region);
      const icity = cities.find(item => item.code === this.city);
      const idistrict = districts.find(item => item.code === this.district);

      this.sending = true;
      backend
        .register({
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
        })
        .then(response => {
          this.sending = false;

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
    }
  },
  data() {
    return {
      sending: false,

      name: null,
      lastname: null,
      run: null,
      username: null,
      phone: null,
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
    };
  }
};
</script>
