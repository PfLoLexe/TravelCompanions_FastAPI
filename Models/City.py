from sqlmodel import SQLModel, Field


class CityDefault(SQLModel):
    region_id: int = Field(default=None, foreign_key="region.id")
    name: str
    description: str


class City(CityDefault, table=True):
    id: int = Field(default=None, primary_key=True)
