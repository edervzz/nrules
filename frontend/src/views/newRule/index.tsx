import Menubar from "../../components/Menubar";
import Session from "../../components/Session";
import RuleForm from "../../components/RuleForm";
import FooterAux from "../../components/Footer/FooterAux";
import Messages from "../../locales/Messages";
import { useState } from "react";
import {
    CreateRuleDto,
    ErrorDto,
    NewRuleCondition,
    NewRuleOutput,
    NewRuleTag,
    ParametersDto,
    TagDto,
} from "../../models";
import Storage from "../../storage";
import { useNavigate } from "react-router-dom";
import { LoadingErrorListModal } from "../../components/LoadingModal";

function NewRuleView() {
    const [showSending, setShowSending] = useState(false);
    const [errorList, setErrorList] = useState<ErrorDto[]>([]);

    const navigate = useNavigate();

    const handleSubmit = (
        rulename: string,
        ruletype: string,
        strategy: string,
        conditions: NewRuleCondition[],
        outputs: NewRuleOutput[],
        tags: NewRuleTag[]
    ) => {
        setShowSending(true);
        setErrorList([]);

        // const conds = conditions.map((x) => {
        //     return {
        //         key: x.variable,
        //         typeof: x.type,
        //         usefor: "INPUT",
        //     } as ParametersDto;
        // });

        // const outs = outputs.map((x) => {
        //     return {
        //         key: x.variable,
        //         typeof: x.type,
        //         usefor: "OUTPUT",
        //     } as ParametersDto;
        // });

        const tgs = tags.map((x) => {
            return {
                key: x.key,
                value: x.value,
            } as TagDto;
        });

        const newRule: CreateRuleDto = {
            name: rulename,
            rule_type: ruletype == "1" ? "TABLE" : "TREE",
            strategy: strategy,
            // parameters: [...conds, ...outs],
            tags: [...tgs],
        };

        Storage.Rule.PostRule(newRule).then((result) => {
            if (result.ok) {
                setShowSending(false);
                const item = result.item!;
                const elements = item.split("/");
                const uuidobj = elements[elements.length - 1];
                navigate(`/editor/${uuidobj}`);
            } else {
                const data = result.errorList!;
                setErrorList(data);
            }
        });
    };

    return (
        <Session>
            <Menubar
                link_new="#"
                brand={Messages.NRULE}
                title={Messages.NEWRULE_CREA_RULE}
            />
            <LoadingErrorListModal
                show={showSending}
                title={Messages.COMMON_SENDING}
                isFailure={errorList.length > 0}
                errorList={errorList}
                onClose={() => setShowSending(false)}
            />

            <RuleForm onSubmit={handleSubmit} />

            <FooterAux />
        </Session>
    );
}

export default NewRuleView;
