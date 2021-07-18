<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header>
            <h4 class="title">Almacen</h4>
            <p class="category">Filtros</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Codigo</label>
                  <md-input type="text"></md-input>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <!--
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Proveedor</label>
                  <md-input type="text"></md-input>
                </md-field>
              </div>
              -->
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Familia</label>
                  <md-input type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Servicio</label>
                  <md-input type="text"></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-datepicker v-bind:md-model-type="String" md-immediately>
                  <label>Fecha Vencimiento</label>
                </md-datepicker>
              </div>
              <div class="md-layout-item md-small-size-100 md-size-50">
                <md-field>
                  <label>Stock mayor a</label>
                  <md-input type="text"></md-input>
                </md-field>
              </div>

              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Stock menor a</label>
                  <md-input type="text"></md-input>
                </md-field>
              </div>
            </div>
            <div style="margin-top: 15px">
              <div class="md-layout">
                <div class="md-layout-item md-medium-size-50">
                  <md-button class="md-primary md-block">Filtrar</md-button>
                </div>
              </div>
              <div style="margin-top: 15px">
                <md-table>
                  <md-table-row>
                    <md-table-head md-numeric>Codigo</md-table-head>
                    <md-table-head>Familia</md-table-head>
                    <md-table-head>Producto</md-table-head>
                    <md-table-head>Descripcion</md-table-head>
                    <md-table-head>Fecha Vencimiento</md-table-head>
                    <md-table-head>Precio Compra</md-table-head>
                    <md-table-head>Precio Venta</md-table-head>
                    <md-table-head>Stock</md-table-head>
                    <md-table-head>Stock Critico</md-table-head>
                  </md-table-row>
                </md-table>
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

export default {};
</script>
