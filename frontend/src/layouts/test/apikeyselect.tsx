import react from 'react';
import Axios from "axios";
import { useAuth } from '../../auth-context/auth.context';

export default function Apikeyselect() {
    
    let user = useAuth();
    const TestApiCall = async () => {
        try {
            const response = await Axios.get('http://localhost:8000/api/test/giveapikey', { headers: { Authorization: `${user?.token}` }});
            console.log("response >>", response);
        } catch(err) {
            console.log("Error >>", err);
        }
    }

    return (
        <div>
            <button onClick={TestApiCall}>TestApiCall</button>
            <h1>apikeyselect</h1>
        </div>
    )
}