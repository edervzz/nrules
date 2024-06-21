package entities

type Rule struct {
	ID     string
	Name   string
	Params []Variable
}

type Variable struct {
	KeyValue
}

type KV struct {
	KeyValue
}

type KeyValue struct {
	Name  string `mapper:"name"`
	Value any    `mapper:"value"`
	Type  string `mapper:"type"`
}
