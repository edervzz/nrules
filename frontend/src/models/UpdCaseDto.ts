export type UpdCaseDto = {
    id: string,
    position: number,
    is_active: boolean,
    is_archive: boolean
}

export type UpdItemsCaseDto = {
    items: UpdCaseDto[]
}
