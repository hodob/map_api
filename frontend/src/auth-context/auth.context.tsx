import React, {useState,createContext,useContext} from "react";

type user = null|{
  email: string;
  name: string;
  token: string;
  _id: string;
  Prototype:Object
}
type userset=null|React.Dispatch<React.SetStateAction<user>>

const AuthContext = createContext<user>(null);
const AuthSetContext = createContext<userset>(null);

export const AuthProvider= ({ userData, children }:{userData:user, children :React.ReactNode}) => {
  let [user, setUser] = useState(userData);
  user = typeof user === "string" ? JSON.parse(user) : user;
  return (
    <AuthContext.Provider value={user}>
        <AuthSetContext.Provider value={setUser}>
          {children}
        </AuthSetContext.Provider>
    </AuthContext.Provider>
    )
};

// export const useAuth = () => useContext(AuthContext);
export function useAuth(){
  const context = useContext(AuthContext);
  if(!context){
    throw new Error('AuthContext not found');
  }
  return context;
}
export function useAuthSet(){
  const context = useContext(AuthSetContext);
  if(!context){
    throw new Error('AuthSetContext not found');
  }
  return context;
}
