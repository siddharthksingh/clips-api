from pydantic import BaseModel, HttpUrl


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


class ClipCreate(BaseModel):
    title: str
    description: str
    genre: str
    duration: str
    audio_url: HttpUrl

class ClipResponse(ClipCreate):
    id: int
    play_count: int

    class Config:
        orm_mode = True