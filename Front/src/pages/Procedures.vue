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
                      v-bind:value="item.id"
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
                  >{{
                    procedureEdit === null ? "Agregar" : "Editar"
                  }}
                  procedimiento</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-danger md-block" v-on:click="clear"
                  >Limpiar Formulario</md-button
                >
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="proceduresLoaded.length">
                  <md-table class="ls--mtop-15px" v-model="proceduresLoaded">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Documento cargado">{{
                        item.client.name
                      }}</md-table-cell>
                      <md-table-cell md-label="Monto del documento">{{
                        item.procedure.name
                      }}</md-table-cell>
                      <md-table-cell md-label="Monto del documento">{{
                        item.description
                      }}</md-table-cell>
                      <md-table-cell>
                        <md-button
                          v-on:click="loadEdit(item)"
                          class="md-primary md-just-icon"
                        >
                          <md-icon>edit</md-icon>
                        </md-button>
                        <md-button
                          v-on:click="remove(item)"
                          class="md-danger md-just-icon"
                        >
                          <md-icon>delete</md-icon>
                        </md-button>
                      </md-table-cell>
                    </md-table-row>
                  </md-table>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay procedimientos disponibles para visualizar
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
  mounted() {
    this.loadAllClients(() => {
      this.loadProcedures();
    });
  },

  methods: {
    submit() {
      if (this.procedureEdit === null) this.submitCreate();
      else this.submitEdit();
    },

    submitCreate() {
      backend
        .procedureSave({
          client: this.client,
          procedure: this.procedure,
          description: this.procedureDescription
        })
        .then(response => {
          this.clear();
          this.showNotificationMessage("Procedimiento guardado con exito", {
            type: "success"
          });
          this.loadProcedures();
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },
    submitEdit() {
      backend
        .procedureEdit({
          id: this.procedureEdit.id,
          client: this.client,
          procedure: this.procedure,
          description: this.procedureDescription
        })
        .then(response => {
          this.clear();
          this.showNotificationMessage("Procedimiento editado con exito", {
            type: "success"
          });
          this.loadProcedures();
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    remove(event) {
      this.$confirm("Esta usted seguro?")
        .then(async () => {
          await backend.procedureDelete(event.original);
          this.procedureEdit = null;
          this.loadProcedures();
        })
        .catch(error => {
          if (typeof error === "undefined") {
            return;
          }

          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    clear() {
      this.client = null;
      this.procedure = null;
      this.procedureEdit = null;
      this.procedureDescription = null;
    },

    loadEdit(event) {
      const { original } = event;

      this.client = original.cliente;
      this.procedure = original.tipo_procedimiento;
      this.procedureEdit = original;
      this.procedureDescription = original.descripcion_procedimiento;
    },

    loadAllClients(callback = null) {
      backend.clients().then(clients => {
        clients.forEach(item => {
          this.clients.push({
            id: item.id,
            name: `${item.nombre} ${item.apellido}`
          });
          this.clientsDictionary[`ID:${item.id}`] = item;
        });
        if (callback !== null) callback();
      });
    },

    loadProcedures() {
      backend.procedureSaved().then(({ data: { results } }) => {
        this.proceduresLoaded = results.map(item => ({
          original: item,
          client: this.loadSimpleClient(item.cliente),
          procedure: this.loadSimpleProcedure(item.tipo_procedimiento),
          description: item.descripcion_procedimiento
        }));
      });
    },

    loadSimpleClient(id) {
      const { nombre = null, apellido = null } = this.clientsDictionary[
        `ID:${id}`
      ];

      return {
        id,
        name: `${nombre} ${apellido}`
      };
    },

    loadSimpleProcedure(code) {
      const procedure = this.procedures.find(
        item => Number(item.code) === Number(code)
      );

      return {
        code,
        name: procedure.name
      };
    }
  },

  data: () => ({
    client: null,
    clients: [],
    clientsDictionary: {},

    procedure: null,
    procedureEdit: null,
    procedureDescription: null,
    procedures: [
      { code: "0", name: "Odontologo General" },
      { code: "1", name: "Ortodoncista" },
      { code: "2", name: "Radiologo" },
      { code: "3", name: "Prostodoncista" }
    ],
    proceduresLoaded: []

    // procedures: [
    //   { code: "F", name: "FRENILLOS" },
    //   { code: "R", name: "REVISION" },
    //   { code: "T", name: "TAPADURA" },
    //   { code: "E", name: "EXTRACCION" },
    //   { code: "C", name: "CORONA" },
    //   { code: "T", name: "TRATAMIENTO CONDUCTO" }
    // ]
  })
};
</script>
