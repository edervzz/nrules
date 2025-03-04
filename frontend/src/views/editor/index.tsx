import Session from "../../components/Session";
import Menubar from "../../components/Menubar";
import Messages from "../../locales/Messages";
import Editor from "./Editor";

export default function EditorView() {
    return (
        <Session>
            <Menubar brand={Messages.NRULE} title={Messages.EDITOR}></Menubar>
            <Editor></Editor>
        </Session>
    );
}
