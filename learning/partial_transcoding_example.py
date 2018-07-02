import subprocess

file = "/home/atreides/Music/Paramore/Paramore/09 Still Into You.m4a"
start = 1
delta = 30

command = ["ffmpeg", "-i",
           f"{file}",
           "-ss", f"{start}",
           "-vn",
           "-flags", "bitexact",
           "-acodec", "libopus", "-t", f"{delta}", "-f", "webm", "-"]

pipe = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10 ** 8)
read_stuff = pipe.stdout.read()

print(f"read_stuff: {len(read_stuff)}")

pipe.terminate()
