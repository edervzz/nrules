import { useParams } from "react-router-dom";
import MainContainer from "../../components/MainContainer";
import Menubar from "../../components/Menubar";
import Editor from "./Editor";

export default function EditorPage() {
    const { id } = useParams();
    console.log(id);

    return (
        <MainContainer>
            <Menubar></Menubar>
            <Editor></Editor>
        </MainContainer>
    );
}
