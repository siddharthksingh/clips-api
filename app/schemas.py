from pydantic import BaseModel


class ClipBase(BaseModel):
    id: int
    title: str
    description: str | None
    genre: str | None
    duration: str | None
    audio_url: str

    class Config:
        orm_mode = True


class ClipStats(BaseModel):
    id: int
    title: str
    genre: str | None
    duration: str | None
    play_count: int

    class Config:
        orm_mode = True