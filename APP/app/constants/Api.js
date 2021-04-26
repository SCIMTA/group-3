const R = require("@app/assets/R").default;
const NavigationUtil = require("@app/navigation/NavigationUtil").default;
const { showMessages } = require("@app/utils/AlertHelper");
const { API_STATUS } = require("@constant");
const { AsyncStorage } = require("react-native");

const createAPI = () => {
  const dev = false;

  const APIInstant = require("axios").default.create();
  APIInstant.defaults.baseURL = dev
    ? "http://192.168.0.112:8003/"
    : "http://128.199.108.177:8003/";
  APIInstant.defaults.timeout = 20000;
  APIInstant.defaults.headers = {
    "Content-Type": "application/json"
  };
  APIInstant.interceptors.request.use(config => {
    return config;
  }, Promise.reject);

  APIInstant.interceptors.response.use(response => {
    // const data = response.data;

    return response;
  });
  return APIInstant;
};

const getAPI = createAPI();

/* Support function */
const handleResult = api =>
  api.then(res => {
    if (res.data.status == API_STATUS.RE_LOGIN) {
      showMessages(R.strings().notification, R.strings().re_login, () => {
        AsyncStorage.setItem("token", "").then(() => {
          NavigationUtil.navigate("Auth");
        });
      });
    }
    if (res.data.status == 0) {
      showMessages(R.strings().notification, res.data.message);
      return Promise.reject(res.data.message);
    }
    return Promise.resolve(res.data);
  });

module.exports = {
  predict: payload => handleResult(getAPI.post(`predict`, payload))
};
