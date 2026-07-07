import { useState,useRef } from "react";
import api from "../services/api"

function VoiceRecorder(){
    const [recording,setRecorder]=useState(false);
    const mediaRecorderRef=useRef(null);
    const chunks=useRef([]);
    const [audioUrl,setUrl]=useState("");
    //const [messages,setMessages]=useState("");
    const [ttsurl,setTtsUrl]=useState("");
    const [speaking,setSpeaking]=useState(false);
    const startRecording= async () =>{
        try{
            const stream=await navigator.mediaDevices.getUserMedia(
                {
                    audio:true
                }
            );
            const mediaRecorder=new MediaRecorder(stream);
            mediaRecorderRef.current=mediaRecorder;
            chunks.current=[];
            mediaRecorder.ondataavailable=(event)=>{
                if(event.data.size>0){
                    chunks.current.push(
                        event.data
                    );
                }
            }
            mediaRecorder.onstop= async ()=>{
                const audioblob=new Blob(
                    chunks.current,
                    {
                        type:"audio/webm"
                    }
                )
                 const url=URL.createObjectURL(audioblob);
                 setUrl(url);
                 alert("audio made!")
                 console.log(audioblob);
                 const formdata=new FormData();
                 alert("Created");
                 formdata.append("audio",audioblob,"recording.webm");
                 alert("Form Created");
                 const response=await api.post("/transcribe",formdata);
                 alert("Request Sent!");
                 const data=response.data;
                 const ttsres=await fetch("http://localhost:8000/gtts",
                    {
                        method:"POST",
                        headers:{
                            "Content-Type": "application/json"
                        },
                        body:JSON.stringify(response.data)
                    }

                 )
                 const blob= await ttsres.blob();
                 const ttsaudio=URL.createObjectURL(blob);
                 setTtsUrl(ttsaudio);
                 console.log(data);
                 /*
                 const streamRes=await fetch(
                    "http://localhost:8000/stream",
                    {
                        method:"POST",
                        headers:{
                            "Content-Type":"application/json"
                        },
                        body:JSON.stringify(response.data)
                    }
                 )
                 const reader=streamRes.body.getReader();
                 const decoder=new TextDecoder();
                 var str="";
                 while(true){
                    const {done,value}=await reader.read();
                    if(done)break;
                    str=str+decoder.decode(value);
                    setMessages(str);
                 }
                    */
                 

            };
            mediaRecorder.start();
            setRecorder(true);
           
        }
        catch(err){
            console.log(err);
        }
    }
    const stopRecording=()=>{
        mediaRecorderRef.current.stop();
        setRecorder(false)

    }
    return (
        <div>

            <h2>Voice Recorder</h2>

            {!recording ? (
                <button onClick={startRecording}>
                    Start Recording
                </button>
            ) : (
                <button onClick={stopRecording}>
                    Stop Recording
                </button>
            )}

            {audioUrl && (
                <audio
                    controls
                    src={audioUrl}
                />
            )}
            {ttsurl && (
    <audio
        key={ttsurl}
        controls
        src={ttsurl}
        onPlay={()=>setSpeaking(true)}
        onEnded={()=>setSpeaking(false)}
        onPause={()=>setSpeaking(false)}
    />
)}
{speaking && (
    <p>AI is Speaking...</p>
)}

        </div>
    );

}

export default VoiceRecorder