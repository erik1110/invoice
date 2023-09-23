from beanie import Document
from datetime import datetime

class Media(Document):
    stream: bytes
    content_type: str
    created_timestamp: datetime
