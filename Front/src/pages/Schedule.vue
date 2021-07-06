<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header :data-background-color="themeColor">
            <h4 class="title">Agendar Horario Especialista</h4>
            <p class="category">Ingrese los horarios disponibles del Especialista</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100  md-size-50">
                <md-field>
                  <label>Calendario</label>
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
                  :items="events"
                  :display-period-uom="displayPeriodUom"
                  :show-date="showDate"
                  :show-times="showTimes"
                  :starting-day-of-week="startingDayOfWeek"
                  @click-date="setEventDate"
                  class="theme-default ls--calendar"
                  itemContentHeight="1.5em"
                  locale="es"
                  weekdayNameFormat="long"
                >
                  <calendar-view-header
                    slot="header"
                    slot-scope="t"
                    :header-props="t.headerProps"
                    @input="setShowDate"
                  />
                </calendar-view>
              </div>
            </div>
          </md-card-content>
        </md-card>
      </div>
      <div class="md-layout-item md-medium-size-100 md-size-33">
        <md-card>
          <md-card-header :data-background-color="themeColor">
            <h4 class="title">Fecha y Horario disponible para el Especialista</h4>
            <p class="category">Seleccione fecha y horarios disponibles</p>
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
                      :key="idx"
                      :value="item.value"
                      :disabled="item.disabled"
                      >{{ item.value }}</md-option
                    >
                  </md-select>
                </md-field>
              </div>
              <div class="md-layout-item md-medium-size-100">
                <md-button class="md-primary md-block" @click="submit"
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

  mounted() {
    this.loadEvents();
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

    setEventDate(event, items) {
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
      console.log("set show date");
    }
  },

  props: {
    themeColor: {
      type: String
    }
  },

  data: () => ({
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
