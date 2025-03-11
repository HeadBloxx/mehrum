import os
from django.conf import settings
from django.http import FileResponse, HttpResponse

def download_qr(request, obj_id):
    """Serve the QR code as a downloadable file."""
    qr_path = os.path.join(settings.MEDIA_ROOT, "qrcodes", f"qr_{obj_id}.png")

    if os.path.exists(qr_path):
        return FileResponse(open(qr_path, "rb"), as_attachment=True, filename=f"qr_{obj_id}.png")
    else:
        return HttpResponse("QR code not found.", status=404)
