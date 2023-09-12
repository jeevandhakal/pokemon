from app.database import async_session, engine
from app.models.pokemon import Pokemon, Base
from sqlalchemy import select, func
import aiohttp


async def fetch_pokemon_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to fetch data from {url}")
                return None

async def populate_database():
    # Create the 'pokemon' table if it doesn't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        stmt = select(func.count()).select_from(Pokemon)
        result = await session.execute(stmt)
        count = result.scalar()
        if count == 0:
            base_url = "https://pokeapi.co/api/v2/pokemon"
            url = base_url + "?limit=500"

            while url:
                pokemon_list_data = await fetch_pokemon_data(url)
                if pokemon_list_data:
                    for pokemon_data in pokemon_list_data["results"]:
                        detail_url = pokemon_data["url"]
                        detail_data = await fetch_pokemon_data(detail_url)
                        if detail_data:
                            # Extract ID, name, types, and images
                            pokemon_id = detail_data["id"]
                            name = detail_data["name"]
                            types = [t["type"]["name"] for t in detail_data["types"]]
                            images = {
                                "front_default": detail_data["sprites"]["front_default"],
                                "back_default": detail_data["sprites"]["back_default"]
                            }

                            # Create a new Pokemon instance and add it to the database
                            new_pokemon = Pokemon(
                                id=pokemon_id,
                                name=name,
                                types=types,
                                images=images
                            )
                            session.add(new_pokemon)
                            await session.commit()

                    url = pokemon_list_data["next"]

