import React, {useState,createContext,useContext} from "react";
import PropTypes from "prop-types";

const AuthContext = createContext<any>(null);

export const AuthProvider= ({ userData, children }:{userData:any, children :React.ReactNode}) => {
  let [user, setUser] = useState(userData);
  user = typeof user === "string" ? JSON.parse(user) : user;

  return <AuthContext.Provider value={{ user, setUser }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);

