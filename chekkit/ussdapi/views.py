from django.shortcuts import render
from .models import USSDRecord
from chekkitapp.models import Manufacurer, Product, Batches, Items

# Create your views here.
def check_it(request):
	data = request.data
	processor = USSDProcessor(data=data)
	return processor.process_request()