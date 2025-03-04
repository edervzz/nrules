import { Button, Container, Table } from "react-bootstrap";
import Messages from "../../locales/Messages";
import { ReadRuleDto } from "../../models";

interface PropsBoard {
    fluid?: boolean | string | "sm" | "md" | "lg" | "xl" | "xxl";
    rules: ReadRuleDto[];
}

function Board({ fluid, rules }: PropsBoard) {
    return (
        <Container fluid={fluid}>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>{Messages.NEWRULE_RULENAME}</th>
                        <th>{Messages.ACTIONS}</th>
                        <th colSpan={2}>{Messages.NEWRULE_RULETYPE}</th>
                        <th>{Messages.NEWRULE_RULESTRATEGY}</th>
                        <th>Dev</th>
                        <th>Test</th>
                        <th>Prod</th>
                        <th className="text-center">
                            {Messages.NEWRULE_STATUS}
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {rules.map((x) => (
                        <tr
                            key={x.id}
                            style={{
                                fontSize: "14px",
                                fontWeight: "bold",
                                color: "#868686",
                            }}
                        >
                            <td>
                                <a
                                    style={{
                                        fontSize: "14px",
                                        fontWeight: "bold",
                                        textTransform: "uppercase",
                                        textDecoration: "none",
                                        color: "#0d6efd",
                                    }}
                                    href={"/editor/" + x.id}
                                >
                                    {x.name}
                                </a>
                            </td>
                            <td>
                                <Button variant="primary" size="sm">
                                    <i className="bi bi-play-fill"></i>
                                </Button>
                            </td>
                            <td className="">
                                {x.rule_type == "TREE" && (
                                    <i className="bi bi-diagram-2-fill" />
                                )}
                                {x.rule_type == "TABLE" && (
                                    <i className="bi bi-table" />
                                )}
                            </td>
                            <td>{x.rule_type}</td>
                            <td>{x.strategy}</td>

                            <td>{x.version}</td>
                            <td>{x.version}</td>
                            <td>{x.version}</td>
                            <td className="text-center">
                                <i
                                    className="bi bi-check-circle-fill"
                                    style={{ color: "green" }}
                                ></i>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </Container>
    );
}

export default Board;
