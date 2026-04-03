from mutagen import File

def load_metadata(path: str):
    audio = File(path)
    return {
        "title": str(audio.tags.get("TIT2", path)),
        "artist": str(audio.tags.get("TPE1", "Unknown")),
        "duration": audio.info.length
    }
