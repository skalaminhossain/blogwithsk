from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog 
from .models import Personalblog
from .models import Comment
# Register your models here.

class BlogAdmin(SummernoteModelAdmin):
    list_display = [
        "discription",
        "thumbnail",
        "timecase"
        
    ]
    # summernote_fields = ('discription',)
   

# class PersonalblogAdmin(admin.ModelAdmin):
#     list_display = [
#         "blogtitle",
#         "thumbnail",
#         'description'


#     ]
#     summernote_fields = ('description',)

class PersonalblogAdmin(SummernoteModelAdmin):

    list_display = [
        'blogtitle',
        'thumbnail',
        
    ]

    summernote_fields = ('description',)

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "body"

    ]

admin.site.register(Comment,CommentAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Personalblog , PersonalblogAdmin)