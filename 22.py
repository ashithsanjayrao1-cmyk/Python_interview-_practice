import redis
import json
import time

cache = redis.Redis(host = 'localhost', port = 6379, db = 0 , decode_responses = True)

def fetch_from_database(user_id: int) -> dict:
    """Simulates a slow, expensive database query."""
    print("Database queried! (This is slow...)")
    time.sleep(2)
    return {"id": user_id,"name":"Alice","role":"Admin"}


def get_user_profile(user_id: int) -> dict:
    cache_key = f"user_profile:{user_id}"

    cached_data = cache.get(cache_key)

    if cached_data:
        print("Cache Hit! Loading instantly from Redis.")
        return json.loads(cached_data)

    print("Cache Miss! Fetching from DB...")
    user_data = fetch_from_database(user_id)

    cache.setex(cache_key, 60, json.dumps(user_data))

    return user_data

print(get_user_profile(101))
print(get_user_profile(101))
