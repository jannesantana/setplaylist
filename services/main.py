from webscraping_service import open_URL_spit_songs
from setplay_gen_service import create_playlist
from user_widget_service import get_playlist_input


info = {}
playlist_name, urls = get_playlist_input() # uses the widget script and picks up the urls and the playlist name 

if playlist_name is None:
    print("User cancelled.")


for u in urls:
    if not (u.startswith("http://") or u.startswith("https://")):
        print("Invalid URL (must start with http:// or https://)")
        continue
    a,s = open_URL_spit_songs(u) # opens the urls and picks up the artist name and the list with the songs
    info[a] = {'url':u, 'setlist': s}
    

    
    
print("Great! Creating your setplaylist...")

create_playlist(info,playlist_name) 