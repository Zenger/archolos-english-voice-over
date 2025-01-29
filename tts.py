import os

from TTS.api import TTS
import sqlite3, json
conn = sqlite3.connect("index.db")
cursor = conn.cursor()

raw_speech_path = "<root>/SPEECH"
translated_speech_path = "<root>/translated"
wav_index = cursor.execute("SELECT * FROM wav_index").fetchall()

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)
try:
    for index, line in enumerate(wav_index):
        text = line[2]
        wav = line[3]
        if os.path.exists( os.path.join(translated_speech_path, wav)):
            print(f"{wav} exists")
            continue
        if text and len(text) > 2:
            try:
                tts.tts_to_file(
                    text=text,
                    file_path=os.path.join(translated_speech_path, wav),
                    speaker_wav=[os.path.join(raw_speech_path, wav)],
                    language="en",
                    split_sentences=True,
                )
            except:
                print(f"Failed to translate {wav}")
        print(f"[{index}/{len(wav_index)}] {wav} translated")
except Exception as e:
    print(e)
