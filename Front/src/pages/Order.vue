<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Datos de Orden</h4>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field v-bind:class="vuelidate('product')">
                  <label>Producto</label>
                  <md-input v-model="product" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field v-bind:class="vuelidate('productFamily')">
                  <label>Familia</label>
                  <md-input v-model="productFamily" type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <md-field v-bind:class="vuelidate('productDescription')">
                  <label>Description</label>
                  <md-textarea v-model="productDescription"></md-textarea>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field v-bind:class="vuelidate('productQuantity')">
                  <label>Cantidad</label>
                  <md-input v-model="productQuantity" type="number"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field v-bind:class="vuelidate('productPrice')">
                  <span class="md-prefix">$</span>
                  <label>Precio Unitario</label>
                  <md-input v-model="productPrice" type="number"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field v-bind:class="vuelidate('provider')">
                  <label>Proveedor</label>
                  <md-select v-model="provider">
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in providers"
                      v-bind:key="idx"
                      v-bind:value="item.id"
                      >{{ item.nombre }} {{ item.apellido }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker
                  v-model="productVigency"
                  v-bind:class="vuelidate('productVigency')"
                  v-bind:md-model-type="String"
                  md-immediately
                >
                  <label>Fecha De Vencimiento</label>
                </md-datepicker>
              </div>
            </div>
            <div class="md-layout">
              <div
                class="md-layout-item md-medium-size-100 md-large-size-30 md-size-20"
              >
                <md-button data-background-color="colorboton" class="md-info md-block" v-on:click="addProduct"
                  >Añadir Producto</md-button
                >
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Orden</label>
                  <md-input v-model="orderName" type="text"></md-input>
                  <span class="md-helper-text">Ingrese nombre de orden</span>
                </md-field>
              </div>
              <div class="md-layout-item md-size-100">
                <div class="ls--separator"></div>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="productsAdded.length">
                  <md-table class="ls--mtop-15px" v-model="productsAdded">
                    <md-table-row slot="md-table-row" slot-scope="{ item }">
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
                    </md-table-row>
                  </md-table>
                  <div>
                    <h5>
                      El total de los productos es: <strong>{{ total }}</strong>
                    </h5>
                  </div>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay productos disponibles para visualizar
                  </h4>
                </div>
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-50">
                <md-button data-background-color="colorboton" class="md-primary md-block" v-on:click="submit"
                  >Generar Orden</md-button
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
  validations: () =>
    rules([
      "required as product",
      "required as productFamily",
      "required as productDescription",
      "required as productQuantity",
      "required as productPrice",
      "required as provider",
      "required as productVigency"
    ]),

  mounted() {
    this.loadProducts();
    this.loadProviders();
  },

  methods: {
    submit() {
      if (
        this.orderName === null ||
        !this.orderName.length ||
        !this.productsAdded.length
      ) {
        this.$alert("Debe ingresar el numero de orden y/o los productos");
        return;
      }

      backend
        .makeOrder(this.orderName, this.productsAdded)
        .then(response => {
          this.showNotificationMessage("Orden creada con exito", {
            type: "success"
          });
          this.clear();
          this.orderName = null;
          this.productsAdded = [];
          this.total = null;
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    clear() {
      this.product = null;
      this.productFamily = null;
      this.productDescription = null;
      this.productQuantity = null;
      this.productPrice = null;
      this.productVigency = null;
      this.provider = null;
    },

    totalUpdate() {
      let total = 0;
      this.productsAdded.forEach(item => {
        total += item.quantity * item.price;
      });

      this.total = total;
    },

    addProduct() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos seleccionados");
        return;
      }

      const provider = this.providers.find(item => item.id === this.provider);

      this.productsAdded.push({
        name: this.product,
        family: this.productFamily,
        description: this.productDescription,
        quantity: Number(this.productQuantity),
        price: Number(this.productPrice),
        provider: {
          id: provider.id,
          name: `${provider.nombre} ${provider.apellido}`
        },
        vigency: this.productVigency
      });

      this.$v.$reset();
      this.clear();
      this.totalUpdate();
    },

    loadProducts() {
      backend.products().then(({ data: { results } }) => {
        this.products = results.map(item => ({
          original: item,
          code: item.id,
          name: item.nombre_producto
        }));
      });
    },

    loadProviders() {
      backend.providers().then(({ data: { results } }) => {
        this.providers = results;
      });
    }
  },

  data: () => ({
    orderName: null,

    product: null,
    productFamily: null,
    productDescription: null,
    productQuantity: null,
    productPrice: null,
    productVigency: null,
    products: [],
    productsAdded: [],

    provider: null,
    providers: [],

    total: null
  })
};
</script>
