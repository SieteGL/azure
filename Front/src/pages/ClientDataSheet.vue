<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
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
                    <md-radio v-model="allergy" v-bind:value="true"
                      >Si</md-radio
                    >
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
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-button data-background-color="colorboton" class="md-primary md-block" v-on:click="submit"
                  >Enviar</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-button class="md-danger md-block" v-on:click="clear"
                  >Limpiar Formulario</md-button
                >
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="dataSheetUploaded.length">
                  <md-table class="ls--mtop-15px" v-model="dataSheetUploaded">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Enfermedad">{{
                        item.disease
                      }}</md-table-cell>
                      <md-table-cell md-label="Descripción de la enfermedad">{{
                        item.diseaseType
                      }}</md-table-cell>
                      <md-table-cell md-label="Alergia">{{
                        item.allergy
                      }}</md-table-cell>
                      <md-table-cell md-label="Descripción de la alergia">{{
                        item.allergyType
                      }}</md-table-cell>
                      <md-table-cell>
                        <md-button
                          v-on:click="edit(item)"
                          class="md-primary md-just-icon"
                        >
                          <md-icon>edit</md-icon>
                        </md-button>
                      </md-table-cell>
                    </md-table-row>
                  </md-table>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay documentos disponibles para visualizar
                  </h4>
                </div>
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

  mounted() {
    this.loadAllDataSheet();
  },

  methods: {
    submit() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos seleccionados");
        return;
      }

      if (this.sheetEdit === null) { this.submitCreate(); }
      else { this.submitEdit(); }

      // Aplicar si se quiere limpiar los colores de alerta de la pantalla
      this.$v.$reset();
    },

    submitCreate() {      
      backend
        .clientDataSheet({
          enfermedad: this.disease,
          enfermedades: this.diseaseType,
          alergia: this.allergy,
          alergias: this.allergyType
        },)
        .then(({ data }) => {          
          this.clear();
          this.loadAllDataSheet();
          this.showNotificationMessage("Ficha tecnica creada", {
            type: "success"
          });
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },
    submitEdit() {
      backend
        .clientEditDataSheet({
          enfermedad: this.disease,
          enfermedades: this.diseaseType,
          alergia: this.allergy,
          alergias: this.allergyType
        }, this.sheetEdit.id)
        .then(({ data }) => {          
          this.clear();
          this.loadAllDataSheet();
          this.showNotificationMessage("Ficha tecnica actualizada", {
            type: "success"
          });
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    clear() {
      this.sheetEdit = null;
      this.disease = false;
      this.diseaseType = null;
      this.allergy = false;
      this.allergyType = null;
    },

    edit(event) {
      const { original } = event;

      this.sheetEdit = original;

      this.disease = original.enfermedad === 'S';
      this.diseaseType = original.enfermedades === 'NO' ? null : original.enfermedades;
      this.allergy = original.alergia === 'S';
      this.allergyType = original.alergias === 'NO' ? null : original.alergias;
    },

    loadAllDataSheet() {
      backend.clientDataSheetLoadAll().then(({ data: { results } }) => {
        this.dataSheetUploaded = results.map(item => ({
          original: item,
          disease: item.enfermedad,
          diseaseType: item.enfermedades,
          allergy: item.alergia,
          allergyType: item.alergias
        }));
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
    sheetEdit: null,

    disease: false,
    diseaseType: null,

    allergy: false,
    allergyType: null,

    dataSheetUploaded: []
  })
};
</script>
