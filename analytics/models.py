from django.db import models
from urls.models import URL

class LinkMetrics(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE)
    clicks = models.PositiveIntegerField(default=0)
    device_data = models.JSONField(default=dict, blank=True)  # Stores device type counts

    def record_click(self, device_type):
        """Increment click count and update device data."""
        self.clicks += 1
        if device_type in self.device_data:
            self.device_data[device_type] += 1
        else:
            self.device_data[device_type] = 1
        self.save()

# Create your models here.
