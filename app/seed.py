from models import Clip, Base
from app.database import engine, SessionLocal

Base.metadata.create_all(bind=engine)

clips = [
    {
        "title": "Embrace",
        "description": "Atmospheric, Ambient, Chill music.",
        "genre": "Electronic",
        "duration": "2m 37s",
        "audio_url": "https://raw.githubusercontent.com/siddharthksingh/clips-assets/main/audio/embrace.mp3"
    },
    {
        "title": "Future Design",
        "description": "Abstract, Background, Bass music.",
        "genre": "Future Bass",
        "duration": "1m 14s",
        "audio_url": "https://raw.githubusercontent.com/siddharthksingh/clips-assets/main/audio/future-design.mp3"
    },
    {
        "title": "A call to the soul",
        "description": "Folk, Acoustic, Guitar music.",
        "genre": "Acoustic",
        "duration": "2m 39s",
        "audio_url": "https://raw.githubusercontent.com/siddharthksingh/clips-assets/main/audio/a-call-to-the-soul.mp3"
    },
    {
        "title": "Relaxing",
        "description": "Age, Ambient, Astral music.",
        "genre": "Classical",
        "duration": "1m 12s",
        "audio_url": "https://raw.githubusercontent.com/siddharthksingh/clips-assets/main/audio/relaxing.mp3"
    },
    {
        "title": "Stomping Rock (Four Shots)",
        "description": "Action, Stylish, Trailer music.",
        "genre": "Rock",
        "duration": "1m 59s",
        "audio_url": "https://raw.githubusercontent.com/siddharthksingh/clips-assets/main/audio/stomping-rocks-four-shots.mp3"
    }
]

def seed():
    db = SessionLocal()
    if db.query(Clip).count() == 0:
        for clip in clips:
            db.add(Clip(**clip))
        db.commit()
        print("Seeded database with Pixabay clips.")
        db.close()
    else:
        print("Database already seeded.")

if __name__ == "__main__":
    seed()