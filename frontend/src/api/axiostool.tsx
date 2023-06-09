import Axios from "axios";
import { API_SERVER } from "../config/constant";


const axiostool = Axios.create({
  baseURL: `${API_SERVER}`,
  headers: { "Content-Type": "application/json" },
});

axiostool.interceptors.request.use(
  (config) => {
    return Promise.resolve(config);
  },
  (error) => Promise.reject(error)
);

axiostool.interceptors.response.use(
  (response) => Promise.resolve(response),
  (error) => {
    return Promise.reject(error);
  }
);

export default axiostool;
