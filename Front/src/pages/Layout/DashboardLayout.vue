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
        <p>Dashboard</p>
      </sidebar-link>
      <sidebar-link v-if="showAdminButton" :to="{ name: 'user-manager' }">
        <md-tooltip md-direction="right">Administrador de usuarios</md-tooltip>
        <md-icon>person</md-icon>
        <p>Admin. de Usuarios</p>
      </sidebar-link>
      <sidebar-link :to="{ name: 'schedule' }">
        <md-icon>event</md-icon>
        <p>Agenda</p>
      </sidebar-link>
      <sidebar-link :to="{ name: 'availability' }">
        <md-icon>event</md-icon>
        <p>Ver Disponibilidad</p>
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
    this.showAdminButton = this.$settings.get("isAdmin", false);
    this.themeColor = this.$settings.get("themeColor", "green");
  },

  data() {
    return {
      showAdminButton: false,
      themeColor: "green",
      themeBackgroundImage: require("@/assets/img/sidebar-2.jpg")
    };
  }
};
</script>
