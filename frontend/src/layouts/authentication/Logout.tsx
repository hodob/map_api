import React from 'react';


import { useEffect } from "react";
import AuthApi from "../../api/AuthApi";
import { useNavigate } from "react-router-dom";
import { useAuth } from '../../auth-context/auth.context';


function Logout() {

    const navigate = useNavigate();
    
    const { setUser } = useAuth();
    let { user } = useAuth();


    const handleLogout = async () => {
        await AuthApi.Logout(user);
        await setUser(null);
        localStorage.removeItem("user");
        return navigate("/authentication/sign-in");
      };
    
      useEffect(() => {
        handleLogout();
      }, []);

    return null;
}

export default Logout;