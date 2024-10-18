import i18next from 'i18next';
import * as enCommon from './en.json';
import * as esCommon from './es.json';
import MyVars from '../myvars';

export const defaultNS = 'common'; // Default name space

i18next.init({
    lng: MyVars.language, 
    fallbackLng: 'en', 
    debug: true, // Enable debug mode (optional)
    resources: {
        en: {
            common: enCommon,
        },
        es: {
            common: esCommon,
        },
    },
});

export default i18next;

export function switchLocale(){
    const currentLangu = MyVars.language;
    const newLangu =  currentLangu == "es" ? "en" : "es";
    i18next.changeLanguage(newLangu);
    MyVars.language=newLangu;
}
