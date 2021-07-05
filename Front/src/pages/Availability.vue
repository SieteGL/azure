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
            <md-steppers
              class="ls--horizontal-steppers"
              :md-active-step.sync="active"
              md-linear
            >
              <md-step
                id="first"
                md-label="First Step"
                md-description="Optional"
                :md-done.sync="first"
              >
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                    <md-field>
                      <label>Especilidad</label>
                      <md-select
                        v-model="speciality"
                        @md-selected="onChangeLoadDoctors($event)"
                      >
                        <md-option class="ls--option-span"></md-option>
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in specialties"
                          v-bind:key="idx"
                          :value="item.code"
                          >{{ item.name }}</md-option
                        >
                      </md-select>
                    </md-field>
                  </div>
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                    <md-field>
                      <label>Doctor</label>
                      <md-select v-model="doctor">
                        <md-option class="ls--option-span"></md-option>
                        <md-option
                          class="ls--option-span"
                          v-for="(item, idx) in doctors"
                          v-bind:key="idx"
                          :value="item.code"
                          >{{ item.name }}</md-option
                        >
                      </md-select>
                    </md-field>
                  </div>

                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <md-button
                      class="md-raised"
                      :class="chooseColorClass(themeColor)"
                      @click="loadMedicalSchedules"
                      >Buscar hora</md-button
                    >
                  </div>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <div v-if="doctorsSchedule.length">
                      <md-table
                        class="ls--mtop-15px"
                        v-model="doctorsSchedule"
                        @md-selected="onSelectDoctorsSchedule"
                        :table-header-color="themeColor"
                      >
                        <md-table-row
                          md-selectable="single"
                          slot="md-table-row"
                          slot-scope="{ item }"
                        >
                          <md-table-cell md-label="Doctor">{{
                            item.name
                          }}</md-table-cell>
                          <md-table-cell md-label="Fecha">{{
                            item.date
                          }}</md-table-cell>
                          <md-table-cell md-label="Hora">{{
                            item.time
                          }}</md-table-cell>
                          <md-table-cell md-label="Duración">{{
                            item.duration
                          }}</md-table-cell>
                        </md-table-row>
                      </md-table>
                    </div>
                    <div v-else>
                      <h4 class="text-center">
                        No hay doctores para visualizar
                      </h4>
                    </div>
                  </div>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <md-button
                      class="md-raised md-primary"
                      @click="setDone('first', 'second')"
                      :disabled="secondStep"
                      >Siguiente</md-button
                    >
                  </div>
                </div>
              </md-step>

              <md-step
                id="second"
                md-label="Second Step"
                :md-done.sync="second"
              >
                <div class="md-layout-item md-medium-size-100 md-size-50">
                  <md-datepicker
                    :md-model-type="String"
                    :md-disabled-dates="disabledDates"
                    md-immediately
                  >
                    <label>Fecha</label>
                  </md-datepicker>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <!--
                    <md-table
                      class="ls--mtop-15px"
                      v-model="doctors"
                      :table-header-color="themeColor"
                    >
                      <md-table-row
                        md-selectable="single"
                        slot="md-table-row"
                        slot-scope="{ item }"
                      >
                        <md-table-cell md-label="Doctor">{{
                          item.name
                        }}</md-table-cell>
                        <md-table-cell md-label="Fecha">{{
                          item.date
                        }}</md-table-cell>
                        <md-table-cell md-label="Hora">{{
                          item.time
                        }}</md-table-cell>
                        <md-table-cell md-label="Duración">{{
                          item.duration
                        }}</md-table-cell>
                      </md-table-row>
                    </md-table>
                    -->
                  </div>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100  md-size-50">
                    <md-field>
                      <label>Pacient</label>
                      <md-input type="text"></md-input>
                    </md-field>
                  </div>
                </div>
                <div class="md-layout">
                  <div class="md-layout-item md-medium-size-100  md-size-100">
                    <md-button
                      class="md-raised md-primary"
                      @click="setDone('second', 'third')"
                      >Siguiente</md-button
                    >
                  </div>
                </div>
              </md-step>

              <md-step id="third" md-label="Third Step" :md-done.sync="third">
                <md-button
                  class="md-raised md-primary"
                  @click="setDone('third')"
                  >Confirmar</md-button
                >
              </md-step>
            </md-steppers>
          </md-card-content>
        </md-card>
      </div>
    </div>
  </div>
</template>

<script>
import backend from "@/services/backend.js";

export default {
  beforeMount() {
    backend
      .specialties()
      .then(specialties => {
        this.specialties = specialties;
      })
      .catch(error => {});
    backend
      .doctors(null)
      .then(doctors => {
        this.doctors = doctors;
      })
      .catch(error => {});
  },

  methods: {
    onChangeLoadDoctors(event) {
      backend
        .doctors(event === false ? null : event)
        .then(doctors => {
          this.doctors = doctors;
          this.doctor = false;
        })
        .catch(error => {});
    },

    onSelectDoctorsSchedule(item = null) {
      this.doctorSelected = item;
      this.secondStep = item === null;
    },

    loadMedicalSchedules() {
      backend
        .doctorsSchedule(this.speciality || null, this.doctor || null)
        .then(doctors => {
          this.doctorsSchedule = doctors;
        })
        .catch(error => {});
    },

    setDone(id, index) {
      this[id] = true;

      if (index) {
        this.active = index;
      }
    },

    onSelect(item) {
      this.selected = item;
    },

    disabledDates(date) {
      const current = new Date();

      date.setHours(0, 0, 0, 0);
      current.setHours(0, 0, 0, 0);

      return date < current;
    }
  },

  props: {
    themeColor: {
      type: String
    }
  },

  data: () => ({
    selected: null,
    active: "first",

    first: false,
    second: false,
    secondStep: true,
    third: false,

    speciality: false,
    specialties: [],

    doctor: false,
    doctorSelected: null,
    doctors: [],
    doctorsSchedule: []
  })
};
</script>

<style lang="scss" scoped>
.md-steppers {
}
</style>
