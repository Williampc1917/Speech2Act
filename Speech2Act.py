import openai
import sounddevice as sd
import numpy as np
import subprocess
from scipy.io.wavfile import write
import configparser

openai.api_key = ''

# Function to load commands from a config file
# This allows for easy modification of commands without changing the main script.
def load_commands_from_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    # Returns a dictionary of commands where the keyword is mapped to a corresponding command
    return {keyword.strip(): command.strip() for keyword, command in config.items('Commands')}


# Function to record audio
# 'duration' is the length of the recording in seconds, 'fs' is the sampling frequency
def record_audio(duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    return recording


# Function to save the recording in file
def save_recording(recording, filename='output.wav', fs=44100):
    write(filename, fs, recording)


# Function to transcribe audio using OpenAI's API
def transcribe_audio(filepath):
    with open(filepath, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript


# Main function to listen and execute commands
def listen_and_execute():
    commands = load_commands_from_config()

    # Record
    audio_data = record_audio()
    save_recording(audio_data, 'output.wav')

    # Transcribe the audio file
    try:
        transcript = transcribe_audio('output.wav')
        text = transcript['text']
        print("Transcribed text:", text)

        # Check for specific commands and execute shell scripts accordingly
        for keyword, command in commands.items():
            if keyword.lower() in text.lower():
                subprocess.run(command, shell=True)
                print(f"{keyword.capitalize()} command executed.")
                break  # If keyword is found, stop looking for others

    # Add more commands as needed
    except Exception as e:
        print("An error occurred:", e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    listen_and_execute()
