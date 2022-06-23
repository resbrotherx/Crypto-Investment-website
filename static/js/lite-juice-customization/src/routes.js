// core components
// import Login from "views/auth/Login.js";
import Customers from "views/admin/Customers";
// import Register from "views/auth/Register.js";
// import Tables from "views/admin/Tables.js";
// @material-ui/icons components
// import AccountCircle from "@material-ui/icons/AccountCircle";
import FlashOn from "@material-ui/icons/FlashOn";

import Grain from "@material-ui/icons/Grain";


// import VpnKey from "@material-ui/icons/VpnKey";

var routes = [
  {
    href: "#pablo",
    name: "©  EEDC-SMB",
    icon: FlashOn,
    upgradeToPro: true,
  },
  {
    path: "/index",
    name: "Customers",
    icon: Grain,
    iconColor: "Primary",
    component: Customers,
    layout: "/admin",
  },
 
  {
    divider: true,
  },
  
];
export default routes;
