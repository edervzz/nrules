import Menubar from "../../components/Menubar";
import MainContainer from "../../components/MainContainer";
import CreateRule from "./CreatRule";
import Footer from "../../components/Footer/Footer";
export default function NewRulePage() {
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
