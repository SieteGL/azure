<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Filtros</h4>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Codigo Guia</label>
                  <md-input v-model="filterName" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Familia</label>
                  <md-input v-model="filterFamily" type="text"></md-input>
                </md-field>
              </div>
              <!--
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker :md-model-type="String" md-immediately>
                  <label>Fecha Compra desde</label>
                </md-datepicker>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker :md-model-type="String" md-immediately>
                  <label>Fecha Compra hasta</label>
                </md-datepicker>
              </div>
              -->
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-primary md-block" v-on:click="filter"
                  >Filtrar</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button class="md-info md-block" v-on:click="filterClear"
                    >Limpiar filtros</md-button
                >
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="orders.length">
                  <md-table class="ls--mtop-15px" v-model="orders">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Guía">{{
                        item.order
                      }}</md-table-cell>
                      <md-table-cell md-label="Producto">{{
                        item.name
                      }}</md-table-cell>
                      <md-table-cell md-label="Familia">{{
                        item.family
                      }}</md-table-cell>
                      <md-table-cell md-label="Descripcion">{{
                        item.description
                      }}</md-table-cell>
                      <md-table-cell md-label="Cantidad">{{
                        item.quantity
                      }}</md-table-cell>
                      <md-table-cell md-label="Precio">{{
                        item.price
                      }}</md-table-cell>
                      <md-table-cell md-label="Proveedor">{{
                        item.provider.name
                      }}</md-table-cell>
                      <md-table-cell>
                        <md-button
                          v-on:click="submit(item)"
                          class="md-icon-button md-dense md-success"
                        >
                          <md-icon>done</md-icon>
                        </md-button>                        
                      </md-table-cell>
                    </md-table-row>
                  </md-table>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay ordenes disponibles para visualizar
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
    this.loadProviders(() => {
      this.loadOrders();
    });
  },

  methods: {
    submit(order) {
      backend.makeReception(order.original).then(response => {
        this.showNotificationMessage("Prodcuto rececpcionado con exito", {
          type: "success"
        });
        this.loadOrders();
      });
    },

    filter() {
      const name =
        this.filterName !== null && this.filterName.length
          ? this.filterName
          : null;
      const family =
        this.filterFamily !== null && this.filterFamily.length
          ? this.filterFamily
          : null;

      this.filterOrders({ name, family });
    },

    filterClear() {
      this.filterName = null;
      this.filterFamily = null;
      this.filter();
    },

    filterOrders({ name = null, family = null } = {}) {
      this.orders = this.ordersOriginal.filter(item => {
        let ok = true;

        if (
          ok &&
          name !== null &&
          item.order.toLowerCase().indexOf(name.toLowerCase()) === -1
        ) {
          ok = false;
        }

        if (
          ok &&
          family !== null &&
          item.family.toLowerCase().indexOf(family.toLowerCase()) === -1
        ) {
          ok = false;
        }

        return ok;
      });
    },

    loadOrders() {
      backend.orders().then(({ data: { results } }) => {
        const complete = results
          .filter(item => !item.recepcionado)
          .map(item => ({
            original: item,
            order: item.ordenes.name,
            name: item.nombre_producto,
            family: item.familia,
            description: item.descripcion,
            quantity: Number(item.cantidad),
            price: Number(item.precio_unitario),
            provider: {
              ...this.loadSimpleProvider(item.proveedor)
            },
            vigency: item.fecha_vencimiento
          }));

        this.ordersOriginal = complete;
        this.filterOrders();
      });
    },

    loadProviders(callback = null) {
      backend.providers().then(({ data: { results } }) => {
        results.forEach(item => {
          this.providersDictionary[`ID:${item.id}`] = item;
        });
        if (callback !== null) callback();
      });
    },

    loadSimpleProvider(id) {
      const { nombre = null, apellido = null } = this.providersDictionary[
        `ID:${id}`
      ];

      return {
        id,
        name: `${nombre} ${apellido}`
      };
    }
  },

  data: () => ({
    filterName: null,
    filterFamily: null,

    orders: [],
    ordersOriginal: [],

    providersDictionary: {}
  })
};
</script>
