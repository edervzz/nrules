export type UpdKVItemDto = {
    key: string,
    value: string,
    calculation: string
}

export type UpdItemsKVItemDto = {
    items: UpdKVItemDto[]
}
