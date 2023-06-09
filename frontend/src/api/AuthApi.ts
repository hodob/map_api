import axiostool from "./axiostool";

class AuthApi {

    //   static Login = (data) => {
    //     return axios.post(`${base}/login`, data);
    //   };

    // static Register(data: any): any {
    //     return axiostool.post("/register", data);
    //     // return null;
    // };
      // public static Register(data:any){        
      //   return axiostool.post(`${base}/register`, data)
      // };

      public static Register(data:any){        
        return axiostool.post(`${base}/register`, data, )
      };
    //   static Logout = (data) => {
    //     return axios.post(`${base}/logout`, data, { headers: { Authorization: `${data.token}` } });
    //   };
}

let base = "users";

export default AuthApi;


