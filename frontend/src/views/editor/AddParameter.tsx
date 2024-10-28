import React from "react";
import { Button, Form, InputGroup, Modal } from "react-bootstrap";
import Messages from "../../locales/Messages";

type Props = {};

const AddParameter = (props: Props) => {
    return (
        <Modal show>
            <Modal.Header closeButton>
                <Modal.Title>Add Parameter: Condition</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <InputGroup className="mb-3">
                    <InputGroup.Text>{Messages.CONDNAME}</InputGroup.Text>
                    <Form.Control aria-label="First name" />
                </InputGroup>
                <InputGroup className="mb-3">
                    <InputGroup.Text>{Messages.TYPE}</InputGroup.Text>
                    <Form.Control aria-label="Type" />
                </InputGroup>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary">Close</Button>
                <Button variant="primary">Save Changes</Button>
            </Modal.Footer>
        </Modal>
    );
};

export default AddParameter;
