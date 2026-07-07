
import { useState } from "react";
import api from "../services/api"

function ChatBox(){
   const [message,setMessage]=useState("");
   const [messages,setMessages]=useState([]);
   const [checkStatus,setStatus]=useState("");
   const [checkprogress,setProgress]=useState("");

   const sendmsg=async()=>{
    try{
    const idres= await api.get("/id");
    const id =idres.data.task_id;
    const socket=new WebSocket(`ws://localhost:8000/ws/${id}`);

    socket.onopen=async () =>{
        if(!message.trim()) return;
        const userMsg={
        role:"User",
        text:message
        }
    setMessages(prev => [...prev,userMsg,{
        role:"Assistant",
        text:""
    }]);
    const res = await fetch(
    "http://localhost:8000/stream",
    {
        method: "POST",
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            message: message,
            task_id:id
        })
    }
);
setMessage("");
 const reader=res.body.getReader();
 const decoder=new TextDecoder();
    alert("Connected");
    var str="";

    while(true){
        
        const {done,value}=await reader.read();
        if(done)break;
        str=str+decoder.decode(value);
        setMessages(prev => {
            const updated=[...prev];
            updated[updated.length-1] ={
                role:"Assistant",
                text:str
            }
            return updated;
        })
    }
}
   socket.onmessage=(event)=>{
    const data=JSON.parse(event.data)
    if(data.progress!==undefined){
        console.log('Connected!');
        setProgress(data.progress);
    }
    if(data.status){
        console.log("Status Working!");
        setStatus(data.status);
    }
    if(data.status==="completed"){
        socket.close();
    }
   }
   socket.onerror=(err)=>{
    console.log("Error",err);
   }
   socket.onclose=()=>{
    console.log("Stopped Working!");
   }
 }
    catch(err){
    console.log(err);
}
   };
   return (
    <div>
        <h2>Chat</h2>
        <div>
            {messages.map((msg,index)=>(
                <div value={index}>
                    <b>{msg.role}</b>
                    <p>{msg.text}</p>
                </div>
            ))}

        </div>
        <input value={message} onChange={(e)=>setMessage(e.target.value)}/>
        <button onClick={sendmsg}>Send</button>
        <p>Status: {checkStatus}</p>
        <p>Progress: {checkprogress}%</p>
    </div>
   )
}

export default ChatBox;