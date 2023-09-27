from pydantic import BaseModel
from typing import List, Optional

class SaveData(BaseModel):
    tag: str
    user: Optional[dict]
    invoice: Optional[List[dict]]
    carrier: Optional[dict]

    class Collection:
        name = "data"

    class Config:
        examples = {
            "example": {
                "summary": "登錄紙本電子發票",
                "value": {
                    "tag": "invoice_paper",
                    "user": {
                        "name": "小明",
                        "email": "test@example.com",
                        "phone": "0912345678",
                    },
                    "invoice": [
                        {
                            "invDate": "20230705",
                            "invNum": "AB12345678",
                            "random_number": "1234",
                        },
                        {
                            "invDate": "20230706",
                            "invNum": "AB12345679",
                            "random_number": "1234",
                        },
                    ]
                }
            },
            "example2": {
                "summary": "登錄傳統發票",
                "value": {
                    "tag": "invoice_trad",
                    "user": {
                        "name": "小明",
                        "email": "test@example.com",
                        "phone": "0912345678",
                    },
                    "invoice": [
                        {
                            "invDate": "20230705",
                            "invNum": "AB12345678",
                            "mediaId": "64c07d72ee44f30fa6ac7e7a",
                        },
                        {
                            "invDate": "20230706",
                            "invNum": "AB12345679",
                            "mediaId": "64c07d72ee44f30fa6ac7e7a",
                        },
                    ]
                }
            },
            "example3": {
                "summary": "登錄個人載具",
                "value": {
                    "tag": "carrier",
                    "carrier": {
                        "userId": "64b8d5ece95b7b72e4b249f5",
                        "name": "小明",
                        "email": "test@example.com",
                        "card_no": "/ABC-123",
                        "card_encrypt": "123456",
                    },
                }
            },
        }
