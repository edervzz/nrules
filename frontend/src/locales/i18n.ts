import i18next from 'i18next';
import * as enCommon from './en.json';
import * as esCommon from './es.json';
import Vars from '../vars';

export const defaultNS = 'common'; // Default name space

i18next.init({
    lng: Vars.language, 
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

export function changeLocale(newLangu: string){
    i18next.changeLanguage(newLangu);
    Vars.language=newLangu;
}
