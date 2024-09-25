import requests as req

def link_to_mp3(link):
  headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
    'origin': 'https://spotifydown.com',
    'priority': 'u=1, i',
    'referer': 'https://spotifydown.com/'
    }
  
  response = req.get(url=link, headers=headers)
  return response.content

def get_song_info(id):
    spotifydown_headers = {
        'accept': 'application/json',
        'origin': 'https://spotifydown.com',
        'referer': 'https://spotifydown.com/'
    }
    
    spotifydown_api = 'https://api.spotifydown.com/download/' + id
    
    spotifydown_response = req.get(url=spotifydown_api, headers=spotifydown_headers)
    
    try:
        spotifydown_response_json = spotifydown_response.json() 
        return spotifydown_response_json
    except req.exceptions.JSONDecodeError:
        return {"error": "Invalid response format", "response": spotifydown_response.text}
