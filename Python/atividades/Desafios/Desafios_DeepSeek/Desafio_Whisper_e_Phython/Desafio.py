from IPython.display import Audio, display, JavaScript
from google.colab import output
from base64 import b64decode    

RECORD = """
const sleep = time => new Promise(resolve => setTimeout(resolve, time));

const b2text = blob => new Promise(resolve => {
    const reader = new FileReader();
    reader.onloadend = e => resolve(e.target.result);
    reader.readAsDataURL(blob);
});

var record = time => new Promise(async resolve => {
    let stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    let recorder = new MediaRecorder(stream);
    let chunks = [];

    recorder.ondataavailable = e => chunks.push(e.data);

    recorder.onstop = async () => {
        let blob = new Blob(chunks);
        let text = await b2text(blob);
        resolve(text);
    };

    recorder.start();
    await sleep(time);
    recorder.stop();
});
"""

def record(sec=5):
    display(JavaScript(RECORD))
    js_result = output.eval_js(f'record({sec * 1000})')
    audio = b64decode(js_result.split(',')[1])
    file_name = 'request_audio.wav'
    with open(file_name, 'wb') as f:
        f.write(audio)
    return f'/content/{file_name}'

print('Ouvindo....\\n')
record_file = record()
display(Audio(record_file, autoplay=True))
