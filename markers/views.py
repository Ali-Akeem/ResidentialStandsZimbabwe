from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView


class MarkersMapView(TemplateView):
	template_name = "map.html"
