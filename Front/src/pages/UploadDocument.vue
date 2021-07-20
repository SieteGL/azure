<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Ingreso De Documentos</h4>
            <p class="category">
              Ingrese los documentos necesarios para el beneficio Linda Sonrisa
            </p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <md-avatar class="md-large">
                  <!-- imagen -->
                </md-avatar>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50 md-size-50">
                <md-field>
                  <label>Seleccione Documento</label>
                  <md-select v-model="document">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in documents"
                      v-bind:key="idx"
                      v-bind:value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>

              <div class="md-layout-item md-medium-size-50 md-size-50">
                <md-field>
                  <label>Ingrese monto</label>
                  <md-input v-model="documentAmount" type="number"></md-input>
                  <span class="md-helper-text"
                    >Ingrese valor de su documento (AFP, Liquidación o
                    Finiquito)</span
                  >
                </md-field>
              </div>

              <div class="md-layout-item md-medium-size-100 md-size-100">
                <md-field>
                  <label>Cargar Documento</label>
                  <md-file
                    v-model="documentUploadName"
                    v-on:md-change="onFileUpload($event)"
                    accept="image/*"
                  />
                  <!-- <span class="md-helper-text">Cargar Documento</span> -->
                </md-field>
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="colorboton" class="md-primary md-block" v-on:click="submit"
                  >Guardar</md-button
                >
              </div>
              <!--
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-success md-block">Editar</md-button>
              </div>
              -->
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="documentsUploaded.length">
                  <md-table class="ls--mtop-15px" v-model="documentsUploaded">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Documento cargado">{{
                        item.document.name
                      }}</md-table-cell>
                      <md-table-cell md-label="Monto del documento">{{
                        item.amount
                      }}</md-table-cell>
                      <md-table-cell md-label="Acciones">
                        <md-button
                          class="md-primary md-just-icon"
                          target="_blank"
                          v-bind:href="item.uploaded"
                        >
                          <md-icon>search</md-icon>
                        </md-button>
                        <md-button
                          class="md-danger md-just-icon"
                          v-on:click="remove(item)"
                        >
                          <md-icon>delete</md-icon>
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
import cut from "@/services/cut.js";
import rules from "@/services/validations.js";
import config from "@/config/app";

export default {
  // validations: () =>
  //   rules([
  //     "occupation",
  //   ]),

  mounted() {
    this.loadUploadDocuments();
  },

  methods: {
    submit() {
      if (this.documentsUploaded.length) {
        this.$alert("Tiene que eliminar el archivo primero");
        return;
      }
      backend
        .uploadDocumentSave({
          documento: this.document,
          valor: this.documentAmount,
          imagen: this.documentUpload
        })
        .then(({ data }) => {
          this.document = null;
          (this.documentAmount = null),
            (this.documentUpload = null),
            (this.documentUploadName = null),
            this.loadUploadDocuments();
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    remove(event) {
      this.$confirm("Esta usted seguro?")
        .then(async () => {
          try {
            await backend.uploadDocumentRemove(event.original);

            this.documentsUploaded = [];
            this.showNotificationMessage("Documento eliminado con exito", {
              type: "success"
            });
          } catch (error) {
            if (error.name === "ValidationException") {
              throw error;
            }
            throw new ValidationException("Error al eliminar el documento");
          }
        })
        .catch(error => {
          if (typeof error === "undefined") {
            return;
          }

          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    onFileUpload(event) {
      this.documentUpload = event[0];
    },

    loadUploadDocuments() {
      backend.uploadDocument().then(({ data: { results } }) => {
        const [firstDocument = null] = results;

        if (firstDocument === null) return;

        this.documentsUploaded.push({
          original: firstDocument,
          document:
            this.documents.find(
              item => item.code === firstDocument.documento
            ) || {},
          amount: firstDocument.valor,
          uploaded: firstDocument.imagen
        });
      });
    }
  },

  data: () => ({
    document: null,
    documentAmount: null,
    documentUpload: null,
    documentUploadName: null,
    documents: [
      { code: "2", name: "AFP" },
      { code: "1", name: "Finiquito" },
      { code: "0", name: "Liquidación" }
    ],
    documentsUploaded: []
  })
};
</script>
