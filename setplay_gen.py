import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def open_URL_spit_songs(url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(3)  # wait for the JS to load

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    songs = [li.get_text(strip=True).removesuffix('Play Video') for li in soup.select("li.setlistParts.song")]

    # Load environment variables from .env
    load_dotenv()
    return songs 

def create_playlist(info,playlist_name):
    
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


    playlist = sp.user_playlist_create(user=user["id"], name=playlist_name,public=False)

    playlist_id = playlist["id"]
    
    artists = list(info.keys())
    for artist in artists:
        
        print(f'artist: {artist}\n')
        a = info[artist]
        for track in a['setlist']:
            query = f"track:{track} artist:{artist}"
            results = sp.search(q=query, type="track", limit=1)
            items = results["tracks"]["items"]
            
            if items:
                track_uri = items[0]["uri"]
                print(f"✅ Found: {track} → {track_uri}")
                sp.playlist_add_items(playlist_id, [track_uri])
            else:
                print(f"⚠️ Not found: {track}")
        print('--------------------------------')

    print(f"\n🎵 Done! Songs added to playlist: {playlist_name}")
    return None
    

# url = "https://www.setlist.fm/setlist/the-plot-in-you/2025/poppodium-013-tilburg-netherlands-3358a08d.html"

n_bands = input("How many bands? ")
info = {}
playlist_name = input("Enter playlist name: ")
for n in range(int(n_bands)):
    a = input(f"Enter artist {n+1} name: ")
    u = input(f"Enter artist {n+1} URL: ")
    
    info[a] = {'url':u, 'setlist': open_URL_spit_songs(u)}
    

create_playlist(info,playlist_name)





