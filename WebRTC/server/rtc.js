// let localVideo = document.getElementById('localVideo');
// let remoteVideo = document.getElementById('remoteVideo');
// let localStream;
//
// navigator.mediaDevices.getUserMedia({
//     audio: false,
//     video: true,
// }).then(gotStream).catch(
//     (error) => console.error(error)
// )
//
// function gotStream(stream)
// {
//     localStream = stream;
//     localVideo.srcObejct = stream;
// }

const mediaStreamConstraints = {
    video: true,
    audio: true,
};

const localVideo = document.getElementById('localVideo');
let localStream;

function getLocalMediaStrea(mediaStream)
{
    localStream = mediaStream;
    localVideo.srcObject = mediaStream;
}

function handleLocalMediaStreamError(error)
{
    console.error('navigator.getUserMedia error', error);
}

navigator.mediaDevices.getUserMedia(
    mediaStreamConstraints
).then(getLocalMediaStrea).catch(handleLocalMediaStreamError);