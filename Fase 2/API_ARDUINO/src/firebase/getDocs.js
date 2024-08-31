import { db } from './firebase.js';
import { collection, getDocs, query, orderBy } from "firebase/firestore";

const collectionReference = collection(db, "test-collection")
 
/**
 * Retorna un array con todos los registros de la colección
 */
export const getTestDocs = async () => {
    try {
        // const q = query(collectionReference, orderBy("Fecha", "desc"));
        const q = query(collectionReference);
        const querySnapshot = await getDocs(q);
        return querySnapshot; 
        // querySnapshot.forEach((doc) => {
        //    //console.log(`${doc.id} => ${doc.data()}`);
        // });
    } catch (error) {
        throw new Error(error);
    }
}