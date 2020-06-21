from rest_framework import viewsets
from .model import Vendor
from .serializer import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('id')
    serializer_class = VendorSerializer


class FirmViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.filter(entity_type__exact='firm').order_by('id')
    serializer_class = VendorSerializer
