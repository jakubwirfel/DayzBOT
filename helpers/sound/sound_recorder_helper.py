from datetime import datetime
from time import sleep

import pyaudiowpatch as pyaudio
import wave

from logger import Logger


class SoundRecorderHelper:
    def __init__(self):
        self.duration = 10
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        file: str = f"recorded_sound{current_time}.wav"
        path = fr'C:\tmp\DayzBot'
        file_path = f"{path}\{file}"
        self.filename = file_path

    def record(self) -> str:
        with pyaudio.PyAudio() as p:
            try:
                # Get default WASAPI info
                wasapi_info = p.get_host_api_info_by_type(pyaudio.paWASAPI)
            except OSError:
                print("Looks like WASAPI is not available on the system. Exiting...")
                exit()

            # Get default WASAPI speakers
            default_speakers = p.get_device_info_by_index(wasapi_info["defaultOutputDevice"])

            if not default_speakers["isLoopbackDevice"]:
                for loopback in p.get_loopback_device_info_generator():
                    if default_speakers["name"] in loopback["name"]:
                        default_speakers = loopback
                        break
                else:
                    print(
                        "Default loopback output device not found.\n\nRun `python -m pyaudiowpatch` to check available "
                        "devices.\nExiting...\n")
                    exit()

            Logger.info(f"Recording from: ({default_speakers['index']}){default_speakers['name']}")
            wave_file = wave.open(self.filename, 'wb')
            wave_file.setnchannels(default_speakers["maxInputChannels"])
            wave_file.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
            wave_file.setframerate(int(default_speakers["defaultSampleRate"]))

            def callback(in_data, frame_count, time_info, status):
                wave_file.writeframes(in_data)
                return in_data, pyaudio.paContinue

            with p.open(format=pyaudio.paInt16,
                        channels=default_speakers["maxInputChannels"],
                        rate=int(default_speakers["defaultSampleRate"]),
                        frames_per_buffer=pyaudio.get_sample_size(pyaudio.paInt16),
                        input=True,
                        input_device_index=default_speakers["index"],
                        stream_callback=callback
                        ) as stream:
                sleep(self.duration)
            wave_file.close()
            Logger.info("Sound recorded")
            return self.filename
