<template>
      <div class="ls--login-background ls--login-background-1">
    <div class="ls--login-wrapper">
      <notifications class="ls--fixed-on-screen"></notifications>
      <div class="content">
        <div class="md-layout md-alignment-center-center ls--min-height-100vh">
          <div
            class="md-layout-item md-xsmall-size-100 md-small-size-80 md-medium-size-40 md-large-size-40 md-xlarge-size-30"
          >
            <md-card>
              <md-card-header data-background-color="pruebacolor">
                <h4 class="title">Inicio Sesión</h4>
                <p class="category">Ingrese sus datos</p>
              </md-card-header>
              <md-card-content>
                <div class="md-layout"> 
                  <div class="md-layout-item md-medium-size-100 md-size-100"> <!-- el largo del campo de texto -->
                    <md-field :class="vuelidate('username')"> <!-- Campo donde se registrara el email -->
                      <label>Email</label>
                      <md-input v-model="username" type="text"></md-input>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100 md-size-100">
                    <md-field :class="vuelidate('password')">
                      <label>Password</label>
                      <md-input v-model="password" type="password"></md-input>
                    </md-field>
                  </div>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100">
                    <md-button data-background-color="colorboton"
                      class="md-primary md-block"
                      v-on:click="submit"
                      :disabled="sending"
                      >Iniciar sesión</md-button
                    >
                  </div>
                </div>
                <div v-if="sending" class="md-layout">
                  <div class="md-layout-item md-medium-size-100">
                    <md-progress-bar md-mode="indeterminate"></md-progress-bar>
                  </div>
                </div>
                <div class="md-layout">
                  <div
                    class="md-layout-item md-medium-size-100 ls--create-account"
                  >
                    <router-link 
                      :to="{ name: 'register' }"
                      class="ls--create-account-size"
                      >Crear cuenta de usuario</router-link>
                    
                  </div>
                </div>
              </md-card-content>
            </md-card>
          </div>
        </div>
      </div>
    </div>
    <div class="ls--footer">
    <footer  class="footer">
      <p> Clínica Dental Linda Sonrisa © Todos los derechos reservados /  Calle Nueva 1660, Huechuraba, Región Metropolitana.</p> 
    </footer>
    </div>
  </div>
   
</template>


<script>
import backend from "@/services/backend.js";
import rules from "@/services/validations.js";
import Token from "@/services/Token.js";

export default {
  validations: () => rules(["username", "required as password"]),
  methods: {
    submit() {
      this.$v.$touch();

      if (this.$v.$invalid) {
        this.showNotificationMessage("Debe completar los campos seleccionados");
        return;
      }

      this.sending = true;
      backend
        .login(this.username, this.password)
        .then(async tokens => {
          const token = new Token(tokens);
          const user = await token.store().contentData();
 
          this.$settings.set("isAdmin", user.is_superuser);
          this.$settings.set("isSpecialist", user.is_esp);
          this.$settings.set("isClient", user.is_cli);
          this.$settings.set("isProvider", user.is_pro);
          this.$settings.set("isEmployee", user.is_emp);

          this.$router.push("/dashboard");
        })
        .catch(error => {
          this.sending = false;
          this.showNotificationMessage(
            "Ha ingresado un nombre de usuario o contraseña inválido"
          );
        });
    }
  },
  data() {
    return {
      sending: false,
      username: null,
      password: null
    };
  }
};
</script>
