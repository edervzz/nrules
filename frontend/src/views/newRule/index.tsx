import Menubar from "../../components/Menubar";
import MainContainer from "../../components/MainContainer";
import CreateRule from "./CreateRule";
import FooterAux from "../../components/Footer/FooterAux";
import Messages from "../../locales/Messages";
export default function NewRuleView() {
    return (
        <MainContainer>
            <Menubar link_new="#" title={Messages.NEWRULE_CREA_RULE} />
            <CreateRule></CreateRule>
            <FooterAux></FooterAux>
        </MainContainer>
    );
}
