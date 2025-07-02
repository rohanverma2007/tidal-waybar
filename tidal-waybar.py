#!/usr/bin/python3

import requests
import os
import sys

TIDAL_STATUS_URL = "http://localhost:47837/current"
TIDAL_CONTROL_URL = "http://localhost:47837/player"

def get_current_song():
    try:
        response = requests.get(TIDAL_STATUS_URL)
        data = response.json()

        if data.get("status") == "playing":
            title = data.get("title", "Unknown Track")
            artist = data.get("artists", "Unknown Artist")

            # Limit artist name to 30 characters
            if len(artist) > 20:
                artist = artist[:27] + "..."

            return f" 󰝚 {artist} - {title}"
        else:
            return "󰝚 Paused "
    except requests.RequestException:
        return ""

if __name__ == "__main__":
    button = os.getenv("WAYBAR_BUTTON")

    if button == "1":  # Left click → Previous song
        send_command("previous")
    elif button == "2":  # Middle click → Play/Pause toggle
        send_command("playpause")
    elif button == "3":  # Right click → Next song
        send_command("next")
    else:
        print(get_current_song())  # Default output for Waybar
