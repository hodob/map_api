import react, {useState} from 'react';
import Axios from "axios";
import { useAuth } from '../../auth-context/auth.context';


interface DataTableProps {
    data: {
      key: string;
      category: string;
    }[];
  }
  
  const DataTable:React.FC<DataTableProps> = ({ data }) => {
    console.log(...data)
    return (
        <>
         {data.map((item, index) => (
        <div key={index}>
          <p>Key: {item.key}</p>
          <p>Category: {item.category}</p>
        </div>
      ))}
        </>
    );
  };


export default function ApiSelect(){
    let user = useAuth();
    const [apikey, setApikey] = useState<string>("");
    const [apikey2, setApikey2] = useState<string>("");
    const [testresult, setTestResult] = useState<any>("");

    // const [value, setValue] = useState<string>("");

    const hangapikeychange = (event:any) => {
        setApikey2(event.target.value);
    };
    
    const CreateApiCall = async () => {
        try {
            const response = await Axios.post('http://localhost:8000/api/users/apis', { headers: { Authorization: `${user?.token}` }});
            console.log("response >>", response.data);
            setApikey(response.data.key);
            setApikey2(response.data.key);
        } catch(err) {
            console.log("Error >>", err);
        }
    }

    const TestApiCall = async () => {
        try {
            const response = await Axios.get('http://localhost:8000/api/users/apis', { headers: { Authorization: `${user?.token}` }});
            console.log("response >>", response);
            setTestResult(response.data);
        } catch(err) {
            setTestResult("테스트 실패");
            console.log("Error >>", err);
        }
    }
    return(
        <div>
            <button onClick={CreateApiCall}>apiKey발급</button>
            <h1>apikeyselect</h1>
            <h1>api키 : {apikey}</h1>
            <button onClick={TestApiCall}>apiKey목록</button>
            {/* <h1>테스트결과 : {testresult}</h1> */}
            <DataTable data={testresult} />
        </div>
    )
}