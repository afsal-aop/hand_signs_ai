const video = document.getElementById("video");
const output = document.getElementById("output");

navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
  video.srcObject = stream;
  setInterval(sendFrame, 1000); // every 1s
});

function sendFrame() {
  const canvas = document.createElement("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0);
  const image = canvas.toDataURL("image/jpeg");

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: image })
  })
  .then(res => res.json())
  .then(data => {
    output.innerText = `Prediction: ${data.prediction}`;
  });
}
