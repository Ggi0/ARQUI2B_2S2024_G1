import { db } from './firebase.js';
import { collection, getDocs, query, orderBy } from "firebase/firestore";

const collectionReference = collection(db, "arduino-collection");
 
/**
 * Retorna un array con todos los registros de la colección
 */
export const getSensorDocs = async () => {
    try {
        // const q = query(collectionReference, orderBy("Fecha", "desc"));
        const q = query(collectionReference, orderBy("timestamp", "desc"));
        const querySnapshot = await getDocs(q);
        return querySnapshot;
    } catch (error) {
        throw new Error(error);
    }
}