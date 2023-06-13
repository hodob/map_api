import axiostool from "./axiostool";
type data_login = {
  password: string;
  email: string;
}

type data_register = {
  name: string;
  password: string;
  email: string;
  phone: string;
  address: string;
  dob: string;
  agreeTerms: Boolean;
  agreePrivacyPolicy: Boolean;
  agreeDataProcessing: Boolean;
}

type user = {
  email: string;
  name: string;
  token: string;
  _id: string;
  Prototype:Object
}
class AuthApi {

      static Login = (data:data_login) => {
        return axiostool.post(`${base}/login`, data);
      };

      public static Register(data:data_register){        
        return axiostool.post(`${base}/register`, data, )
      };
      static Logout = (data:user) => {
        return axiostool.post(`${base}/logout`, data, { headers: { Authorization: `${data.token}` } });
      };
}

let base = "users";

export default AuthApi;


