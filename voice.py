from elevenlabs.client import ElevenLabs
from elevenlabs import save

from config import ELEVEN_API_KEY

client = ElevenLabs(
    api_key=ELEVEN_API_KEY
)


def get_voices():
    voices = client.voices.get_all()
    return voices.voices


def generate_audio(text, voice_id, output_path):
    audio = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
        model_id='eleven_multilingual_v2'
    )

    save(audio, output_path)