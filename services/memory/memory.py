# services/memory/memory.py

memory_store = []

async def remember(text):
    memory_store.append(text)

async def recall():
    return memory_store[-10:]
