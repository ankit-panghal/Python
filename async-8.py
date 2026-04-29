import asyncio, httpx

'''async def llm_anfrage(frage):
    await asyncio.sleep(2)      #Simuliert API-Wartezeit
    return f"Antwort : {frage}"

async def hauptsache():
 antworten = await asyncio.gather(     #Alle 3 gleichzeitig starten
    llm_anfrage('Was ist Module?'),
    llm_anfrage('Was bedeutet System Architecture?'),
    llm_anfrage('Wie funktioniert LLMs?')
 )
 #antwort = await llm_anfrage('Was ist SSL Zertifikat?')
 #return antwort
 return antworten

print(asyncio.run(hauptsache()))  # Startet den Async Code'''

async def claude_fragen(frage):
    # with -> Context Manager (Datei/Netwerkbverbindung automatisch offnen/schliessen)
    #AsyncClient -> API Aufrufe senden
    #client -> Objekt als client gennant
    async with httpx.AsyncClient() as client:
    
        response = await client.post(
            "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": "dein-key"},
        json={
        "model": "claude-sonnet-4",
        "max_tokens": 100,
        "messages": [{"role": "user", "content": frage}]
        }
        )
    data = response.json()
    return data["content"][0]["text"]

async def main():
    ergebnisse = await asyncio.gather(
        claude_fragen("Was ist RAG?"),
        claude_fragen("Was ist ein Agent?"),
        claude_fragen("Was ist LangGraph?"),
    )
    return ergebnisse
print(asyncio.run(main()))