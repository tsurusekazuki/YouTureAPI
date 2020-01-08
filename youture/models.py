from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):

    class Meta:
        db_table = 'user'

    name = models.CharField(max_length=32)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class YoutubeFuture(models.Model):

    class Meta:
        db_table = 'youtube_future'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    subscriber = models.IntegerField(verbose_name='チャンネル登録者数', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日', auto_now=True)
    status = models.IntegerField(
        verbose_name='状態',
        blank=True,
        null=True,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class YoutubeFutureFolder(models.Model):

    class Meta:
        db_table = 'youtube_future_folder'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    folder = models.OneToOneField(YoutubeFuture, verbose_name='フォルダID', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class YoutubeFutureResult(models.Model):

    class Meta:
        db_table = 'youtube_future_result'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    estimated_views = models.IntegerField(verbose_name='予測再生数', null=True, blank=True)
    estimated_likes = models.IntegerField(verbose_name='予測高評価数', null=True, blank=True)
    result = models.OneToOneField(YoutubeFuture, verbose_name='結果', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
