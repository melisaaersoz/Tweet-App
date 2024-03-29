from django.contrib import admin
from tweetapp.models import Tweet
# Register your models here.

#Admin özelliklerini özelleştirme
class TweetAdmin(admin.ModelAdmin):
    #gruplara ayırma
    fieldsets=[
        ('Message Group',{"fields":["message"]}),
         ('Nickname Group',{"fields":["nickname"]})
    ]
    #fields=['nickname'] sadece isim görünür



admin.site.register(Tweet, TweetAdmin)
