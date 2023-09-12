from fastapi import APIRouter, Query, HTTPException
from sqlalchemy import select
from sqlalchemy.sql import text
from app.database import async_session
from app.models.pokemon import Pokemon
from app.schemas.pokemon import PokemonResponse
import logging


router = APIRouter()

# Endpoint to get a list of Pokémon with filters
@router.get("/pokemons")
async def get_pokemons(
    name: str = Query(None, description="Filter by Pokémon name"),
    type: str = Query(None, description="Filter by Pokémon type"),
    limit: int = Query(100, description="Number of results to return", le=1000),
    offset: int = Query(0, description="Offset for paginated results", ge=0),
) -> list[PokemonResponse]:
    try:
        async with async_session() as session:
            stmt = select(Pokemon)
            
            if name:
                stmt = stmt.where(Pokemon.name.ilike(f"%{name}%"))
            
            if type:
                subquery = text("EXISTS (SELECT 1 FROM jsonb_array_elements_text(types) as t(type) WHERE type = :type)") \
                    .bindparams(type=type)
                stmt = stmt.where(subquery)
            
            stmt = stmt.limit(limit).offset(offset)
            
            result = await session.execute(stmt)
            pokemons = result.scalars().all()
            
            return pokemons
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while fetching Pokemon data")

