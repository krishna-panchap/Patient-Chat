from src.redis.config import Redis
import asyncio
from src.model.gptj import GPT
from src.redis.cache import Cache


async def main():
    redis = Redis()
    # redis = await redis.create_connection()
    # print(redis)
    # await redis.set("key", "value")
    json_client = redis.create_rejson_connection()
    data = await Cache(json_client).get_chat_history(token="c2d0da81-041c-4014-98cf-95779845b7d5")
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
