import React, {useState,createContext,useContext} from "react";

type AuthContextValue = {
  user: string | null;
  setUser: (user: string | null) => void;
};

const AuthContext = createContext< AuthContextValue | null>(null);

export const AuthProvider= ({ userData, children }:{userData:string | null, children :React.ReactNode}) => {
  let [user, setUser] = useState(userData);
  user = user ? JSON.parse(user) : user;

  return <AuthContext.Provider value={{ user, setUser }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);

