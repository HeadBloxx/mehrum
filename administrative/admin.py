import qrcode
import os
from django.conf import settings
from django.utils.safestring import mark_safe
from django.http import FileResponse, HttpResponse
from django.contrib import admin
from .models import Mehrum

class MehrumAdmin(admin.ModelAdmin):
    list_display = ('id', 'ime', 'datum_dzenaze', 'download_qr')  # Display QR download link in admin

    def save_model(self, request, obj, form, change):
        
        super().save_model(request, obj, form, change)

        qr_data = f"https://mehrum.me/{obj.id}/"
        
        qr = qrcode.make(qr_data)

        qr_directory = os.path.join(settings.MEDIA_ROOT, "qrcodes")
        os.makedirs(qr_directory, exist_ok=True)

        qr_path = os.path.join(qr_directory, f"qr_{obj.id}.png")
        qr.save(qr_path)

    def download_qr(self, obj):
        qr_url = f"/admin/download_qr/{obj.id}/"
        print(qr_url)
        return mark_safe(f'<a href="{qr_url}">Preuzmi QR</a>')

    download_qr.short_description = "QR Code"

admin.site.register(Mehrum, MehrumAdmin)