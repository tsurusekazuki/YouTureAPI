from django.db import models


class User(models.Model):

    class Meta:
        db_table = 'user'

    name = models.CharField(max_length=32)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Youtube(models.Model):

    class Meta:
        db_table = 'youtube'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    category_id = models.IntegerField(verbose_name='カテゴリID', null=True, blank=True)
    subscriber = models.IntegerField(verbose_name='チャンネル登録者数', null=True, blank=True)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
