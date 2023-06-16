import react, {useState} from 'react';
import Axios from "axios";
import { useAuth } from '../../auth-context/auth.context';

export default function Apikeyselect() {
    
    let user = useAuth();
    const [apikey, setApikey] = useState<string>("");
    const [apikey2, setApikey2] = useState<string>("");
    const [testresult, setTestResult] = useState<string>("");

    // const [value, setValue] = useState<string>("");

    const hangapikeychange = (event:any) => {
        setApikey2(event.target.value);
    };
    const CreateApiCall = async () => {
        try {
            const response = await Axios.get('http://localhost:8000/api/test/giveapikey', { headers: { Authorization: `${user?.token}` }});
            console.log("response >>", response);
            setApikey(response.data.apikey);
            setApikey2(response.data.apikey);
        } catch(err) {
            console.log("Error >>", err);
        }
    }

    const TestApiCall = async () => {
        try {
            const response = await Axios.get('http://localhost:8000/api/test/testapikey?apikey='+apikey2, { headers: { Authorization: `${user?.token}` }});
            console.log("response >>", response);
            setTestResult(response.data);

        } catch(err) {
            setTestResult("테스트 실패");
            console.log("Error >>", err);
        }
    }

    return (
        <div>
            <button onClick={CreateApiCall}>apiKey발급</button>
            <h1>apikeyselect</h1>
            <h1>api키 : {apikey}</h1>

            <div>
            <input type="text" value={apikey2} onChange={hangapikeychange} width="400"/>
            <p>입력된 값: {apikey2}</p>
            <h3>접근주소: http://localhost:8000/api/test/testapikey?apikey={apikey2}</h3>
            </div>
            <button onClick={TestApiCall}>apiKey테스트</button>
            <h1>테스트결과 : {testresult}</h1>
        </div>
    )
}