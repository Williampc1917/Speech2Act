# Speech2Act

'Speech2Act' is an innovative tool that bridges the gap between spoken language and action, enabling users to control their computer through voice commands. Utilizing the cutting-edge capabilities of OpenAI's Speech to Text API, which is powered by the robust Whisper model, 'Speech2Act' listens to user-defined commands and executes corresponding actions on their computer. Whether you're opening software, controlling playback, or managing system tasks,'Speech2Act' provides a seamless, hands-free computing experience. 


## Features

- Voice Command Recognition: Leverages OpenAI's Speech to Text API for accurate transcription of audio to text.
- Customizable Actions: Users can define what actions are triggered by specific voice commands.
- Adaptable Listening Duration: The duration for which the program listens can be adjusted as per user preference.
- Dynamic Command Execution: Execute shell commands or scripts directly based on the spoken words.
- User-Friendly Configuration: Simple configuration file setup for non-technical users to specify command keywords and associated actions.


## How It Works

  1. Setup: Users configure the config.ini file with the desired voice command keywords and their corresponding shell commands or script actions.
  2. Listening: By default, the program listens for a predefined time window (configurable by the user) for voice input.
  3. Transcription: The recorded audio is sent to OpenAI's API and transcribed using the Whisper model.
  4. Command Execution: When a voice command keyword is recognized in the transcribed text, speech2Act executes the associated command.
## Configuration

Speech2Act uses a simple INI file format for command configuration. Users can define their commands and the corresponding actions in the config.ini file like this:

```bash
[Commands]
open matlab = /usr/local/MATLAB/R2023b/bin/matlab
play music = vlc ~/Music
open browser = firefox
```



## Requirements

- Python 3.x
- OpenAI API Key(with acccess to the Speech To Text API)
- SoundDevice and SciPy (for audio recording and handling)
- ConfigParser (for cofiguration management)
## License

[MIT](https://choosealicense.com/licenses/mit/)
