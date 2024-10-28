import { createBrowserRouter } from "react-router-dom";

import NewRuleView from "./views/newRule";
import MatrixView from "./views/matrix";
import TransportsView from "./views/Transports";
import TenancyView from "./views/Tenancy";
import UsersView from "./views/Users";
import LoginView from "./views/login";
import HomePage from "./views/home";
import EditorView from "./views/editor";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <LoginView />,
    },
    {
        path: "/home",
        element: <HomePage />,
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
        path: "/matrix",
        element: <MatrixView />,
    },
    {
        path: "/transports",
        element: <TransportsView />,
    },
    {
        path: "/tenancy",
        element: <TenancyView />,
    },
    {
        path: "/users",
        element: <UsersView />,
    },
    {
        path: "/runner",
        element: <UsersView />,
    },
]);
