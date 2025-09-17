document.addEventListener('DOMContentLoaded', function() {
  const startButton = document.getElementById('start-btn');
  const stopButton = document.getElementById('stop-btn');
  const analyzeButton = document.getElementById('analyze-btn');
  const resultDiv = document.getElementById('result');
  let mediaRecorder;
  let audioChunks = [];

  startButton.onclick = async () => {
    audioChunks = [];
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (e) => {
      audioChunks.push(e.data);
    };
    mediaRecorder.start();
    startButton.disabled = true;
    stopButton.disabled = false;
    analyzeButton.disabled = true;
  };

  stopButton.onclick = () => {
    mediaRecorder.stop();
    mediaRecorder.onstop = () => {
      startButton.disabled = false;
      stopButton.disabled = true;
      analyzeButton.disabled = false;
    };
  };

  analyzeButton.onclick = async () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
    const formData = new FormData();
    formData.append('file', audioBlob, 'recording.webm');

    resultDiv.textContent = 'Analyzing...';

    try {
      const response = await fetch('/analyze', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      resultDiv.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
      resultDiv.textContent = 'Error analyzing audio';
    }
  };
});
