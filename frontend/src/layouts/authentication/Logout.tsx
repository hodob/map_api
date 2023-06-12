import React from 'react';


import { useEffect } from "react";
// import AuthApi from "../../../api/auth";
import { useNavigate } from "react-router-dom";
// import { useAuth } from "../../../auth-context/auth.context";


function Logout() {

    const navigate = useNavigate();
    // const history = useHistory();
    // const { setUser } = useAuth();
    // let { user } = useAuth();


    // const handleLogout = async () => {
        // await AuthApi.Logout(user);
        // await setUser(null);
    //     localStorage.removeItem("user");
    //     return history.push("/authentication/sign-in");
    //   };
    
    //   useEffect(() => {
    //     handleLogout();
    //   }, []);

    return null;
}

export default Logout;