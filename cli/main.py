from core.player import SimplePlayer
from infra.metadata import load_metadata

player = SimplePlayer()

while True:
    cmd = input("> ").strip().split()
    if not cmd:
        continue
    match cmd[0].lower():
        case "play":
            path = cmd[1]
            meta = load_metadata(path)
            print(f"Playing: {meta['artist']} - {meta['title']} ({meta['duration']:.2f} seconds)")
            player.load(path)
            player.play()

        case "stop":
            player.stop()
            break
