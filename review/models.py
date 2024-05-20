from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

User=get_user_model()

class Like(models.Model):
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    user=models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE, verbose_name='Пользователь')
    post=models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE, verbose_name='Пост')

    def __str__(self):
        return f'{self.post} {self.user}'


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    user=models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE, verbose_name='Пользователь')
    post=models.ForeignKey(Post,related_name='cooments',on_delete=models.CASCADE, verbose_name='Пост')
    body=models.TextField(verbose_name='Комментарий')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Дата изменения комментария')

    def __str__(self):
        return f'{self.user} {self.post} {self.body}'



class Favorite(models.Model):
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    created_at= models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления в избранное') 

    def __str__(self):
        return f'{self.post}'


class Rating(models.Model):
    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post= models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    rating = models.IntegerField(verbose_name='Рейтинг')  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания рейтинга')

    def __str__(self):
        return f'{self.post} {self.rating}'
