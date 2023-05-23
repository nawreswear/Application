from django.contrib import admin

from .models import Service
admin.site.register(Service)

from .models import Detail
admin.site.register(Detail)

from .models import Project
admin.site.register(Project)

from .models import Team
admin.site.register(Team)



from .models import Personnel
admin.site.register(Personnel)

from .models import Client
admin.site.register(Client)

from .models import Testimonial
admin.site.register(Testimonial)


from .models import Contact
admin.site.register(Contact)
# Register your models here.
