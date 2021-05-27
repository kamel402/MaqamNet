const recorder = document.getElementById('recorder');
const player = document.getElementById('player');

const button = document.getElementById('recButton');
const sbutton = document.getElementById('stoButton');
var rec = false
var audiourl

document.addEventListener('DOMContentLoaded', function () {
    sbutton.style.display = "none";
});


recorder.addEventListener('change', function (e) {
    const file = e.target.files[0];
    const url = URL.createObjectURL(file);
    // Do something with the audio file.
    player.src = url;
});


const recordAudio = () =>
    new Promise(async resolve => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true, video: false });
        const mediaRecorder = new MediaRecorder(stream);
        const audioChunks = [];

        mediaRecorder.addEventListener("dataavailable", event => {
            audioChunks.push(event.data);
        });

        const start = () => mediaRecorder.start();

        const stop = () =>
            new Promise(resolve => {
                mediaRecorder.addEventListener("stop", () => {
                    const audioBlob = new Blob(audioChunks);
                    const audioUrl = URL.createObjectURL(audioBlob);
                    audiourl = audioUrl;
                    const audio = new Audio(audioUrl);
                    const play = () => audio.play();
                    resolve({ audioBlob, audioUrl, play });
                });

                mediaRecorder.stop();
            });

        resolve({ start, stop });
    });

const sleep = time => new Promise(resolve => setTimeout(resolve, time));

sbutton.addEventListener('click', function () {
    button.style.display = "block";
    sbutton.style.display = "none";
    rec = true;
});
button.addEventListener('click', function () {
    sbutton.style.display = "block";
    button.style.display = "none";
    (async () => {
        const recorder = await recordAudio();
        recorder.start();
        while (rec == false) {
            await sleep(10);
        }
        const audio = await recorder.stop();
        player.src = audiourl;
    })();
    rec = false;
})