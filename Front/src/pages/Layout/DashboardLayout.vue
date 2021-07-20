<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <notifications class="ls--fixed-on-screen"></notifications>
    <side-bar
      :theme-color="themeColor"
      :theme-background-image="themeBackgroundImage"
    >
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link :to="{ name: 'dashboard' }">
        <md-icon>dashboard</md-icon>
        <p>HOME</p>
      </sidebar-link>
      <sidebar-link v-if="showAdminButton" :to="{ name: 'user-manager' }">
        <md-tooltip md-direction="right">Administrador de usuarios</md-tooltip>
        <md-icon>person</md-icon>
        <p>Usuarios</p>
      </sidebar-link>
      <sidebar-link v-if="showScheduleButton" :to="{ name: 'schedule' }">
        <md-icon>event</md-icon>
        <p>Agenda</p>
      </sidebar-link>
      <sidebar-link
        v-if="showAvailabilityButton"
        :to="{ name: 'availability' }"
      >
        <md-icon>event</md-icon>
        <p>Reserva De Hora</p>
      </sidebar-link>
      <sidebar-link
        v-if="showClientDataSheetButton"
        :to="{ name: 'client-data-sheet' }"
      >
        <md-icon>article</md-icon>
        <p>Ficha Técnica</p>
      </sidebar-link>
      <sidebar-link
        v-if="showUploadDocumentButton"
        :to="{ name: 'upload-document' }"
      >
        <md-icon>upload</md-icon>
        <p>Adjuntar Documentos</p>
      </sidebar-link>
      <sidebar-link v-if="showProceduresButton" :to="{ name: 'procedures' }">
        <md-icon>article</md-icon>
        <p>Procedimientos</p>
      </sidebar-link>
      <sidebar-link v-if="showReceptionButton" :to="{ name: 'reception' }">
        <md-icon>article</md-icon>
        <p>Recepción</p>
      </sidebar-link>
      <sidebar-link v-if="showWarehouseButton" :to="{ name: 'warehouse' }">
        <md-icon>article</md-icon>
        <p>Cargar Almacen</p>
      </sidebar-link>
      <sidebar-link
        v-if="showWarehouseViewButton"
        :to="{ name: 'warehouse-view' }"
      >
        <md-icon>article</md-icon>
        <p>Almacen</p>
      </sidebar-link>
      <sidebar-link v-if="showOrderButton" :to="{ name: 'order' }">
        <md-icon>article</md-icon>
        <p>Pedido</p>
      </sidebar-link>
      <sidebar-link v-if="showServicesButton" :to="{ name: 'services' }">
        <md-icon>article</md-icon>
        <p>Servicios</p>
      </sidebar-link>
      <sidebar-link v-if="showTicketButton" :to="{ name: 'ticket' }">
        <md-icon>article</md-icon>
        <p>Boleta</p>
      </sidebar-link>
      <sidebar-link :to="{ name: 'logout' }">
        <md-icon>logout</md-icon>
        <p>Cerrar sessión</p>
      </sidebar-link>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>
      <fixed-plugin
        :color.sync="themeColor"
        :image.sync="themeBackgroundImage"
      ></fixed-plugin>
      <dashboard-content :theme-color="themeColor"></dashboard-content>
      <content-footer v-if="!$route.meta.hideFooter"></content-footer>
    </div>
  </div>
</template>

<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "@/pages/Layout/MobileMenu.vue";
import FixedPlugin from "./Extra/FixedPlugin.vue";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    MobileMenu,
    FixedPlugin
  },

  beforeMount() {
    // { name: 'schedule' }          cliente, especialista, recepcionista
    // { name: 'availability' }      cliente,
    // { name: 'client-data-sheet' } cliente, especialista
    // { name: 'upload-document' }   cliente,
    // { name: 'procedures' }        especialista
    // { name: 'reception' }         recepcionista
    // { name: 'warehouse' }         recepcionista
    // { name: 'warehouse-view' }    recepcionista
    // { name: 'order' }             ???
    // { name: 'services' }          ???
    // { name: 'ticket' }            ???
    // { name: 'logout' }            ???

    const isAdmin = this.$settings.get("isAdmin", false);
    const isClient = this.$settings.get("isClient", false);
    const isEmployee = this.$settings.get("isEmployee", false);
    const isProvider = this.$settings.get("isProvider", false);
    const isSpecialist = this.$settings.get("isSpecialist", false);

    this.showAdminButton = isAdmin;
    this.showScheduleButton = isAdmin || isClient || isSpecialist || isEmployee;
    this.showAvailabilityButton = isAdmin || isClient;
    this.showClientDataSheetButton = isAdmin || isClient || isSpecialist;
    this.showUploadDocumentButton = isAdmin || isClient;
    this.showProceduresButton = isAdmin || isSpecialist;
    this.showReceptionButton = isAdmin || isEmployee;
    this.showWarehouseButton = isAdmin || isEmployee;
    this.showWarehouseViewButton = isAdmin || isEmployee;
    this.showOrderButton = isAdmin;
    this.showServicesButton = isAdmin;
    this.showTicketButton = isAdmin || isEmployee;

    this.themeColor = this.$settings.get("themeColor", "green");
  },

  data() {
    return {
      showAdminButton: false,
      showAvailabilityButton: false,
      showScheduleButton: false,
      showClientDataSheetButton: false,
      showUploadDocumentButton: false,
      showProceduresButton: false,
      showReceptionButton: false,
      showWarehouseButton: false,
      showWarehouseViewButton: false,
      showOrderButton: false,
      showServicesButton: false,
      showTicketButton: false,

      themeColor: "green",
      themeBackgroundImage: require("@/assets/img/sidebar-2.jpg")
    };
  }
};
</script>
