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
                <h4 class="title">Contáctanos</h4>
                <p class="category">Aquí va un formulario para contactar</p>
              </md-card-header>
              
                
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
