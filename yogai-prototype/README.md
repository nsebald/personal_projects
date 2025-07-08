# YogAI Prototype 🧘‍♀️

## Purpose
This app helps create a yoga class tailored to specific injuries or discomforts. It identifies common physical issues and suggests appropriate yoga poses. These poses are then scripted and converted into an audio class for a guided yoga session.

## Application Flow
1. **User Input**: User enters their injury or physical discomfort in the web interface
2. **Medical Analysis**: The app uses OpenAI GPT-3.5 to analyze the injury and identify underlying weaknesses
3. **Pose Recommendation**: Based on the analysis, the system generates 3 specific yoga poses that can help address the issue
4. **Visual Resources**: For each recommended pose, the app fetches relevant images from Pexels API
5. **Class Scripting**: OpenAI generates a guided yoga class script focusing on one of the recommended poses
6. **Audio Generation**: ElevenLabs converts the script into natural-sounding speech audio
7. **Results Delivery**: The app returns the diagnosis, pose images, and audio file URL to the user

## API Usage
- **OpenAI**: Used for generating textual content (medical analysis, pose recommendations, and class scripting).
- **Pexels**: An image database utilized for visual resources of yoga poses.
- **Eleven Labs**: Provides text-to-speech conversion services. I also experimented with using my own voice samples for fun, which turned out to be a unique experience.

## Contents
1. `app.py`: Main Flask application script handling server and route configurations.
2. `constants.py`: Stores API keys (ensure these are kept secret).
3. `index.html`: Contains HTML and JavaScript for the app's frontend.
4. `Gen AI Project-Video Tutorial`: Walkthrough video demonstrating the app's functionality.
5. `Yoga.ipynb`: Jupyter notebook used to develop and test app functions.
6. `requirements.txt`: Python dependencies needed to run the application.

## How to Use
Begin with the "Gen AI Project-Video Tutorial" to familiarize yourself with the app's functionality.

## Running the App
1. Install dependencies: `pip install -r requirements.txt`
2. Open your terminal.
3. Change the directory to the project folder.
4. Execute `python app.py`.
5. Copy the server link, typically something like `http://127.0.0.1:5000`.
6. On the website, enter the specific injury.
7. Download the audio file (will download in browser) and enjoy your yoga class!

## Technical Flow Details
- The app uses Flask routes to handle web requests
- POST request to `/get_poses` triggers the entire AI pipeline
- Error handling is implemented for API timeouts and failures
- Audio files are saved to the static directory for web serving
- The frontend displays results dynamically using JavaScript

## Features
- 🤖 AI-powered injury analysis
- 🧘‍♀️ Personalized yoga pose recommendations
- 🖼️ Visual pose demonstrations
- 🎤 Audio-guided yoga classes
- 🌐 Web-based interface

## Security Note
⚠️ **Important**: The `constants.py` file contains API keys and is excluded from version control via `.gitignore`. For production use, consider using environment variables for better security. 