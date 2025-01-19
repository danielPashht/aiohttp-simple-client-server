import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8081/add_task', json={'title': 'Buy milk'}) as response:
            print('Adding task...')
            print(await response.json())

        async with session.get('http://localhost:8081/tasks') as response:
            print('Getting tasks...')
            print(await response.json())

        async with session.post('http://localhost:8081/add_task', json={'title': 'Buy eggs'}) as response:
            print('Adding task...')
            print(await response.json())

        async with session.get('http://localhost:8081/tasks') as response:
            print('Getting tasks...')
            print(await response.json())

        async with session.put('http://localhost:8081/task/1') as response:
            print('Toggling task...')
            print(await response.json())

        async with session.get('http://localhost:8081/tasks') as response:
            print('Getting tasks...')
            print(await response.json())

        async with session.put('http://localhost:8081/task/2') as response:
            print('Toggling task...')
            print(await response.json())

        async with session.get('http://localhost:8081/tasks') as response:
            print('Getting tasks...')
            print(await response.json())

        async with session.delete('http://localhost:8081/task/1') as response:
            print('Deleting task...')
            print(await response.json())

        async with session.get('http://localhost:8081/tasks') as response:
            print('Getting tasks...')
            print(await response.json())

        async with session.delete('http://localhost:8081/task/2') as response:
            print('Deleting task...')
            print(await response.json())

        async with session.get('http://localhost:8081/tasks') as response:
            print('Getting tasks...')
            print(await response.json())


if __name__ == '__main__':
    asyncio.run(main())
