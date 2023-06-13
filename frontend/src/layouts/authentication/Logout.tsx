import React from 'react';


import { useEffect } from "react";
import AuthApi from "../../api/AuthApi";
import { useNavigate } from "react-router-dom";
import { useAuth } from '../../auth-context/auth.context';

type AuthContextValue = {
    user: string | null;
    setUser: (user: string | null) => void;
  };
  
function Logout() {

    const navigate = useNavigate();
    
    // const { setUser }  = useAuth() as AuthContextValue;
    // const setUser: (user: string | null) => void
    const { setUser } : any= useAuth();
    let { user }:any = useAuth() ;

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