import MainLayout from "./layouts/main";


const routes = [
    {
      type: "none",
      name: "MainLayout",
      key: "main-layout",
      route: "/",
    //   icon: <Shop size="12px" />,
      component: MainLayout,
      noCollapse: true,
      protected: false,
    },
    {
        type: "none",
        name: "dummy",
        key: "dummy-layout",
        route: "/dummy",
      //   icon: <Shop size="12px" />,
        component: MainLayout,
        noCollapse: true,
        protected: false,
      },
    // {
    //   type: "collapse",
    //   name: "Dashboard",
    //   key: "dashboard",
    //   route: "/dashboard",
    //   icon: <Shop size="12px" />,
    //   component: Dashboard,
    //   noCollapse: true,
    //   protected: true,
    // },
    // {
    //   type: "collapse",
    //   name: "Tables",
    //   key: "tables",
    //   route: "/tables",
    //   icon: <Office size="12px" />,
    //   component: Tables,
    //   noCollapse: true,
    //   protected: true,
    // },
    // {
    //   type: "collapse",
    //   name: "Billing",
    //   key: "billing",
    //   route: "/billing",
    //   icon: <CreditCard size="12px" />,
    //   component: Billing,
    //   noCollapse: true,
    //   protected: true,
    // },
    // {
    //   type: "collapse",
    //   name: "Virtual Reality",
    //   key: "virtual-reality",
    //   route: "/virtual-reality",
    //   icon: <Cube size="12px" />,
    //   component: VirtualReality,
    //   noCollapse: true,
    //   protected: true,
    // },
    // {
    //   type: "collapse",
    //   name: "RTL",
    //   key: "rtl",
    //   route: "/rtl",
    //   icon: <Settings size="12px" />,
    //   component: RTL,
    //   noCollapse: true,
    //   protected: true,
    // },
    // { type: "title", title: "Account Pages", key: "account-pages" },
    // {
    //   type: "collapse",
    //   name: "Profile",
    //   key: "profile",
    //   route: "/profile",
    //   icon: <CustomerSupport size="12px" />,
    //   component: Profile,
    //   noCollapse: true,
    //   protected: true,
    // },
    // {
    //   type: "none",
    //   name: "Sign In",
    //   key: "sign-in",
    //   route: "/authentication/sign-in",
    //   icon: <Document size="12px" />,
    //   component: SignIn,
    //   noCollapse: true,
    // },
    // {
    //   type: "none",
    //   name: "Sign Up",
    //   key: "sign-up",
    //   route: "/authentication/sign-up",
    //   icon: <SpaceShip size="12px" />,
    //   component: SignUp,
    //   noCollapse: true,
    // },
    // {
    //   type: "collapse",
    //   name: "Logout",
    //   key: "sign-out",
    //   route: "/authentication/sign-out",
    //   icon: <SpaceShip size="12px" />,
    //   component: SignOut,
    //   noCollapse: true,
    // },
  ];
  
  export default routes;
  