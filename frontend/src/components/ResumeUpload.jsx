import { useState} from "react";
import api from "../services/api";

function ResumeUpload(){
    const [file,setFile]=useState(null);
    const [checkStatus,setStatus]=useState("");
    const [progress,setProgress]=useState("");

    const setResume=async()=>{
        
        const idres=await api.get("/id")
        const id=idres.data.task_id
        //const currStatus=await api.get(`/status/${id}`)
        //setStatus(currStatus.data.status)
        //setProgress(currStatus.data.progress)
        const socket=new WebSocket(`ws://localhost:8000/ws/${id}`);
        socket.onopen= async()=>{
             const formData=new FormData();
             formData.append("file",file);
             formData.append("task_id",id);
             await api.post("/upload_resume",formData);
            console.log("Connected!");
        };
        socket.onmessage=(event)=>{
            const data=JSON.parse(event.data)
            if(data.progress!==undefined){
                console.log("Progress Working");
                setProgress(data.progress)
            }
            
            if(data.status){
                console.log("Status Working");
                setStatus(data.status)
            }
            if(data.status==="completed"){
                socket.close();
            }

        }
        socket.onerror=(err)=>{
            console.log("Error",err)

        }
        socket.onclose=()=>{
            console.log("Close");
        }
    }

    return (
        <div>
            <h2>Resume Upload</h2>
            <input type="file" onChange={(e)=>setFile(e.target.files[0])} />
            <button onClick={setResume}>Upload</button>
            <p>Status: {checkStatus}</p>
            <p>Progress: {progress}%</p>
        </div>
    )
}

export default ResumeUpload;