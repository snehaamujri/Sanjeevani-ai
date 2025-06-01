from django.http import JsonResponse
from datetime import date
import json
import os

def verify_batch(request, batch_id):
    file_path = os.path.join(os.path.dirname(__file__), '../blockchain.json')

    with open(file_path) as f:
        data = json.load(f)
        for batch in data:
            if batch["batchID"] == batch_id:
                is_expired = date.today() > date.fromisoformat(batch["expiry"])
                if batch["valid"] and not is_expired:
                    return JsonResponse({
                        "verified": True,
                        "medicine": batch["medicineName"],
                        "expiry": batch["expiry"]
                    })
    return JsonResponse({"verified": False})
