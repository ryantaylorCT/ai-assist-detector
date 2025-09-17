let mediaRecorder;
let audioChunks = [];

const startBtn = document.getElementById('start');
const stopBtn = document.getElementById('stop');
const analyzeBtn = document.getElementById('analyze');
const resultPre = document.getElementById('result');

startBtn.onclick = async () => {
    audioChunks = [];
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert('Your browser does not support audio recording');
        return;
    }
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = (event) => {
            if (event.data.size > 0) {
                audioChunks.push(event.data);
            }
        };
        mediaRecorder.start();
        startBtn.disabled = true;
        stopBtn.disabled = false;
        analyzeBtn.disabled = true;
        resultPre.textContent = '';
    } catch (err) {
        console.error(err);
        alert('Could not start recording: ' + err.message);
    }
};

stopBtn.onclick = () => {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
        startBtn.disabled = false;
        stopBtn.disabled = true;
        analyzeBtn.disabled = false;
    }
};

analyzeBtn.onclick = async () => {
    if (audioChunks.length === 0) {
        return;
    }
    const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.webm');
    resultPre.textContent = 'Analyzing...';
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        resultPre.textContent = JSON.stringify(data, null, 2);
        analyzeBtn.disabled = true;
    } catch (err) {
        console.error(err);
        resultPre.textContent = 'Error analyzing audio: ' + err.message;
    }
};
