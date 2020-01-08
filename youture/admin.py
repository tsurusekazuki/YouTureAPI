from django.contrib import admin

from .models import User, YoutubeFuture, \
    YoutubeFutureFolder, YoutubeFutureResult


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(YoutubeFuture)
class YouTubeFuture(admin.ModelAdmin):
    pass


@admin.register(YoutubeFutureFolder)
class YouTubeFutureFolder(admin.ModelAdmin):
    pass


@admin.register(YoutubeFutureResult)
class YoutubeFutureResult(admin.ModelAdmin):
    pass
