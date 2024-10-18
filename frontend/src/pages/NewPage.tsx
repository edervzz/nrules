import Menubar from "../components/Menubar";
import MainContainer from "../components/MainContainer";
import CreateRule from "../components/CreateRule";
import Footer from "../components/Footer/Footer";
export default function NewPage() {
    return (
        <>
            <MainContainer>
                <Menubar link_new="#" />
                <CreateRule></CreateRule>
                <Footer></Footer>
            </MainContainer>
        </>
    );
}
