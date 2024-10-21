import { createBrowserRouter } from "react-router-dom";

import NewRulePage from "./pages/newRule";
import MatrixPage from "./pages/matrix";
import Transports from "./pages/TransportsPage";
import TenancyPage from "./pages/TenancyPage";
import UsersPage from "./pages/UsersPage";
import LoginPage from "./pages/login";
import HomePage from "./pages/home";
import EditorPage from "./pages/editor";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <LoginPage />,
    },
    {
        path: "/home",
        element: <HomePage />,
    },
    {
        path: "/new",
        element: <NewRulePage />,
    },
    {
        path: "/editor/:id",
        element: <EditorPage />,
    },
    {
        path: "/matrix",
        element: <MatrixPage />,
    },
    {
        path: "/transports",
        element: <Transports />,
    },
    {
        path: "/tenancy",
        element: <TenancyPage />,
    },
    {
        path: "/users",
        element: <UsersPage />,
    },
    {
        path: "/runner",
        element: <UsersPage />,
    },
]);
