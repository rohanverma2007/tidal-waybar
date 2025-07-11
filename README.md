# tidal-waybar
Adds Tidal support to Hyprland Waybar

# How does it look?
__This is how it looks with my waybar config file:__
![image](https://github.com/user-attachments/assets/2170bc8d-b2dd-4a18-aa49-a64b5a39a193)

# How do I set this up?
1. Ensure you have all the dependencies downloaded!
```
sudo pacman -S python python-requests
```

2. Firstly, I recommend installing the ```tidal-hifi-bin``` from the AUR, you can find alternatives for your distro but I'm currently supporting Arch Linux only. Other clients are **unsupported!**
```
yay -S tidal-hifi-bin
```

3. Click file at the top left, click settings, then go to the API option and ensure the API port is set to 47837 (app must be restarted after applying!)

4. Create a ```scripts``` folder inside of your waybar config and move the .py file to the scripts folder (download it from releases), your config directory should look like this:
```
waybar/
├── config.json
├── style.css
├── scripts/
└───── tidal-waybar.py
```

5. Once tidal-waybar.py script is setup in the scripts folder, you must chmod the file (this command works assuming you are in the scripts directory)
```
chmod +x tidal-waybar.py
```

6. Add to your config.json (atleast this is what I have)
```
    "custom/tidal": {
    	"exec": "~/.config/waybar/scripts/tidal-waybar.py",
    	"interval": 5,
    	"return-type": "string",
    	"on-click": "~/.config/waybar/scripts/tidal-waybar.py",
    	"on-click-middle": "~/.config/waybar/scripts/tidal-waybar.py",
    	"on-click-right": "~/.config/waybar/scripts/tidal-waybar.py"
    },
```

# What features are there to be expected?
- Keybind Support (clicking has control access)
- Displays band name and song
- Minimal and lightweight integration

