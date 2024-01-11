import soundcard as sc
import soundfile as sf
import numpy as np
from tqdm import tqdm

OUTPUT_FILE_NAME = "out.wav"    # file name.
SAMPLE_RATE = 16000              # [Hz]. sampling rate.


def get_rt_syssound():
    data = []
    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        # record audio with loopback from default speaker.
        try:
            while True:
                data_t = mic.record(numframes=SAMPLE_RATE)
                # print(data)
                # print(type(data))
                print(data_t.shape)
                data.extend(data_t)
        except KeyboardInterrupt:
            data= np.array(data)
            print(data.shape)
            # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
            sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)

def get_syssound():
    data = []
    RECORD_SEC = int(input("how many seconds wanted to record : "))
    with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
        for i in tqdm(range(RECORD_SEC)):
            data_t = mic.record(numframes=SAMPLE_RATE)
            data.extend(data_t)
        data= np.array(data)
        sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)

if __name__ == "__main__":
    get_syssound()
