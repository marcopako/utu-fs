import subprocess

channels = [
("NASA Live","https://www.youtube.com/watch?v=21X5lGlDOfg","https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg","Ciencia"),
]

playlist = "#EXTM3U\n"

for name,url,logo,group in channels:
    try:
        stream = subprocess.check_output(
            ["yt-dlp","-g","-f","best",url],
            stderr=subprocess.DEVNULL
        ).decode().split("\n")[0]

        playlist += f'#EXTINF:-1 tvg-logo="{logo}" group-title="{group}",{name}\n'
        playlist += stream + "\n"

    except:
        pass

with open("youtube.m3u","w") as f:
    f.write(playlist)
