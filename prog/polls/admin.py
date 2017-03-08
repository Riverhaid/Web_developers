from django.contrib import admin
from polls.models import *

# Register your models here.
'''class DonationAdmin(admin.ModelAdmin):
	list_display=('name','category','price','description')


class CategoryAdmin(admin.ModelAdmin):
	list_display=('id','name')
admin.site.register(Good,GoodAdmin)
admin.site.register(Category,CategoryAdmin)
'''
admin.site.register(Donation)
admin.site.register(ReqToken)
admin.site.register(Request)
admin.site.register(Winner)