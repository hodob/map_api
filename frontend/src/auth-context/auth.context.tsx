import React, {useState,createContext} from "react";
import PropTypes from "prop-types";

const AuthContext = createContext<any>(null);


export const AuthProvider:any|null= ({ userData, children }:{userData:any, children :any}) => {
  let [user, setUser]:[user:null|any,setUser:null|any] = useState<any|null>(userData);
  user = typeof user === "string" ? JSON.parse(user) : user;

  return <AuthContext.Provider value={{ user, setUser }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => React.useContext(AuthContext);

