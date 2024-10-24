import MainContainer from "../../components/MainContainer";
import Menubar from "../../components/Menubar";
import Matrixes from "./Matrixes";
import Footer from "../../components/Footer/Footer";

export default function MatrixPage() {
    return (
        <MainContainer>
            <Menubar></Menubar>
            <Matrixes></Matrixes>
            <Footer></Footer>
        </MainContainer>
    );
}
