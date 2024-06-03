from django.db import models #  Импортирует модуль models Django для определения базовых классов моделей.
from django.contrib.auth import get_user_model # Импортирует функцию get_user_model, которая возвращает модель пользователя, используемую в проекте.


User = get_user_model() #Получает модель пользователя, используемую в проекте.

class Post(models.Model): # для сохранения в баззе данных 
    class Meta:
        verbose_name = 'Пост' # для человека читаемой строки
        verbose_name_plural = 'Посты' # plural = множество


    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, 
                               related_name='posts', 
                               verbose_name='Автор',
                               blank=True)
    
#"""    author: Поле ForeignKey, связанное с моделью пользователя. 
#on_delete=models.CASCADE указывает, что при удалении пользователя будут удалены и связанные с ним посты.
# related_name='posts' определяет имя обратной связи, которое можно использовать для обращения к постам пользователя.

    
    title = models.CharField(max_length= 60, 
                             verbose_name= 'Название')
# Поле CharField, предназначенное для заголовка поста.
    
    content = models.TextField(blank=True,
                               verbose_name= 'Описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')

#created_at: Поле DateTimeField с параметром auto_now_add=True, которое автоматически устанавливает текущую дату и время при создании объекта.

    image = models.ImageField(upload_to='media/',
                              verbose_name='Фото')



    def __str__(self):
        return self.title
    







    # Виды on_delete
    #PROTECT: Запрещает удаление связанного объекта, если на него ссылаются другие объекты. В случае попытки удаления будет вызвано исключение ProtectedError
    #SET_DEFAULT: При удалении связанного объекта, значение внешнего ключа в связанных объектах будет установлено в значение по умолчанию, указанное в поле default
    #SET_NULL: При удалении связанного объекта, значение внешнего ключа в связанных объектах будет установлено в NULL. Требует, чтобы поле могло быть пустым (null=True).