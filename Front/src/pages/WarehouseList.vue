<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Almacen</h4>
            <p class="category">Filtros</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Codigo</label>
                  <md-input v-model="filterCode" type="text"></md-input>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Familia</label>
                  <md-input v-model="filterFamily" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker
                  v-model="filterDate"
                  v-bind:md-model-type="String"
                  md-immediately
                >
                  <label>Fecha Vencimiento</label>
                </md-datepicker>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-50">
                <md-field>
                  <label>Stock mayor a</label>
                  <md-input v-model="filterStockMin" type="number"></md-input>
                </md-field>
              </div>

              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Stock menor a</label>
                  <md-input v-model="filterStockMax" type="number"></md-input>
                </md-field>
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="colorboton" class="md-primary md-block" v-on:click="filter"
                  >Filtrar</md-button
                >
              </div>
              <div class="md-layout-item md-medium-size-50">
                <md-button  data-background-color="red" class="md-info md-block" v-on:click="filterClear"
                  >Limpiar filtros</md-button
                >
              </div>
            </div>

            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="warehouse.length">
                  <md-table class="ls--mtop-15px" v-model="warehouse">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
                      <md-table-cell md-label="Codigo">{{
                        item.code
                      }}</md-table-cell>
                      <md-table-cell md-label="Producto">{{
                        item.name
                      }}</md-table-cell>
                      <md-table-cell md-label="Familia">{{
                        item.family
                      }}</md-table-cell>
                      <md-table-cell md-label="Fecha de vencimiento">{{
                        item.vigency
                      }}</md-table-cell>
                      <md-table-cell md-label="Stock">{{
                        item.stock
                      }}</md-table-cell>
                      <md-table-cell md-label="Stock critico">{{
                        item.critical
                      }}</md-table-cell>
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
    this.loadAll();
  },

  methods: {
    filter() {
      const code =
        this.filterCode !== null && this.filterCode.length
          ? this.filterCode
          : null;
      const family =
        this.filterFamily !== null && this.filterFamily.length
          ? this.filterFamily
          : null;

      const stockMin =
        this.filterStockMin !== null && this.filterStockMin.length
          ? Number(this.filterStockMin)
          : null;

      const stockMax =
        this.filterStockMax !== null && this.filterStockMax.length
          ? Number(this.filterStockMax)
          : null;

      const date =
        this.filterDate !== null && this.filterDate.length
          ? Date.parse(this.filterDate)
          : null;

      this.filterWarehouse({ code, family, stockMin, stockMax, date });
    },

    filterClear() {
      this.filterCode = null;
      this.filterDate = null;
      this.filterFamily = null;
      this.filterStockMin = null;
      this.filterStockMax = null;

      this.filter();
    },

    filterWarehouse({
      code = null,
      family = null,
      stockMin = null,
      stockMax = null,
      date = null
    } = {}) {
      this.warehouse = this.warehouseOriginal.filter(item => {
        if (
          code !== null &&
          item.code.toLowerCase().indexOf(code.toLowerCase()) === -1
        ) {
          return false;
        }
        if (
          family !== null &&
          item.family.toLowerCase().indexOf(family.toLowerCase()) === -1
        ) {
          return false;
        }
        if (stockMin !== null && stockMin > item.stock) {
          return false;
        }
        if (stockMax !== null && stockMax < item.stock) {
          return false;
        }
        if (date !== null && date !== item.vigencyDate) {
          return false;
        }

        return true;
      });
    },

    loadAll() {
      backend.warehouseFilterList().then(({ data: { results } }) => {
        this.warehouseOriginal = results.map(item => ({
          original: item,
          code: item.codigo,
          name: item.nombre_producto,
          family: item.familia,
          vigency: item.fecha_vencimiento,
          vigencyDate: Date.parse(item.fecha_vencimiento),
          stock: item.stock,
          critical: item.stock_critico
        }));
        this.filterWarehouse();
      });
    }
  },

  data: () => ({
    filterCode: null,
    filterDate: null,
    filterFamily: null,
    filterStockMin: null,
    filterStockMax: null,

    warehouse: [],
    warehouseOriginal: []
  })
};
</script>
