from sqlmodel import SQLModel, Field, Relationship


class RegionDefault(SQLModel):
    name: str


class Region(RegionDefault, table=True):
    id: int = Field(default=None, primary_key=True)
