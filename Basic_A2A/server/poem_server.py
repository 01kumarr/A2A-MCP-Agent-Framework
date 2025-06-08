from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional
from fastapi.responses import JSONResponse

app = FastAPI()


class MessagePart(BaseModel):
    text: str

class Message(BaseModel):
    role: Optional[str] = None
    parts: List[MessagePart]

class Task(BaseModel):
    id: str
    message: Message


# Endpoint: Agent Card
@app.get("/.well-known/agent.json")
async def agent_card():
    return {
        "name": "WritePoemAgent",
        "description": "Write a beautiful poem in Shakespeare’s style, with no more than 14 lines",
        "url": "http://localhost:8000",
        "version": "1.0",
        "capabilities": {
            "streaming": False,
            "pushNotifications": False
        }
    }

# Endpoint: Task Handling

@app.post("/tasks/send")
async def handle_task(task: Task):
    try:
        user_message = task.message.parts[0].text
    except (IndexError, AttributeError):
        raise HTTPException(status_code=400, detail="Invalid task format")

    poem = {
            "title": "A Sonnet to the Fading Light",
            "style": "Shakespearean",
            "lines": [
                        "When golden sun doth kiss the distant hill,",
                        "And twilight paints the skies in hues of flame,",
                        "The world grows hushed, as though it drinks its fill",
                        "Of silence, cloaked in dusk’s eternal name.",
                        "The stars peep forth like secrets of the night,",
                        "Each one a tale the heavens long to tell,",
                        "And winds, like whispering ghosts, in gentle flight",
                        "Do weave through leaves a soft, enchanted spell.",
                        "O Time, thou thief with ever-silent tread,",
                        "Why must thou steal the sweetness of the day?",
                        "Thy shadow lengthens where bright joy hath fled,",
                        "And youth doth turn, like dreams, to swift decay.",
                        "Yet in this dark, one truth remains still fair:",
                        "Love’s light outshines the stars that burn in air."
                    ]
    }

    reply_text = f"The poem is: {poem['title']}\n" + "\n".join(poem['lines'])

    return {
        "id": task.id,
        "status": {"state": "completed"},
        "messages": [
            task.message.model_dump(),
            {
                "role": "agent",
                "parts": [{"text": reply_text}]
            }
        ]
    }
