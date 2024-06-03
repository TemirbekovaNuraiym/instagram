from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post


User = get_user_model


#Этот метод вызывается при создании нового объекта Post. Он автоматически устанавливает текущего пользователя как автора поста перед сохранением в базу данных

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True) # Итак, поле author в этом сериализаторе будет представлять email автора поста и будет доступно только для чтения.
    class Meta:
        model = Post
        fields = '__all__'

#model = Post: Определяет модель, которую сериализатор будет использовать.
#fields = '__all__': Здесь указывается, что все поля модели Post будут включены в сериализацию.


    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user #. Этот контекст содержит дополнительные данные о запросе,
        # которые могут быть полезны при выполнении различных операций сериализации или валидации.
        
 #В вашем примере, self.context['request'].user используется для доступа к пользователю, отправившему запрос, и установки его как автора нового поста перед сохранением.       
        
        post = super().create(validated_data)
        post.save()
        return post
    
#Этот метод вызывается при создании нового объекта Post. Он автоматически устанавливает текущего пользователя как автора поста перед сохранением в базу данных.

'====================================================================================================='

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'image', 'author') 


#используется для операций, когда требуется только ограниченное количество полей для отображения.