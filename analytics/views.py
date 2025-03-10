from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_agents import parse  # Install this using `pip install pyyaml user-agents`
from django.shortcuts import get_object_or_404
from analytics.models import LinkMetrics

class TrackLinkClickView(APIView):
    def get(self, request, link_id):
        link = get_object_or_404(LinkMetrics, id=link_id)

        # Extract device type
        user_agent = request.headers.get("User-Agent", "")
        parsed_ua = parse(user_agent)
        device_type = "Mobile" if parsed_ua.is_mobile else "Tablet" if parsed_ua.is_tablet else "Desktop"

        # Record the click
        link.record_click(device_type)

        return Response({"message": "Click recorded", "redirect_url": link.url}, status=status.HTTP_200_OK)

# Create your views here.
