import api from "../services/api";
import { useState } from "react";

function AnalyzeResume(){
    const [message,setMessage]=useState("");

    const getval=async()=>{
        try{
            const res= await api.get("/analyze_resume");
            const text=res.data.response;
            setMessage(text);

        }
        catch(err){
            console.log(err);
        }
    }
    return (
        <div>
            <button onClick={getval}>Analyze</button>
            <p>{message}</p>
        </div>
    )
}
export default AnalyzeResume