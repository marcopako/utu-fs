playlist = """#EXTM3U

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" group-title="Ciencia",NASA Live
https://www.youtube.com/@NASA/live

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/2/2b/Canal_Once_logo_2025.png" group-title="Noticias",Canal Once
https://www.youtube.com/@CanalOnceIPN/live

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/f/f6/Logo-nmas.png" group-title="Noticias",NMás
https://www.youtube.com/@nmas/live

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/9/92/Kings-league.png" group-title="Entretenimiento",Kings League Mexico
https://www.youtube.com/@kingsleague_mex/live

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/9/92/Kings-league.png" group-title="Entretenimiento",Kings League España
https://www.youtube.com/@KingsLeagueOfficial/live
"""

with open("youtube.m3u","w") as f:
    f.write(playlist)
