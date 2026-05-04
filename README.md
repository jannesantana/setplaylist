# Setlist.fm → Spotify Playlist Generator

A Python application that converts concert setlists from setlist.fm into playable playlists on Spotify.

The user provides a setlist URL and a playlist name. The app extracts the songs, matches them to Spotify tracks, and creates a playlist automatically.

Being a big fan of live music, everytime I go to a concert, I like to create a playlist containing the approximate setlist of each concert from setlist.fm. However, as a metalhead, this process was very lengthy since metal concerts usually have 2-3 openers and 1-2 headlines. So I decided to automate this process. 

# Features
* Extract artist and song list from a Setlist.fm page
* Match songs to Spotify tracks
* Automatically create a Spotify playlist
* Simple user interface (widget-based input)
* Modular code structure (scraping, matching, playlist generation separated)


# Project Structure
```
├── setplay_gen_service.py      # Spotify interaction (playlist creation)
├── webscraping_service.py      # Setlist.fm scraping
├── user_widget_service.py      # User interface (input/output)
├── main.py                     # Orchestrates the workflow
├── requirements.txt
└── README.md
```

# Installation

1. Clone the repository
2. Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
3. Install dependencies `pip install -m requirements.txt`

# Spotify Setup

This project uses the Spotify Web API via Spotipy.

1. Go to the Spotify Developer Dashboard
2. Create an application
3. Get your:
```
CLIENT_ID
CLIENT_SECRET
```
4. Set a redirect URI (e.g. http://localhost:8888/callback)

5. Create a .env file:
```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

# Usage

1. Run the application: `python main.py`
2. Enter the playlist name, URLs (one per line) and press Submit.

![widget screenshot](https://github.com/jannesantana/setplaylist/blob/main/setplaylist_screenshot.png)

3. Authenticate with Spotify (browser will open)

4. Playlist will be created automatically.

![terminal screenshot](https://github.com/jannesantana/setplaylist/blob/main/terminal_screenshot.png)

# Limitations
Song matching may fail for:
* live versions
* remixes
* typos or uncommon titles (make sure you pasted the correct URL).
* Requires a Spotify account
* Depends on Setlist.fm page structure

# Future Improvements
* Improve song matching (fuzzy search, scoring)
* Handle missing tracks more robustly (instead of just skipping)
* Add CLI or web interface
* Deploy as a web application
