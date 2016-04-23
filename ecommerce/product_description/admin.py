from django.contrib import admin
from product_description.models import *

# Register your models here.

admin.site.register(PdpSpecificationType)
admin.site.register(PdpSpecification)
admin.site.register(PdpDescription)
admin.site.register(PdpKeyFeature)
admin.site.register(PdpPhysicalFeature)
admin.site.register(PdpFeatured)
