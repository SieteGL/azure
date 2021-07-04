import Content from "@/pages/Layout/Content.vue";
import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";
import Dashboard from "@/pages/Dashboard.vue";
import Availability from "@/pages/Availability.vue";
import Schedule from "@/pages/Schedule.vue";
import Login from "@/pages/Auth/Login.vue";
import Register from "@/pages/Auth/Register.vue";
import UserManager from "@/pages/Admin/UserManager.vue";
import storage from "@/services/storage.js";

const routes = [
  {
    path: "/auth",
    component: Content,
    children: [
      {
        path: "login",
        name: "login",
        component: Login
      },
      {
        path: "logout",
        name: "logout",
        beforeEnter: (to, from, next) => {
          storage.clear();
          next({ name: "login" });
        }
      },
      {
        path: "register",
        name: "register",
        component: Register
      }
    ]
  },
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "dashboard",
        meta: {
          title: "Dashboard",
          hideFooter: true,
          requiresAuth: true
        },
        component: Dashboard
      },
      {
        path: "admin/user-manager",
        name: "user-manager",
        meta: {
          title: "Administrador de usuarios",
          hideFooter: true,
          requiresAuth: true
        },
        component: UserManager
      },
      {
        path: "schedule",
        name: "schedule",
        meta: {
          title: "Crear agenda",
          hideFooter: true,
          requiresAuth: true
        },
        component: Schedule
      },
      {
        path: "availability",
        name: "availability",
        meta: {
          title: "Disponibilidad de horas",
          hideFooter: true,
          requiresAuth: true
        },
        component: Availability
      }
    ]
  }
];

export default routes;
