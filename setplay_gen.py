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
from user_widget import get_playlist_input





def open_URL_spit_songs(url): 
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(3)  # wait for the JS to load

    soup = BeautifulSoup(driver.page_source, "html.parser")
    artist = soup.find("meta", property="qc:artist")
    driver.quit()

    songs = [li.get_text(strip=True).removesuffix('Play Video') for li in soup.select("li.setlistParts.song")]

    return artist["content"],songs 

def create_playlist(info,playlist_name):
    
    scope = "playlist-modify-private"
    # print(os.getenv("SPOTIPY_CLIENT_ID"))
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

# print("Hello! Welcome to setplaylist! \n \n Start by entering the playlist's name, then enter the setlist's URL. \n \n When you're finished, type END.")

info = {}
playlist_name, urls = get_playlist_input()

if playlist_name is None:
    print("User cancelled.")
# else:
#     print("playlist name =", playlist_name)
#     print("urls =", urls)
# playlist_name = input("Enter playlist name: ")

for u in urls:
    if not (u.startswith("http://") or u.startswith("https://")):
        print("Invalid URL (must start with http:// or https://)")
        continue
    a,s = open_URL_spit_songs(u)
    info[a] = {'url':u, 'setlist': s}
    

# while True:
#     u = input(f"Enter artist URL or END to finish creating: ")
#     if u.upper() == "END":
#         break
#     if not (u.startswith("http://") or u.startswith("https://")):
#         print("Invalid URL (must start with http:// or https://)")
#         continue
#     a, s = open_URL_spit_songs(u)
#     info[a] = {'url':u, 'setlist': s}
    
    
    
    
    
    
print("Great! Creating your setplaylist...")

create_playlist(info,playlist_name)





