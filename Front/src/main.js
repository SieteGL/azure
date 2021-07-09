// =========================================================
// * Vue Material Dashboard - v1.4.0
// =========================================================
//
// * Product Page: https://www.creative-tim.com/product/vue-material-dashboard
// * Copyright 2019 Creative Tim (https://www.creative-tim.com)
// * Licensed under MIT (https://github.com/creativetimofficial/vue-material-dashboard/blob/master/LICENSE.md)
//
// * Coded by Creative Tim
//
// =========================================================
//
// * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from "vue";
import VueSimpleAlert from "vue-simple-alert";
import Vuelidate from "vuelidate";
import VueRouter from "vue-router";
import App from "./App";
import storage from "./services/storage";
import routes from "./routes/routes";
import GlobalComponents from "./ins-components";
import GlobalDirectives from "./ins-directives";
import GlobalHelpers from "./ins-helpers";
import Notifications from "./components/NotificationPlugin";
import MaterialDashboard from "./material-dashboard";
import Chartist from "chartist";
import Settings from "./services/Settings.js";

Vue.prototype.$settings = Settings.load();

// configure router
const router = new VueRouter({
  routes,
  linkExactActiveClass: "nav-item active"
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some(record => record.meta.requiresAuth) &&
    storage.get("token") === null
  ) {
    next({ name: "login" });
  } else {
    next();
  }
});

Vue.prototype.$Chartist = Chartist;

Vue.use(Vuelidate);
Vue.use(VueRouter);
Vue.use(MaterialDashboard);
Vue.use(GlobalComponents);
Vue.use(GlobalDirectives);
Vue.use(GlobalHelpers);
Vue.use(Notifications);
Vue.use(VueSimpleAlert, {
  confirmButtonText: "Aceptar",
  cancelButtonText: "Cancelar"
});

// Datepicker locale
const { material: datepicker } = Vue;
datepicker.locale = {
  ...datepicker.locale,
  // i18n strings
  days: [
    "Domingo",
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado"
  ],
  shortDays: ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"],
  shorterDays: ["D", "L", "M", "X", "J", "V", "S"],
  months: [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
  ],
  shortMonths: [
    "Ene",
    "Feb",
    "Mar",
    "Abr",
    "May",
    "Jun",
    "Jul",
    "Ago",
    "Sep",
    "Oct",
    "Nov",
    "Dic"
  ],
  shorterMonths: ["E", "F", "Mz", "A", "M", "Jn", "J", "A", "S", "O", "N", "D"]
};

/* eslint-disable no-new */
new Vue({
  el: "#app",
  render: h => h(App),
  router,
  data: {
    Chartist: Chartist
  }
});
