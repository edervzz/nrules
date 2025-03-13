import { createBrowserRouter } from "react-router-dom";

import NewRuleView from "./views/newRule";
import XTest from "./views/xtest";
import RulesView from "./views/rules";
// import TransportsView from "./views/Transports";
import TenancyView from "./views/tenancy/Tenancy";
// import UsersView from "./views/Users";
import LoginView from "./views/login";
import EditorView from "./views/editor";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <LoginView />,
    },
    {
        path: "/new",
        element: <NewRuleView />,
    },
    {
        path: "/editor/:id",
        element: <EditorView />,
    },
    {
        path: "/rules",
        element: <RulesView />,
    },
    {
        path: "/tenancy",
        element: <TenancyView />,
    },
    {
        path: "/xtest",
        element: <XTest />,
    },
]);
