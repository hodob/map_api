import React from 'react';

import routes from './routes';

// type routesType = {
//     type: string,
//     name: string,
//     key: string,
//     route: string,
//     icon: any,
//     component: any,
//     noCollapse: boolean,
//     protected: boolean,
// };
type RouteType = {
  type: string;
  name: string;
  key: string;
  route: string;
  icon: any;
  component: any;
  noCollapse: boolean;
  protected: boolean;
};



const getRoutes = (allRoutes : RouteType) =>
(
  allRoutes.map((route:any) => {
    //   if (route.collapse) {
    //     return getRoutes(route.collapse);
    //   }

    //   if (route.route) {
    //     if (route.protected) {
    //       return <ProtectedRoute path={route.route} component={route.component} key={route.key} />;
    //     }
    //     return (
    //     <Route exact path={route.route} component={route.component} key={route.key} />
    //     );

    //   }
    //   return null;
    })
)
    ;

function App() {
  return (
    <>
      {getRoutes(routes)}
    </>
  );
}

export default App;
