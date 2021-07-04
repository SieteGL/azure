const API_LOCATION = "http://localhost:8000/api";
const API_LOCATION_IS_SPECIALIST = `${API_LOCATION}/usuarios/1`;
const API_LOCATION_IS_ADMIN = `${API_LOCATION}/usuarios/0`;

const API_LOCATION_TOKEN_REFRESH = `${API_LOCATION}/token/refresh/`;

const STORAGE_KEY_TOKEN = "token";
const STORAGE_KEY_SETTINGS = "settings";

const USER_TYPE_ADMIN = "admin";
const USER_TYPE_SPECIALIST = "specialist";
const USER_TYPE_PROVIDER = "provider";
const USER_TYPE_RECEPTIONIST = "receptionist";

const USER_TYPE_IDS = {
  [USER_TYPE_ADMIN]: "admin",
  [USER_TYPE_SPECIALIST]: "espe",
  [USER_TYPE_PROVIDER]: "pro",
  [USER_TYPE_RECEPTIONIST]: "recep"
};

const CALENDAR_EVENT_TIME = [
  { value: "00:00", disabled: false },
  { value: "01:00", disabled: false },
  { value: "02:00", disabled: false },
  { value: "03:00", disabled: false },
  { value: "04:00", disabled: false },
  { value: "05:00", disabled: false },
  { value: "06:00", disabled: false },
  { value: "07:00", disabled: false },
  { value: "08:00", disabled: false },
  { value: "09:00", disabled: false },
  { value: "10:00", disabled: false },
  { value: "11:00", disabled: false },
  { value: "12:00", disabled: false },
  { value: "13:00", disabled: false },
  { value: "14:00", disabled: false },
  { value: "15:00", disabled: false },
  { value: "16:00", disabled: false },
  { value: "17:00", disabled: false },
  { value: "18:00", disabled: false },
  { value: "19:00", disabled: false },
  { value: "20:00", disabled: false },
  { value: "21:00", disabled: false },
  { value: "22:00", disabled: false },
  { value: "23:00", disabled: false }
];

export default {
  API_LOCATION,
  API_LOCATION_IS_ADMIN,
  API_LOCATION_IS_SPECIALIST,
  API_LOCATION_TOKEN_REFRESH,

  STORAGE_KEY_SETTINGS,
  STORAGE_KEY_TOKEN,

  USER_TYPE_ADMIN,
  USER_TYPE_SPECIALIST,
  USER_TYPE_PROVIDER,
  USER_TYPE_RECEPTIONIST,
  USER_TYPE_IDS,

  CALENDAR_EVENT_TIME
};
