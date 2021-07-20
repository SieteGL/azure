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
              <!--
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Familia</label>
                  <md-input v-model="filterFamily" type="text"></md-input>
                </md-field>
              </div>
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
                <md-button  data-background-color="colorboton" class="md-primary md-block" v-on:click="filter"
                  >Filtrar</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="red" class="md-info md-block" v-on:click="filterClear"
                  >Limpiar filtros</md-button
                >
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="orders.length">
                  <md-table class="ls--mtop-15px" v-model="orders">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Orden">{{
                        item.order
                      }}</md-table-cell>
                      <md-table-cell md-label="Producto">{{
                        item.name
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
                      <md-table-cell md-label="Total">{{
                        item.total
                      }}</md-table-cell>
                      <md-table-cell>
                        <md-button
                          v-on:click="submit(item)"
                          class="md-just-icon md-success"
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
    this.loadOrders();
  },

  methods: {
    submit(order) {
      backend
        .storeReception(order.original)
        .then(response => {
          this.showNotificationMessage("Producto almacenado con exito", {
            type: "success"
          });
          this.loadOrders();
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    filter() {
      const name =
        this.filterName !== null && this.filterName.length
          ? this.filterName
          : null;

      this.filterOrders({ name });
    },

    filterClear() {
      this.filterName = null;
      this.filter();
    },

    filterOrders({ name = null } = {}) {
      this.orders = this.ordersOriginal.filter(item => {
        let ok = true;

        if (
          ok &&
          name !== null &&
          item.order.toLowerCase().indexOf(name.toLowerCase()) === -1
        ) {
          ok = false;
        }

        return ok;
      });
    },

    loadOrders() {
      backend.receptions().then(({ data: { results } }) => {
        console.log(results);
        const complete = results.map(item => {
          const detail = item.detalles_recepcion;
          return {
            original: item,
            order: detail.ordenes.name,
            name: detail.nombre_producto,
            description: detail.descripcion,
            quantity: Number(detail.cantidad),
            price: Number(detail.precio_unitario),
            total: Number(detail.total)
          };
        });

        this.ordersOriginal = complete;
        this.filterOrders();
      });
    }
  },

  data: () => ({
    filterName: null,
    filterFamily: null,

    orders: [],
    ordersOriginal: []
  })
};
</script>
