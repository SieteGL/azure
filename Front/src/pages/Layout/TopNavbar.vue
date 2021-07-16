<template>
  <md-toolbar md-elevation="0" class="md-transparent">
    <div class="md-toolbar-row">
      <div class="md-toolbar-section-start">
        
        <h3 class="md-title">{{ $route.meta.title }}</h3>
      </div>
     
    </div>
    <md-toolbar md-elevation="0" class="md-transparent">
        <footer class="footer">
      <nav>
        <ul>
          <li>
            <a href="" target="_blank">Profesionales</a>
          </li>
          <li>
            <a href="" target="_blank">
              Convenio o Beneficio
            </a>
          </li>
          <li>
            <a href="" target="_blank">
              Contáctanos
            </a>
          </li>
        </ul>
      </nav>
  </footer>
      </md-toolbar>
  </md-toolbar>
  
  
</template>

<script>
export default {
  data() {
    return {
      selectedEmployee: null,
      employees: [
        "Jim Halpert",
        "Dwight Schrute",
        "Michael Scott",
        "Pam Beesly",
        "Angela Martin",
        "Kelly Kapoor",
        "Ryan Howard",
        "Kevin Malone"
      ]
    };
  },
  methods: {
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    }
  }
};
</script>