import { Festival } from './Festival';


export interface FestivalResponse {
    status: string;
    hash: string;
    username: string;
    suggestions: Array<Festival>;
}
