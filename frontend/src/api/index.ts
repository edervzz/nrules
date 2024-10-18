
const host = import.meta.env.VITE_API_URL_HOST + "/nr/api/" + import.meta.env.VITE_API_VER;

export const CREA_RULE = (tid: string) => `${host}/t/${tid}/rules`
export const READ_RULES_PAGE = (tid: string, no:string, size:string) => `${host}/t/${tid}/rules?pageNo=${no}&pageSize=${size}`
