#Теперь надо создать файл filters.py в директории simpleapp/ в той же папке, где лежат наши модели и всё остальное. Нас
#никто не заставляет писать фильтры именно в файле filters.py, но, как мы и отмечали ранее, порядок в коде лучше
#соблюдать с самого начала, иначе при увеличении кодовой базы начнём путаться, что и где лежит.

from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    material = ModelChoiceFilter(
        field_name='productmaterial__material',
        queryset=Material.objects.all(),
        label='Material',
    )


    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Product
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           #'productmaterial__material': ['exact'],   #Вместо 2 пробелов прописал один ! Внимательнее
           # поиск по названию
           'name': ['icontains'],
           # количество товаров должно быть больше или равно
           'quantity': ['gt'],
           'price': [
               'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
       }