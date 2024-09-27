import i18next from 'i18next';
import * as enCommon from './en.json';
import * as esCommon from './es.json';

export const defaultNS = 'common'; // Default name space

i18next.init({
    lng: 'en', 
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
