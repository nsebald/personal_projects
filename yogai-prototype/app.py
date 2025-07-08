from flask import Flask, request, jsonify, render_template, send_file, url_for
import openai
import requests
from elevenlabs.client import ElevenLabs
import os

app = Flask(__name__)
# At the top of your app.py file, you can write:
from constants import API_KEY, PEXELS_API, ELEVEN_API

# And then use them in your code like so:
openai.api_key = API_KEY
pexels_api_key = PEXELS_API
elevenlabs_api_key = ELEVEN_API


def doctor(query):

    # Create the client with params for OpenAI API
    """
    Data generation with Open AI
    """
    prompt = (
        """
        You are a physiologist. Determine what weaknesses could exist in the body that led to the injury. Give me one response listing a body part and weakness. The response should be a short, single phrase. The injury is:
        """
        + query
    )

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct", #we use the gpt 3.5 instruct for this task (the smallest one and only completion)
        prompt=prompt,
        max_tokens=1000, # max tokens for the response for your ask prompting
        temperature=0,  # 0 to 1 by  step of 0.1 O deterministic, 1 is very creative
    )

    result = response.choices[0].text

    return result

def yogi_poses(query):

    # Create the client with params for OpenAI API

    """
    Data generation with Open AI
    """
    prompt = (
        """
        You are a yogi expert. Determine 3 yoga poses that can help resolve the following issue. Output format is a list of poses. The issue is:
        """
        + query
    )

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct", #we use the gpt 3.5 instruct for this task (the smallest one and only completion)
        prompt=prompt,
        max_tokens=1000, # max tokens for the response for your ask prompting
        temperature=0,  # 0 to 1 by  step of 0.1 O deterministic, 1 is very creative
    )

    result = response.choices[0].text

    

    return result


def search_images(pexels_api_key, queries, per_page=10, page=1):
    """Search for images using the Pexels API for multiple search terms."""
    url = 'https://api.pexels.com/v1/search'
    headers = {'Authorization': pexels_api_key}
    query_photos = {}  # Using a dictionary to associate photos with their queries

    for query in queries:
        params = {
            'query': query,
            'per_page': per_page,
            'page': page
        }
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                query_photos[query] = [photo['src']['original'] for photo in data['photos']]
            else:
                print(f"Failed to fetch data for {query}: {response.status_code}")
        except requests.exceptions.Timeout:
            print("Request to Pexels API timed out.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    return query_photos


def yoga_class(query):

    # Create the client with params for OpenAI API

    ClientOpenAi = openai.OpenAI(
            api_key= openai.api_key,
            organization= openai.organization
        )
    """
    Data generation with Open AI
    """
    prompt = (
        """
        Craft a monologue-driven script of a yoga class from the perspective of the intructor. Just include the speech from the instructor. Emphasize clear, instructional language that details how to safely enter and hold each pose, including any necessary adjustments or alignment cues. Incorporate motivational and affirming statements to encourage participants throughout the practice. Use just one pose to create a short class. Don't  mention the instructor's name.
        """
        + query
    )

    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct", #we use the gpt 3.5 instruct for this task (the smallest one and only completion)
        prompt=prompt,
        max_tokens=200, # max tokens for the response for your ask prompting
        temperature=.5,  # 0 to 1 by  step of 0.1 O deterministic, 1 is very creative
    )

    result = response.choices[0].text

    return result


def generate_audio(script, voice):
    client = ElevenLabs(api_key=elevenlabs_api_key)
    audio_data_generator = client.generate(text=script, voice=voice)
    audio_data = b"".join(audio_data_generator)
    
    # Specify just the filename, not the path
    audio_filename = 'output_audio.mp3'
    audio_file_path = os.path.join('static', audio_filename)
    
    with open(audio_file_path, 'wb') as audio_file:
        audio_file.write(audio_data)

    # Return the filename only, not the full path
    return audio_filename



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_poses', methods=['POST'])
def get_poses():
    injury = request.form.get('injury')
    diagnosis = doctor(injury)
    pose_response = yogi_poses(diagnosis)

    pose_lines = [line.strip() for line in pose_response.split('\n') if line.strip()]
    pose_list = [line.split('. ', 1)[1] if '. ' in line else line for line in pose_lines]
    photos_dict = search_images(pexels_api_key, pose_list, 1, 1)

    script = yoga_class(diagnosis)
    audio_file_path = generate_audio(script, voice="BqyrAbIbkSyoI8Crkpfl")
    audio_url = url_for('static', filename=audio_file_path, _external=True)

    # Consider adding error handling for each step and return appropriate error messages if needed
    return jsonify({'diagnosis': diagnosis, 'photos_dict': photos_dict, "audio_file_path": audio_url})


# @app.route('/get_audio', methods=['POST'])
# def get_audio():
#     injury = request.form.get('injury')
#     if not injury:
#         return jsonify({'error': 'No injury provided'}), 400

    

#     # Send the audio file for download
#     return send_file(audio_file_path, as_attachment=True)



# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)  # host='0.0.0.0' makes the server publicly available on your network
