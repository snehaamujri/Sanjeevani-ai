from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import csv
from django.http import HttpResponse
from sms_utils import send_sms

INCIDENTS = []  # In-memory list for demo

@csrf_exempt
def healthworker_dashboard(request):
    # Dummy data for demo
    inventory = [
        {"medicine": "Paracetamol", "batch": "CIPLA-XYZ123", "expiry": "2025-12-31", "stock": 120},
        {"medicine": "Ibuprofen", "batch": "SUN-ABC456", "expiry": "2024-11-30", "stock": 50},
        {"medicine": "Amoxicillin", "batch": "PFIZER-DEF789", "expiry": "2026-03-15", "stock": 80},
        {"medicine": "Cetrizine", "batch": "DRREDDY-GHI012", "expiry": "2025-09-20", "stock": 200},
        {"medicine": "Azithromycin", "batch": "SUN-JKL345", "expiry": "2025-07-10", "stock": 60},
        {"medicine": "Metformin", "batch": "CIPLA-MNO678", "expiry": "2026-01-05", "stock": 90},
        {"medicine": "Amlodipine", "batch": "TORRENT-PQR901", "expiry": "2025-11-18", "stock": 110},
        {"medicine": "Atorvastatin", "batch": "GLENMARK-STU234", "expiry": "2026-05-22", "stock": 70},
    ]
    tasks = [
        {"task": "Verify batch CIPLA-XYZ123", "status": "pending"},
        {"task": "Deliver Ibuprofen to PHC-2", "status": "pending"},
    ]
    alerts = [
        {"type": "expiry", "msg": "Ibuprofen batch SUN-ABC456 expiring soon!"},
    ]

    if request.method == "POST":
        if "incident" in request.POST:
            incident = request.POST.get("incident")
            if incident:
                INCIDENTS.append(incident)
        elif "toggle_task" in request.POST:
            idx = int(request.POST.get("task_idx"))
            if tasks[idx]["status"] == "pending":
                tasks[idx]["status"] = "done"
            else:
                tasks[idx]["status"] = "pending"
        elif "buy_medicine" in request.POST:
            name = request.POST.get("buyer_name")
            phone = request.POST.get("buyer_phone")
            batch = request.POST.get("buyer_batch")
            medicine = next((item["medicine"] for item in inventory if item["batch"] == batch), "")
            msg = f"Hello {name}, your medicine ({medicine}, Batch {batch}) is verified ✅. Stay healthy! - Sanjeevani.AI"
            send_sms(phone, msg)

    inventory_count = len(inventory)
    tasks_pending = sum(1 for t in tasks if t["status"] == "pending")
    alerts_count = len(alerts)
    medicine_names = [item["medicine"] for item in inventory]
    medicine_stock = [item["stock"] for item in inventory]

    return render(request, "dashboard/dashboard.html", {
        "inventory": inventory,
        "tasks": tasks,
        "alerts": alerts,
        "incidents": INCIDENTS,
        "inventory_count": inventory_count,
        "tasks_pending": tasks_pending,
        "alerts_count": alerts_count,
        "medicine_names": json.dumps(medicine_names),
        "medicine_stock": json.dumps(medicine_stock),
    })

def download_inventory(request):
    # Dummy data for demo (use your real inventory in production)
    inventory = [
        {"medicine": "Paracetamol", "batch": "CIPLA-XYZ123", "expiry": "2025-12-31", "stock": 120},
        {"medicine": "Ibuprofen", "batch": "SUN-ABC456", "expiry": "2024-11-30", "stock": 50},
        {"medicine": "Amoxicillin", "batch": "PFIZER-DEF789", "expiry": "2026-03-15", "stock": 80},
        {"medicine": "Cetrizine", "batch": "DRREDDY-GHI012", "expiry": "2025-09-20", "stock": 200},
        {"medicine": "Azithromycin", "batch": "SUN-JKL345", "expiry": "2025-07-10", "stock": 60},
        {"medicine": "Metformin", "batch": "CIPLA-MNO678", "expiry": "2026-01-05", "stock": 90},
        {"medicine": "Amlodipine", "batch": "TORRENT-PQR901", "expiry": "2025-11-18", "stock": 110},
        {"medicine": "Atorvastatin", "batch": "GLENMARK-STU234", "expiry": "2026-05-22", "stock": 70},
    ]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory.csv"'
    writer = csv.writer(response)
    writer.writerow(['Medicine', 'Batch', 'Stock', 'Expiry'])
    for item in inventory:
        writer.writerow([item['medicine'], item['batch'], item['stock'], item['expiry']])
    return response
