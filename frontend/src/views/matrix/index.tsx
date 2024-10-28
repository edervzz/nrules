import MainContainer from "../../components/MainContainer";
import Menubar from "../../components/Menubar";
import Matrixes from "./Matrixes";
import Footer from "../../components/Footer/Footer";
import Messages from "../../locales/Messages";

export default function MatrixView() {
    return (
        <MainContainer>
            <Menubar title={Messages.COMMON_MATRIX}></Menubar>
            <Matrixes></Matrixes>
            <Footer></Footer>
        </MainContainer>
    );
}
