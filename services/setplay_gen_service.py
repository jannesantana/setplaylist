import os
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from user_widget_service import get_playlist_input
from webscraping_service import open_URL_spit_songs



def create_playlist(info,playlist_name):
    
    """
    
    This function creates the playlist
    
    Input
    ---
    
    info : dictionary with the following structura info['artist name' (str)] = {'url' : (str), 'setlist' : list}
    
    Returns
    ---
    None
    
    """
    
    # ---- spotify autentication --- #
    
    scope = "playlist-modify-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=scope,
        cache_path=".cache-" + os.getenv("SPOTIPY_CLIENT_ID")
        
    ))
    # Check if authenticated
    user = sp.current_user()
    print(f"Authenticated as {user['display_name']}")


    playlist = sp.user_playlist_create(user=user["id"], name=playlist_name,public=False) # creates the playlist
    # ---------------------------- 

    playlist_id = playlist["id"] # playlist id
    
    artists = list(info.keys())
    for artist in artists:
        
        print(f'artist: {artist}\n')
        a = info[artist]
        for track in a['setlist']:
            query = f"track:{track} artist:{artist}"
            results = sp.search(q=query, type="track", limit=1) 
            items = results["tracks"]["items"] # loook for the track using query and sp.search
            
            if items: # checks if track is found
                track_uri = items[0]["uri"]
                print(f"✅ Found: {track} → {track_uri}")
                sp.playlist_add_items(playlist_id, [track_uri]) # adds it to the playlist
            else:
                print(f"⚠️ Not found: {track}")
        print('--------------------------------')

    print(f"\n🎵 Done! Songs added to playlist: {playlist_name}")
    return None
    





