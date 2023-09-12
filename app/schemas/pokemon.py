from pydantic import BaseModel

class PokemonResponse(BaseModel):
    id: int
    name: str
    types: list[str]
    images: dict[str, str]