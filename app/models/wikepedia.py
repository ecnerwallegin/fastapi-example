from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WikipediaSearchResult(BaseModel):
    pageid: int
    title: str
    snippet: str
    size: int
    wordcount: int
    timestamp: datetime
    
class WikipediaPage(BaseModel):
    pageid: int
    title: str
    text: str

