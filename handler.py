import asyncio

def async_handler(coro):  
    def wrapper(e):
        asyncio.create_task(coro(e)) 
    return wrapper   