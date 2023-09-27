from app.models.data import Data
from app.utils.crypto import encrypt_with_salt
from rich.console import Console
from datetime import datetime

import pytz

tz = pytz.timezone('Asia/Taipei')

console = Console()

async def perform_save_data(save_data):
    data_models = []
    if save_data.tag in ["invoice_paper", "invoice_trad"]:
        invoice_data = save_data.invoice
        user_data = save_data.user
        for invoice in invoice_data:
            invoice["gov"] = {
                "status": "審查中",
                "gov_status": "等待查詢中",
                "error_msg": "",
            }
            data_model = Data(
                tag=save_data.tag,
                created_timestamp=datetime.now(tz),
                updated_timestamp=datetime.now(tz),
                data={**user_data, **invoice}
            )
            data_models.append(data_model)

    elif save_data.tag == "carrier":
        carrier_data = save_data.carrier
        if 'card_encrypt' in carrier_data:
            encrypted_card = encrypt_with_salt(carrier_data['card_encrypt'])
            carrier_data['card_encrypt'] = encrypted_card
        carrier_data["gov"] = {
                "status": "審查中",
                "gov_status": "等待查詢中",
                "error_msg": "",
        }
        data_model = Data(
            tag=save_data.tag,
            created_timestamp=datetime.now(tz),
            updated_timestamp=datetime.now(tz),
            data={**carrier_data},
        )
        data_models.append(data_model)


    result = await Data.insert_many(data_models)
    inserted_ids = result.inserted_ids

    for idx, data_model in enumerate(data_models):
        setattr(data_model, 'id', str(inserted_ids[idx]))

    return data_models
