import React from 'react';

import { Route,Routes } from "react-router-dom";
import routes from './routes';

import 'bootstrap/dist/css/bootstrap.min.css';

import NavbarLayout from './layouts/navbar/Navbar';

type RouteType = {
  type: string;
  name: string;
  key: string;
  route: string;
  // icon: any;
  component: () => JSX.Element;
  noCollapse: boolean;
  protected: boolean;
};

const getRoutes :any = (allRoutes: RouteType[]) =>
allRoutes.map((route: RouteType) => 
{
  // if (true){
  //   return <Route path={route.route} element={<route.component/>} key={route.key}/>
  // }
  return <Route path={route.route} element={<route.component/>} key={route.key}/>
});

function App() {
  return (
    <>
    <NavbarLayout/>
    <Routes>
      {getRoutes(routes)}
      </Routes>
      </>
  );
}

export default App;