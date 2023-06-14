import React, {useState,createContext,useContext} from "react";

type user = {
  email: string
  name: string
  token: string
  _id: string
  Prototype:Object
};

type userset=React.Dispatch<React.SetStateAction<user|null>>

const AuthContext = createContext<user|null>(null);
const AuthSetContext = createContext<userset|null>(null);

export const AuthProvider= ({ userData, children }:{userData:user, children :React.ReactNode}) => {
  let [user, setUser] = useState<null|user>(userData);
  user = typeof user === "string" ? JSON.parse(user) : user;
  return (
    <AuthContext.Provider value={user}>
        <AuthSetContext.Provider value={setUser}>
          {children}
        </AuthSetContext.Provider>
    </AuthContext.Provider>
    )
};

export function useAuth(){
  const context1= useContext(AuthContext);
  return context1;
}

export function useAuthSet(){
  const context2 = useContext(AuthSetContext);
    return context2;
  }

