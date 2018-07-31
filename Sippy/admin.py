from django.contrib import admin
from .models import did
from .models import customer
from .models import account
from .models import vendor
from .models import histDid
from .models import yoothUser

admin.site.register(did)
admin.site.register(customer)
admin.site.register(account)
admin.site.register(vendor)
admin.site.register(histDid)
admin.site.register(yoothUser)




