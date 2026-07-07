import ChatBox from "./components/ChatBox";
import ResumeUpload from "./components/ResumeUpload";
import AnalyzeResume from "./components/AnalyzeResume";
import VoiceRecorder from "./components/VoiceRecorder";

function App(){
  return (
    <div>
      <h1>AI Carrer Host</h1>
      <ResumeUpload/>
      <AnalyzeResume/>
      <ChatBox/>
      <VoiceRecorder/>
    </div>
  );
}

export default App;