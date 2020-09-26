from django import forms

from Marketplace.models import Plant
from django.utils.translation import gettext_lazy as _


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['title', 'description', 'flowering_time', 'harvest_time', 'perennial', 'hardy', 'location_type', 'image', 'plant_type', 'market_type', 'reserved', 'city', 'zip_code']
        labels = {
            'title': _('Name'),
            'description': _('Beschreibung'),
            'flowering_time': _('Blütezeit'),
            'harvest_time': _('Erntezeit'),
            'perennial': _('Mehrjährig'),
            'hardy': _('Winterfest'),
            'location_type': _('Lageempfehlung'),
            'image': _('Bild'),
            'plant_type': _('Pflanzentyp'),
            'market_type': _('Marktplatztyp'),
            'reserved': _('Reserviert'),
            'city': _('Stadt'),
            'zip_code': _('Postleitzahl'),
        }
        widgets = {
            'user': forms.HiddenInput(),
            'created_at': forms.HiddenInput(),
            'slug': forms.HiddenInput(),
        }