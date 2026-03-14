import subprocess

channels = [
("NASA Live","https://www.youtube.com/@NASA/live","https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg","Ciencia"),
("Canal Once","https://www.youtube.com/@CanalOnceIPN/live","https://upload.wikimedia.org/wikipedia/commons/2/2b/Canal_Once_logo_2025.png","Noticias"),
("NMás","https://www.youtube.com/@nmas/live","https://upload.wikimedia.org/wikipedia/commons/f/f6/Logo-nmas.png","Noticias"),
("Kings League Mexico","https://www.youtube.com/@kingsleague_mex/live","https://upload.wikimedia.org/wikipedia/commons/9/92/Kings-league.png","Entretenimiento"),
("Kings League España","https://www.youtube.com/@KingsLeagueOfficial/live","https://upload.wikimedia.org/wikipedia/commons/9/92/Kings-league.png","Entretenimiento")
]

playlist = "#EXTM3U\n"

for name,url,logo,group in channels:
    try:
        stream = subprocess.check_output(
            ["yt-dlp","-g","-f","best",url],
            stderr=subprocess.DEVNULL
        ).decode().strip()

        playlist += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
        playlist += stream + "\n"

    except:
        print(f"{name} not live")

with open("youtube.m3u","w") as f:
    f.write(playlist)
