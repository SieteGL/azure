<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item md-medium-size-100 md-size-66">
        <md-card>
          <md-card-header data-background-color="pruebacolor">
            <h4 class="title">Toma De Hora</h4>
            <p class="category">Seleccione la Hora y Fecha de un Especialista Disponible</p>
          </md-card-header>
          <md-card-content>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Especialidad</label>
                  <md-select
                    v-model="speciality"
                    @md-selected="onChangeSpeciality($event)"
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
              <div class="md-layout-item md-medium-size-100 md-size-50">
                <md-field>
                  <label>Doctor</label>
                  <md-select v-model="doctor">
                    <md-option class="ls--option-span"></md-option>
                    <md-option
                      class="ls--option-span"
                      v-for="(item, idx) in doctors"
                      v-bind:key="idx"
                      :value="item.id"
                      >{{ item.nombre }} {{ item.apellido }}
                    </md-option>
                  </md-select>
                </md-field>
              </div>
              <div
                class="md-layout-item md-medium-size-100 md-large-size-30 md-size-20"
              >
                <md-button class="md-info md-block" @click="loadDoctorsHours"
                  ><md-icon>search</md-icon> Buscar hora</md-button
                >
              </div>
            </div>
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-100 md-size-100">
                <div v-if="doctorsSchedule.length">
                  <md-table
                    class="ls--mtop-15px"
                    v-model="doctorsSchedule"
                    :table-header-color="themeColor"
                    @md-selected="onSelectDoctorsSchedule"
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
                    </md-table-row>
                  </md-table>
                </div>
                <div v-else>
                  <h4 class="text-center">
                    No hay horas disponibles para visualizar
                  </h4>
                </div>
              </div>
              <div
                class="md-layout-item md-medium-size-100 md-large-size-30 md-size-20"
              >
                <md-button
                  class="md-primary md-block"
                  @click="submit"
                  :disabled="doctorSelected === null"
                  >Tomar hora</md-button
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
import ValidationException from "@/exceptions/ValidationException.js";

export default {
  mounted() {
    this.loadSpecialties();
    this.loadDoctors();
  },

  methods: {
    submit() {
      this.$confirm("Esta usted seguro?")
        .then(async () => {
          try {
            await backend.doctorsScheduleTake(this.doctorSelected.id);

            this.speciality = false;
            this.doctor = false;
            this.doctorSelected = null;
            this.doctorsSchedule = [];
          } catch (error) {
            if (error.name === "ValidationException") {
              throw error;
            }
            throw new ValidationException(
              "Error al asignar la hora al cliente"
            );
          }
        })
        .catch(error => {
          this.showNotificationMessage(this.chooseNotificationMessage(error));
        });
    },

    loadDoctors() {
      backend
        .doctors()
        .then(doctors => {
          this.doctors = doctors;
          this.doctorsOriginal = doctors;
          this.doctor = false;
        })
        .catch(error => {});
    },

    loadSpecialties() {
      backend
        .specialties()
        .then(specialties => {
          this.specialties = specialties;
        })
        .catch(error => {});
    },

    /**
     * Carga los horarios de los doctores seleccionados
     */
    loadDoctorsHours() {
      backend
        .doctorsSchedule(this.speciality, this.doctor)
        .then(({ data: { results } }) => {
          const doctor = this.doctors.find(item => item.id === this.doctor);
          const today = new Date();

          this.doctorsSchedule = results
            .filter(item => today < new Date(`${item.fecha} ${item.hora}`))
            .map(item => ({
              id: item.id,
              name: `${doctor.nombre} ${doctor.apellido}`,
              date: item.fecha,
              time: item.hora
            }));
        });
    },

    onChangeSpeciality(event) {
      this.doctors = this.doctorsOriginal.filter(
        ({ especialidades }) =>
          event === false || especialidades === String(event)
      );
      this.doctorsSchedule = [];
      this.doctor = false;
      this.doctorSelected = null;
    },

    onSelectDoctorsSchedule(item = null) {
      this.doctorSelected = item;
    }
  },

  props: {
    themeColor: {
      type: String
    }
  },

  data: () => ({
    speciality: false,
    specialties: [],

    doctor: false,
    doctorSelected: null,
    doctors: [],
    doctorsOriginal: [],
    doctorsSchedule: []
  })
};
</script>

