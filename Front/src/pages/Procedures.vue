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
                <md-field>
                  <label>Cliente</label>
                  <md-select v-model="client">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in clients"
                      v-bind:key="idx"
                      v-bind:value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Tipo De Procedimiento</label>
                  <md-select v-model="procedure">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in procedures"
                      v-bind:key="idx"
                      v-bind:value="item.code"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-100">
                <md-field>
                  <label>Describa su procediimiento</label>
                  <md-textarea v-model="procedureDescription"></md-textarea>
                  <span class="md-helper-text"
                    >Descripción del o los Procedimientos</span
                  >
                </md-field>
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-primary md-block" v-on:click="submit"
                  >Agregar</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-danger md-block" v-on:click="clear"
                  >Limpiar Formulario</md-button
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
import cut from "@/services/cut.js";
import rules from "@/services/validations.js";
import config from "@/config/app";

export default {
  mounted() {
    this.loadAllClients();
  },

  methods: {
    submit() {
      backend
        .procedureSave({
          client: this.client,
          procedure: this.procedure,
          description: this.procedureDescription
        })
        .then(() => {
          this.clear();
          this.showNotificationMessage("Procedimiento guardado con exito", {
            type: "success"
          });
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    clear() {
      this.client = null;
      this.procedure = null;
      this.procedureDescription = null;
    },

    loadAllClients() {
      backend.clients().then(clients => {
        this.clients = clients.map(item => ({
          code: item.email,
          name: `${item.nombre} ${item.apellido}`
        }));
      });
    }
  },

  data: () => ({
    client: null,
    clients: [],

    procedure: null,
    procedureDescription: null,
    procedures: [
      { code: "0", name: "Odontologo General" },
      { code: "1", name: "Ortodoncista" },
      { code: "2", name: "Radiologo" },
      { code: "3", name: "Prostodoncista" }
    ]
  })
};
</script>
