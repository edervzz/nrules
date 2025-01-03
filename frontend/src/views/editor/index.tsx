import MainContainer from "../../components/MainContainer";
import Menubar from "../../components/Menubar";
import Messages from "../../locales/Messages";
import Editor from "./Editor";

export default function EditorView() {
    return (
        <MainContainer>
            <Menubar title={Messages.EDITOR}></Menubar>
            <Editor></Editor>
        </MainContainer>
    );
}
