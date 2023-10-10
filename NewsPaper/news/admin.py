from django.contrib import admin
from .models import *

# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # list_display = [field.name for field in Post._meta.get_fields()]
    list_display = ('header', 'category', 'type')  # оставляем только имя и цену товара
    list_filter = ('category', 'rating', 'name', 'type')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('header', 'category__name_category')
    # генерируем список имён всех полей для более красивого отображения

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)

# Register your models here.
