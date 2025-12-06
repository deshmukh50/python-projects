import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)  # Reset colors after each use

def print_lyrics():
    lyrics = [
        "Hum tere bin ab reh nahi sakte",
        "Tere bina kya wajood mera",
        "Hum tere bin ab reh nahi sakte",
        "Tere bina kya wajood mera",
        "Tujhse juda gar ho jaayenge",
        "Toh khud se hi ho jaayenge juda",
        "Kyoonki tum hi ho, ab tum hi ho",
        "Zindagi ab tum hi ho",
        "Chain bhi, mera dard bhi",
        "Meri aashiqui ab tum hi ho"
    ]
    
    delays = [2.0, 1.8, 2.0, 1.8, 2.2, 2.0, 1.5, 1.5, 1.5, 2.5]  # Approximate song timings
    
    print("🎶 Now playing - Tum Hi Ho 💖")
    time.sleep(1.5)
    
    for i, line in enumerate(lyrics):
        if i >= 6: 
            color = Fore.BLUE
        else:
            color = Fore.WHITE
        
        for char in line:
            sys.stdout.write(color + char)
            sys.stdout.flush()
            time.sleep(0.08) 
        print(Style.RESET_ALL)
        time.sleep(delays[i])

print_lyrics()
