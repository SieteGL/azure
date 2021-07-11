<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header>
            <h4 class="title">Ficha Técnica Paciente</h4>
            <p class="category">
              Ingrese los datos necesarios para su Ficha Técnica
            </p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-medium-size-100 md-size-100">
                    <p class="category">¿Usted Presenta Alguna Enfermedad?</p>
                    <md-radio v-model="disease" v-bind:value="true"
                      >Si</md-radio
                    >
                    <md-radio v-model="disease" v-bind:value="false"
                      >No</md-radio
                    >
                  </div>
                  <div
                    v-if="disease"
                    class="md-layout-item md-medium-size-100 md-size-100"
                  >
                    <md-field v-bind:class="vuelidate('diseaseType')">
                      <label>¿Que Tipo de Enfermedad?</label>
                      <md-input v-model="diseaseType" type="text"></md-input>
                    </md-field>
                  </div>
                </div>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <div class="md-layout md-gutter">
                  <div class="md-layout-item md-medium-size-100 md-size-100">
                    <p class="category">¿Usted Presenta Alguna Alergia?</p>
                    <md-radio v-model="allergy" v-bind:value="true">Si</md-radio>
                    <md-radio v-model="allergy" v-bind:value="false"
                      >No</md-radio
                    >
                  </div>
                  <div
                    v-if="allergy"
                    class="md-layout-item md-medium-size-100 md-size-100"
                  >
                    <md-field v-bind:class="vuelidate('allergyType')">
                      <label>¿Que Tipo de Alergia?</label>
                      <md-input v-model="allergyType" type="text"></md-input>
                    </md-field>
                  </div>
                  <!--
                  <div class="md-layout">
                    <div class="md-layout-item md-medium-size-100  md-size-35">
                      <md-field>
                        <label>Escriba si tiene más de una alergia</label>
                        <md-input type="text"></md-input>
                      </md-field>
                    </div>
                  </div>
                  -->
                </div>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-button class="md-primary md-block" v-on:click="submit"
                  >Enviar</md-button
                >
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
import config from "@/config/app";
import rules from "@/services/validations.js";

export default {
  validations: () =>
    rules([
      "clientDataSheetAllergyType as allergyType",
      "clientDataSheetDiseaseType as diseaseType"
    ]),

  methods: {
    submit() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos seleccionados");
        return;
      }

      // Aplicar si se quiere limpiar los colores de alerta de la pantalla
      this.$v.$reset();

      backend
        .clientDataSheet({
          enfermedad: this.disease,
          enfermedades: this.diseaseType,
          alergia: this.allergy,
          alergias: this.allergyType
        })
        .then(({ data }) => {
          this.disease = false;
          this.diseaseType = null;
          this.allergy = false;
          this.allergyType = null;

          this.showNotificationMessage("Ficha tecnica actualizada", {
            type: "success"
          });
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    }
  },

  watch: {
    disease(value) {
      if (!value) {
        this.diseaseType = null;
      }
    },
    allergy(value) {
      if (!value) {
        this.allergyType = null;
      }
    }
  },

  data: () => ({
    disease: false,
    diseaseType: null,

    allergy: false,
    allergyType: null
  })
};
</script>
