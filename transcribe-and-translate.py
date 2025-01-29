import os
import asyncio
import whisper
import sqlite3
from googletrans import Translator

conn = sqlite3.connect('index.db')
cursor = conn.cursor()

ROOT_PATH = "<ROOT>"
ORIGINAL_WAV_ROOT = os.path.join(ROOT_PATH, "SPEECH")

missing_wavs = cursor.execute('SELECT * FROM wav_index WHERE english_value IS NULL OR english_value = \'\' ').fetchall()
print(f"Found {len(missing_wavs)} missing WAV files")
model = whisper.load_model("medium")


async def transcribe_wav(wav_file):
    result = model.transcribe(wav_file, language="pl")
    return result['text']


async def translate(text):
    async with Translator() as translator:
        x = await translator.translate(text, dest='en')
        return x.text


async def update_value(index, english_text, polish_text):
    cursor.execute('UPDATE wav_index SET english_value = ?, polish_value = ? WHERE id = ?', (english_text, polish_text, index))
    conn.commit()


async def main():
    for index, entry in enumerate(missing_wavs):
        transcript = await transcribe_wav(os.path.join(ORIGINAL_WAV_ROOT, f"{entry[3]}"))
        translated = await translate(transcript)

        await update_value(entry[0], translated, transcript)
        print(f"[{index}/{len(missing_wavs)}] Transcribed and translated {entry[1]}")


if __name__ == "__main__":
    asyncio.run(main())
