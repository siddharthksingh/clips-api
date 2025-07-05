from fastapi import FastAPI, HTTPException, Request
from fastapi.params import Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Clip
from app.schemas import ClipBase, ClipStats, ClipCreate, ClipResponse
from starlette_exporter import PrometheusMiddleware, handle_metrics
from prometheus_client import Counter
import os
import requests
import uvicorn


app = FastAPI()
Base.metadata.create_all(bind=engine)


app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/clips", response_model=list[ClipBase])
def list_clips(db: Session = Depends(get_db)):
    clips = db.query(Clip).all()
    return clips

clip_stream_counter = Counter(
    "clip_streams_total",
    "Total number of stream requests by clip ID",
    ["clip_id"]
)

@app.get("/clips/{clip_id}/stream")
def stream_clip(clip_id: int, db: Session = Depends(get_db), request: Request = None):
    clip = db.query(Clip).filter(Clip.id == clip_id).first()
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")

    # Increment play count
    if request.headers.get("range") is None and request.method == "GET":
        clip.play_count += 1
        db.commit()
        clip_stream_counter.labels(clip_id=str(clip_id)).inc()

    # Stream audio directly from the URL
    try:
        r = requests.get(clip.audio_url, stream=True)
        r.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="Failed to fetch audio from source")

    return StreamingResponse(
        r.iter_content(chunk_size=1024),
        media_type="audio/mpeg",
        headers={"Content-Disposition": f"inline; filename={clip.title}.mp3"}
    )


@app.get("/clips/{clip_id}/stats", response_model=ClipStats)
def get_stats(clip_id: int, db: Session = Depends(get_db)):
    clip = db.query(Clip).filter(Clip.id == clip_id).first()
    if not clip:
        raise HTTPException(status_code=404, detail="Clip not found")
    return {
        "id": clip.id,
        "title": clip.title,
        "play_count": clip.play_count,
        "genre": clip.genre,
        "duration": clip.duration
    }


@app.post("/clips", response_model=ClipResponse)
def create_clip(clip_data: ClipCreate, db: Session = Depends(get_db)):
    new_clip = Clip(**clip_data.model_dump())
    db.add(new_clip)
    db.commit()
    db.refresh(new_clip)
    return new_clip


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)