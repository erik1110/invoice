from beanie import Document
from datetime import datetime

class Data(Document):
    tag: str
    data: dict
    created_timestamp: datetime
    updated_timestamp: datetime
