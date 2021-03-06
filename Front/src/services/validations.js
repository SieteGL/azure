import {
  required,
  requiredIf,
  email,
  sameAs,
  minLength,
  maxLength
} from "vuelidate/lib/validators";

/*
 * Vuelidate
 * https://vuelidate.js.org/#sub-error-vs-any-error
 */

const validations = {
  required: { required },
  occupation: { required },
  name: {
    required,
    minLength: minLength(3)
  },
  lastname: {
    required,
    minLength: minLength(2)
  },
  run: {
    required,
    minLength: minLength(6)
  },
  username: { required, email },
  phone: { required },
  birthdate: { required },
  gender: { required },
  region: { required },
  city: { required },
  district: { required },
  address: {
    required,
    minLength: minLength(6)
  },
  house: {
    required,
    maxLength: maxLength(5)
  },
  password: {
    required,
    /**
     * Validador original
     *   /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/
     *
     * @param {string} value
     *
     * @returns {boolean}
     */
    strongPassword: value => /^(?=.*[0-9])(?=.*[!@#$%^&*]).{6,16}$/.test(value)
  },
  confirmPassword: {
    required,
    sameAsPassword: sameAs("password")
  },

  /*
   * Validaciones especiales por página
   */
  userManagerSpeciality: {
    required: requiredIf(function() {
      return this.occupation === "specialist";
    })
  },
  clientDataSheetAllergyType: {
    required: requiredIf(function() {
      return this.allergy;
    })
  },
  clientDataSheetDiseaseType: {
    required: requiredIf(function() {
      return this.disease;
    })
  }
};

export default function rules(properties) {
  const extra = {};
  properties.forEach(property => {
    const [attr, , name = null] = property.split(" ");
    if (attr in validations) extra[name || attr] = validations[attr];
  });

  return extra;
}
