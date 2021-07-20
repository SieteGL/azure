<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header>
            <h4 class="title">Boleta N°</h4>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Empresa</label>
                  <md-select v-model="company">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in companies"
                      v-bind:key="idx"
                      v-bind:value="item.id"
                      >{{ item.name }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
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
                  <label>Almacen</label>
                  <md-select v-model="warehouse">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in warehouseList"
                      v-bind:key="idx"
                      v-bind:value="item.id"
                      >{{ item.code }}
                    </md-option>
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Especialista</label>
                  <md-select v-model="doctor">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in doctors"
                      v-bind:key="idx"
                      v-bind:value="item.id"
                      >{{ item.nombre }} {{ item.apellido }}
                    </md-option>
                  </md-select>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-size-100">
                <div class="ls--separator"></div>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Servicio</label>
                  <md-select v-model="service">
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
                <md-button
                  class="md-primary md-block"
                  v-on:click="submitService"
                  >Añadir Servicio</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-button class="md-danger md-block" v-on:click="clear"
                  >Limpiar Campos</md-button
                >
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="collection.length">
                  <md-table class="ls--mtop-15px" v-model="collection">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Servicio">{{
                        item.service
                      }}</md-table-cell>
                      <md-table-cell md-label="Total">{{
                        item.amount
                      }}</md-table-cell>
                    </md-table-row>
                  </md-table>
                  <div>
                    <h5>
                      El total de los servicios es: <strong>{{ total }}</strong>
                    </h5>
                  </div>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay ordenes disponibles para visualizar
                  </h4>
                </div>
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-primary md-block" v-on:click="submit"
                  >Generar Boleta</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-danger md-block" v-on:click="clearTicket"
                  >Cancelar Boleta</md-button
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
    this.loadDoctors();
    this.loadAllClients();
    this.loadAllCompanies();
    this.loadAllServices();
    this.loadAllWarehouse();
  },

  methods: {
    submit() {
      backend
        .ticketCreate({
          company: this.company,
          document: 1,
          doctor: this.doctor,
          client: this.client,
          warehouse: this.warehouse,
          services: this.collection
        })
        .then(response => {
          this.clear();
          this.collection = [];
          this.showNotificationMessage("Boleta creada con exito", {
            type: "success"
          });
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    submitService() {
      const service = this.services.find(item => item.id === this.service);

      this.collection.push({
        original: service,
        id: service.id,
        service: service.name,
        amount: service.amount
      });
      this.totalUpdate();
      this.service = null;
    },

    clear() {
      this.client = null;
      this.doctor = null;
      this.service = null;
      this.warehouse = null;
    },

    clearTicket() {
      this.$confirm("Esta usted seguro?")
        .then(async () => {
          this.clear();
          this.collection = [];
        })
        .catch(error => {
          if (typeof error === "undefined") {
            return;
          }
        });
    },

    totalUpdate() {
      let total = 0;
      this.collection.forEach(item => {
        total += item.amount;
      });

      this.total = total;
    },

    loadDoctors() {
      backend
        .doctors()
        .then(doctors => {
          this.doctors = doctors;
        })
        .catch(error => {});
    },

    loadAllClients() {
      backend.clients().then(clients => {
        clients.forEach(item => {
          this.clients.push({
            id: item.id,
            name: `${item.nombre} ${item.apellido}`
          });
        });
      });
    },

    loadAllCompanies() {
      backend.companies().then(({ data: { results } }) => {
        this.companies = results.map(item => ({
          original: item,
          id: item.id,
          name: item.nombre_empresa
        }))
      });
    },

    loadAllServices() {
      backend.serviceListCreated().then(({ data: { results } }) => {
        this.services = results.map(item => ({
          original: item,
          id: item.id,
          name: item.name,
          amount: item.valor_paquete
        }));
      });
    },

    loadAllWarehouse() {
      backend.warehouseFilterList().then(({ data: { results } }) => {
        this.warehouseList = results.map(item => ({
          original: item,
          id: item.id,
          code: item.codigo
        }));
      });
    }
  },

  data: () => ({
    total: null,

    client: null,
    company: null,
    doctor: null,
    service: null,
    warehouse: null,

    clients: [],
    companies: [],
    doctors: [],
    services: [],
    warehouseList: [],

    collection: []
  })
};
</script>
