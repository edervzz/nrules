import MainContainer from "../../components/MainContainer";
import Menubar from "../../components/Menubar";
import Editor from "./Editor";

export default function EditorPage() {
    return (
        <MainContainer>
            <Menubar></Menubar>
            <Editor></Editor>
        </MainContainer>
    );
}
