import React, {useState,createContext,useContext} from "react";


const AuthContext = createContext<any>(null);

export const AuthProvider= ({ userData, children }:{userData:string | null, children :React.ReactNode}) => {
  let [user, setUser] = useState(userData);
  user = typeof user === "string" ? JSON.parse(user) : user;

  return <AuthContext.Provider value={{ user, setUser }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);

