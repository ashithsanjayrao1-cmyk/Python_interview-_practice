import asyncio

async def fetch_data(item_id: int):
    print(f"Starting fetch for {item_id}....")

    await asyncio.sleep(1)

    print(f"Finished fetch for{item_id}!")
    return f"Item {item_id}"

async def main():

    results = await asyncio.gather(

        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print("All Resuls:", results)


if __name__ == "__main__":
    asyncio.run(main())
    