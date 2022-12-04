import numpy as np
import soundfile as sfile

from logger import Logger


class SoundRecognizeHelper:

    @classmethod
    def recognize(cls, wav_file: str) -> int:
        filename = wav_file

        signal, sr = sfile.read(filename)

        try:
            samples_sf = signal[:, 0]
        except:
            samples_sf = signal

        data = [cls.__convert_to_decibel(i) for i in samples_sf]
        counter = 0
        max_dB = max(data)
        Logger.info(f"Max Db: {max_dB}; Min dB: {min(data)}")
        for item in data:
            if max_dB >= item >= max_dB - 1.5 and max_dB >= -28:
                counter += 1

        Logger.info(f"Find {counter} sounds")

        return counter

    @staticmethod
    def __convert_to_decibel(arr):
        ref = 1
        if arr != 0:
            return 20 * np.log10(abs(arr) / ref)
        else:
            return -60
