<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Listado Servicios</h4>
            <p class="category">Ingreso</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Nombre</label>
                  <md-input v-model="service" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Valor</label>
                  <md-input v-model="serviceAmount" type="number"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label for="movies">Lista de servicios</label>
                  <md-select v-model="serviceCollection" multiple>
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in services"
                      v-bind:key="idx"
                      v-bind:value="item.id"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-button data-background-color="colorboton" class="md-primary md-block" v-on:click="submit"
                  >Añadir Servicio</md-button
                >
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="servicesCreated.length">
                  <md-table class="ls--mtop-15px" v-model="servicesCreated">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Orden">{{
                        item.name
                      }}</md-table-cell>
                      <md-table-cell md-label="Producto">{{
                        item.amount
                      }}</md-table-cell>
                      <md-table-cell md-label="Descripción">{{
                        item.description
                      }}</md-table-cell>
                      <md-table-cell>
                        <md-button
                          v-on:click="deleteServiceCreated(item)"
                          class="md-icon-button md-dense md-danger"
                        >
                          <md-icon>delete</md-icon>
                        </md-button>
                      </md-table-cell>
                    </md-table-row>
                  </md-table>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay servicios disponibles para visualizar
                  </h4>
                </div>
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
      <div class="md-layout-item md-medium-size-100 md-size-33">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Crear Servicio</h4>
            <p class="category">Ingreso</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-size-100">
                <md-field>
                  <label>Nombre</label>
                  <md-input v-model="serviceNew" type="text"></md-input>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-size-100">
                <md-button data-background-color="colorboton"
                  class="md-primary md-block"
                  v-on:click="submitService"
                  >Crear Servicio</md-button
                >
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="services.length">
                  <md-table class="ls--mtop-15px" v-model="services">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Nombre del servicio">{{
                        item.name
                      }}</md-table-cell>
                      <md-table-cell>
                        <md-button
                          v-on:click="deleteService(item)"
                          class="md-icon-button md-dense md-danger"
                        >
                          <md-icon>delete</md-icon>
                        </md-button>
                      </md-table-cell>
                    </md-table-row>
                  </md-table>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay servicios disponibles para visualizar
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
    this.loadAllServices();
    this.loadAllServicesCreated();
  },

  methods: {
    submit() {
      backend
        .serviceCreate({
          name: this.service,
          amount: this.serviceAmount,
          collection: this.serviceCollection
        })
        .then(response => {
          this.clear();
          this.loadAllServicesCreated();
          this.showNotificationMessage("Servicio creado con exito", {
            type: "success"
          });
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    submitService() {
      backend
        .serviceNew(this.serviceNew)
        .then(response => {
          this.serviceNew = null;
          this.loadAllServices();
          this.showNotificationMessage("Servicio creado con exito", {
            type: "success"
          });
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    deleteServiceCreated(event) {
      this.$confirm("Esta usted seguro?")
        .then(async () => {
          await backend.serviceListDeleteCreated(event.original);
          this.loadAllServicesCreated();
        })
        .catch(error => {
          if (typeof error === "undefined") {
            return;
          }

          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    deleteService(event) {
      this.$confirm("Esta usted seguro?")
        .then(async () => {
          await backend.serviceListDelete(event.original);
          this.loadAllServices();
          this.loadAllServicesCreated();
        })
        .catch(error => {
          if (typeof error === "undefined") {
            return;
          }

          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    clear() {
      this.service = null;
      this.serviceAmount = null;
      this.serviceCollection = null;
    },

    loadAllServices() {
      backend.serviceList().then(({ data: { results } }) => {
        this.services = results.map(item => ({
          original: item,
          id: item.id,
          name: item.servicio
        }));
      });
    },
    loadAllServicesCreated() {
      backend.serviceListCreated().then(({ data: { results } }) => {
        this.servicesCreated = results.map(item => ({
          original: item,
          name: item.name,
          amount: item.valor_paquete,
          description: item.servicios_lista.map(it => it.servicio).join(", ")
        }));
      });
    }
  },
  data: () => ({
    service: null,
    serviceNew: null,
    serviceAmount: null,
    serviceCollection: [],

    services: [],
    servicesCreated: []
  })
};
</script>
