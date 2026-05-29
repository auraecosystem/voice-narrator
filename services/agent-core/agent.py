# services/agent-core/agent.py

from memory.memory import remember, recall

async def think(user_input):

    history = await recall()

    prompt = f"""
    Previous memory:
    {history}

    User:
    {user_input}
    """

    await remember(user_input)

    return prompt
