<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header :data-background-color="themeColor">
            <h4 class="title">Employees Stats</h4>
            <p class="category">New employees on 15th September, 2016</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field>
                  <label>Mostrar el calendario en</label>
                  <md-select v-model="displayPeriodUom">
                    <md-option class="ls--option-span" value="month"
                      >Mes</md-option
                    >
                    <md-option class="ls--option-span" value="week"
                      >Semana</md-option
                    >
                  </md-select>
                </md-field>
              </div>
            </div>
            <div class="md-layout">
              <div
                class="md-layout-item md-medium-size-100 md-size-100 ls--calendar-view"
              >
                <calendar-view
                  v-bind:items="events"
                  v-bind:display-period-uom="displayPeriodUom"
                  v-bind:show-date="showDate"
                  v-bind:show-times="showTimes"
                  v-bind:starting-day-of-week="startingDayOfWeek"
                  v-on:click-date="setEventDate"
                  v-on:click-item="dropEvent"
                  class="theme-default ls--calendar"
                  itemContentHeight="1.5em"
                  locale="es"
                  weekdayNameFormat="long"
                >
                  <calendar-view-header
                    slot="header"
                    slot-scope="t"
                    v-bind:header-props="t.headerProps"
                    v-on:input="setShowDate"
                  />
                </calendar-view>
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
      <div
        v-if="isSpecialist"
        class="md-layout-item md-medium-size-100 md-size-33"
      >
        <md-card>
          <md-card-header v-bind:data-background-color="themeColor">
            <h4 class="title">Employees Stats</h4>
            <p class="category">New employees on 15th September, 2016</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field>
                  <label>Fecha</label>
                  <md-input v-model="eventDate" type="text" disabled></md-input>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field>
                  <label>Hora</label>
                  <md-select v-model="eventHour">
                    <md-option class="ls--option-span"></md-option>
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in eventHours"
                      v-bind:key="idx"
                      v-bind:value="item.value"
                      v-bind:disabled="item.disabled"
                      >{{ item.value }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100">
                <md-button class="md-primary md-block" v-on:click="submit"
                  >Crear evento</md-button
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
import config from "@/config/app";
import { CalendarView, CalendarViewHeader } from "vue-simple-calendar";
// The next two lines are processed by webpack. If you're using the component without webpack compilation,
// you should just create <link> elements for these. Both are optional, you can create your own theme if you prefer.
//
// https://www.npmjs.com/package/vue-simple-calendar/v/5.0.1#events
require("vue-simple-calendar/static/css/default.css");

export default {
  components: {
    CalendarView,
    CalendarViewHeader
  },

  beforeMount() {
    this.isSpecialist = this.$settings.get("isSpecialist", false);
  },

  mounted() {
    if (this.isSpecialist) this.loadEvents();
    else this.loadClientEvents();
  },

  methods: {
    submit() {
      backend
        .doctorsScheduleEvent(this.eventDate, this.eventHour)
        .then(({ data }) => {
          this.loadEvents();

          this.eventDate = null;
          this.eventHour = null;
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    loadEvents() {
      backend
        .doctorsScheduleEvents()
        .then(({ data: { results } }) => {
          this.events = results.map(item => ({
            id: item.id,
            response: {
              ...item
            },
            startDate: `${item.fecha} ${item.hora}`,
            title: "Ocupado"
          }));
        })
        .catch(() => {
          console.log("Error el recuperar el horario");
        });
    },

    loadClientEvents() {
      backend
        .doctorsScheduleClientEvents()
        .then(({ data: { results } }) => {
          this.events = results.map(item => ({
            id: item.id,
            response: {
              ...item
            },
            startDate: `${item.fecha} ${item.hora}`,
            title: "Ocupado"
          }));
        })
        .catch(() => {
          console.log("Error el recuperar el horario");
        });
    },

    dropEvent(event) {
      if (!this.isSpecialist) {
        return;
      }

      this.$confirm("Desea eliminar la hora seleccionada?")
        .then(async () => {
          const response = await backend.doctorsScheduleEventDrop(event);
          this.loadEvents();
        })
        .catch(error => {
          if (typeof error === "undefined") {
            return;
          }

          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    setEventDate(event, items) {
      if (!this.isSpecialist) {
        return;
      }

      const date = event.toISOString().substr(0, 10);
      const hours = items.map(
        ({ originalItem: { response } }) => response.hora
      );

      this.eventDate = date;
      this.eventHours.forEach(item => {
        item.disabled = hours.indexOf(item.value) !== -1;
      });
    },

    setShowDate(date) {
      this.showDate = date;
    }
  },

  props: {
    themeColor: {
      type: String
    }
  },

  data: () => ({
    isSpecialist: false,

    showDate: new Date(),
    showTimes: true,

    startingDayOfWeek: 1,
    displayPeriodUom: "month",

    // eventos
    events: [],
    eventDate: null,
    eventHour: null,
    eventHours: config.CALENDAR_EVENT_TIME
  })
};
</script>
