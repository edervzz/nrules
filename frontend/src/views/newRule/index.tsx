import Menubar from "../../components/Menubar";
import MainContainer from "../../components/MainContainer";
import CreateRule from "./CreateRule";
import Footer from "../../components/Footer/Footer";
export default function NewRuleView() {
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
