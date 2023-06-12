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
class AuthApi {

      static Login = (data:data_login) => {
        console.log(data);
        return axiostool.post(`${base}/login`, data);
      };

      public static Register(data:data_register){        
        return axiostool.post(`${base}/register`, data, )
      };
    //   static Logout = (data) => {
    //     return axios.post(`${base}/logout`, data, { headers: { Authorization: `${data.token}` } });
    //   };
}

let base = "users";

export default AuthApi;


