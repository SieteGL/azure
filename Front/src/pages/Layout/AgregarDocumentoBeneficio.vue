<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
             <md-card-header data-background-color="pruebacolor">
               <h4 class="title">Ingreso De Documentos</h4>
               <p class="category">Ingrese los documentos necesarios para el beneficio Linda Sonrisa</p>
             </md-card-header>
             <md-card-content>
               <!--Avatar de presentación-->
                <div>
                  <md-avatar class="md-large">
                    <img src="@/assets/img/fran.jpg" alt="People">
                  </md-avatar>                 
                </div>
                <br>
                <div class="md-layout-item md-medium-size-100  md-size-50">
                  <p class="category">Seleccione el Tipo de Documento</p>
                </div>
                <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-field :class="vuelidate('gender')"> <!--Preguntar como modificar el nombre "gender" para habilitarlo al documento-->
                      <label>Seleccione Documento</label> 
                      <md-select v-model="documento">
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in documentos"
                          v-bind:key="idx"
                          :value="item.code" 
                          >{{ item.name }}</md-option
                        >
                      </md-select>
                    </md-field>
                  </div>
                  <br>
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                  <p class="category">Ingrese valor de su documento (AFP, Liquidación o Finiquito)</p>
                </div>
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                    <md-field :class="vuelidate('lastname')">
                      <label>Ingrese monto</label>
                      <md-input v-model="lastname" type="text"></md-input>
                    </md-field>
                  </div>
                  <br>
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                  <p class="category">Cargar Documento</p>
                </div>
                <md-field>
                  <label>Multiple</label>
                    <md-file v-model="multiple" multiple />
                </md-field>
                <!--Se agregara campo cliente para ingresar el usuario-->
                <div class="md-layout-item md-medium-size-100 md-size-50">
                    <md-field :class="vuelidate('gender')"> <!--Preguntar como modificar el nombre "gender" para habilitarlo al documento-->
                      <label>Paciente/Usuario</label> 
                      <md-select v-model="usuario">
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in usuario"
                          v-bind:key="idx"
                          :value="item.code" 
                          >{{ item.name }}</md-option
                        >
                      </md-select>
                    </md-field>
                  </div>
               <div class="md-layout">
                 <div class="md-layout-item md-medium-size-50">
                   <md-button data-background-color="colorboton"
                  class="md-primary md-block"
                  v-on:click="submit"
                  :disabled="sending"
                  >Guardar</md-button>
                 </div>
               </div>
               <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100 ls--create-account">
                  </div>
               </div>
               <div class="md-layout">
                 <div class="md-layout-item md-medium-size-50">
                   <md-button data-background-color="colorboton"
                  class="md-primary md-block"
                  v-on:click="submit"
                  :disabled="sending"
                  >Editar</md-button>
                 </div>
               </div>
               <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100 ls--create-account">
                  </div>
               </div>

               <div class="md-layout">
                 <div class="md-layout-item md-medium-size-50">
                   <md-button data-background-color="colorboton"
                  class="md-primary md-block"
                  v-on:click="submit"
                  :disabled="sending"
                  >Limpiar</md-button>
                 </div>
               </div>
               <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100 ls--create-account">
                  </div>
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

  name: 'FileField',
    data: () => ({
      initial: 'vue-material-is-awesome.jpg',
      single: null,
      placeholder: null,
      disabled: null,
      multiple: null
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

    documento: null,
    documentos: [
      { code: "A", name: "AFP" },
      { code: "F", name: "Finiquito" },
      { code: "L", name: "Liquidación" }
    ],

    usuario: [
      { code: "A", name: "username" }
      
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
  .separator + .separator {
    margin-top: 24px;
  }
</style>