# Этот код определяет кастомное разрешение (permission) для использования в Django REST Framework. 
# Разрешения в DRF определяют, имеет ли пользователь право выполнять определенные операции с данными.


from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): # Таким образом, он является кастомным разрешением, которое можно использовать в вашем API.
    def has_object_permission(self, request, view, obj):    
#Этот метод определяет, имеет ли пользователь право на выполнение операций с объектом. Он принимает три аргумента:

#self: ссылка на текущий экземпляр класса.
#request: объект запроса.
#view: представление (view), которое обрабатывает запрос.
#obj: объект модели, с которым происходит взаимодействие.

        if request.method in permissions.SAFE_METHODS:
            return True
#Этот блок проверяет, является ли метод запроса безопасным (GET, HEAD, OPTIONS). Если да, то разрешение предоставляется без дополнительных проверок.        

        return obj.author == request.user
    
# Этот блок проверяет, является ли пользователь автором объекта. Если да, то разрешение предоставляется; в противном случае - нет.
    
    