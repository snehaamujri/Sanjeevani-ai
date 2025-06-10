from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from sms_utils import send_sms

@csrf_exempt
def send_report(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get("name")
            phone = data.get("phone")
            batch_id = data.get("batchID")

            # Dummy verification logic
            message = f"Hello {name}, your medicine (Batch {batch_id}) is verified ✅. Stay healthy!"
            response = send_sms(phone, message)
            return JsonResponse({"status": "success", "message": "SMS sent", "response": response})
        except Exception as e:
            return JsonResponse({"status": "failed", "message": str(e)})

    return JsonResponse({"status": "failed", "message": "Only POST allowed"})

def verify_batch(request, batch_id):
    # Example logic for verifying a batch
    return JsonResponse({"status": "success", "batch_id": batch_id, "message": "Batch verified successfully"})
