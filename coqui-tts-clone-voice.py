import torch
from TTS.api import TTS
import gradio as gr

device = "cuda" if torch.cuda.is_available() else "cpu"


text_to_speech = """

"""


multilingual = "tts_models/multilingual/multi-dataset/xtts_v2"

voz_a_clonar = ""
output_path = ""
language = ""

def generate_audio_copy_voice():
    tts = TTS(model_name=multilingual).to(device)
    tts.tts_to_file(text=text_to_speech, speaker_wav=voz_a_clonar, file_path=output_path, language=language)
    return output_path

print(generate_audio_copy_voice())