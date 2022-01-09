from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator, RegexValidator
from .models import *
from django.forms import ModelForm, TextInput, DateInput, Select, NumberInput
from django import forms

# Тип для заполнения даты
class DateInput(forms.DateInput):
    input_type = 'date'

# Форма поставщика
class ProviderForm(ModelForm):
    class Meta:
        model = Provider
        fields = ['provider_name', 'inn', 'address', 'phone']

        widgets = {
            'provider_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название фирмы поставщика'
            }),
            'inn': TextInput(attrs={
                         'class': 'form-control',
                         'placeholder': 'ИНН'
             }),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+71234567890'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            })
            }

    def __init__(self, *args, **kwargs):
        super(ProviderForm, self).__init__(*args, **kwargs)
        self.fields['inn'].validators = [MinValueValidator(10**9), MaxValueValidator(10 ** 12)]
        validate_phone = RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$',
                                           message='Неправильно введен номер телефона.',
                                           code='invalid_format')
        self.fields['phone'].validators = [validate_phone]

# Форма клиента
class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ['client_name', 'phone', 'address', 'inn']

        widgets = {
            'client_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название клиентской фирмы'
            }),
            'inn': TextInput(attrs={
                         'class': 'form-control',
                         'placeholder': 'ИНН'
             }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+71234567890'
            }),
            'address': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            })
            }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['inn'].validators = [MinValueValidator(10**9), MaxValueValidator(10**12)]
        validate_phone = RegexValidator(regex=r'^((\+7|7|8)+([0-9]){10})$',
                                        message='Неправильно введен номер телефона.',
                                        code='invalid_format')
        self.fields['phone'].validators = [validate_phone]

# Форма ед измерения
class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

        widgets = {
            'unit': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Новая единица измерения'
            }),
        }
# Форма для места хранения
class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

        widgets = {
            'place_for_store': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место хранения'
            }),
        }
# Форма продуктов
class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['product_name', 'amount', 'unit', 'price_for_one', 'place_for_store', 'provider', 'description', 'certificate', 'valid']

        widgets = {
            'product_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование товара'
            }),
            'amount': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
             }),
            'unit': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Единица измерения'
            }),
            'price_for_one': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00.0'
            }),
            'place_for_store': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Место хранения'
            }),
            'provider': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Поставщик товара'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание товара'
            }),
            'certificate': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '№ сертификата'
            }),
            'valid': DateInput(attrs={
                'class': 'form-control',

            }),
            }

# проверка размера ФАЙЛА
def file_size(value): # add this to some file where you can import it from
    limit = 500*1024
    if value.size > limit:
        raise ValidationError('Файл слишком большой. Максимальный размер файла 500Кб.')

# Форма для загрузки бланка заказа
class BlankForm(ModelForm):
    docfile = forms.FileField(label='Работа с файлом:', validators=[file_size, FileExtensionValidator(['docx', 'doc'])])
    # date = forms.CharField(max_length=20, initial=str(datetime.today().strftime('%d.%m.%Y')))

    class Meta:
        model = Blank
        fields = ['client']

        widgets = {
            'client': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Название документа'
            }),
        }

# Форма номера акта
class NumActForm(ModelForm):
    cols = forms.CharField(max_length=2)

    class Meta:
        model = NumAct
        fields = '__all__'
        widgets = {
            'numact': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер акта',
            }),

        }

# Форма номера описи
class NumOpisForm(ModelForm):
    cols_opis = forms.CharField(max_length=3)

    class Meta:
        model = NumOpis
        fields = '__all__'
        widgets = {
            'numopis': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер описи',
            }),
        }

# Форма загрузки акта
class ActOpenForm(ModelForm):
    arr = NumAct.objects.all()
    n = len(arr)
    list_pr = []
    inside = [0, 1]

    for i in range(n):
        list_pr.append(i)
        inside[0] = str(arr[i].numact)
        inside[1] = arr[i]
        f = tuple(inside.copy())
        list_pr[i] = f

    list_pr.insert(0,['1', ' '])
    CHOICES = tuple(list_pr)


    numact = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES)
    docfile = forms.FileField(label='Работа с файлом:', validators=[file_size, FileExtensionValidator(['docx', 'doc'])])
    date = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), initial=str(datetime.today().strftime('%d.%m.%Y')))


    class Meta:
        model = ActDoc
        fields =['client']

        widgets = {
            'client': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Клиент'
            }),
        }


# Форма заполнения акта
class ActForm(forms.Form):
        # act_num = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={"class": "form-control", 'valid': 'None'}))
        act_date = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
        post = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
        name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
        contract_num = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))
        contract_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
        doc_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={"class": "form-control"}))


# Форма заполнения описи
class OpisForm(forms.Form):
        podrazdel = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Структурное подразделение' }))
        okud = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Код ОКУД'}))
        okpo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Код ОКПО'}))
        v_activ = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Вид деятельности'}))
        num = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Номер'}))
        date = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Дата'}))
        d_start = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Дата начала инвен.'}))
        d_end = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Дата конца инвен.'}))
        v_oper = forms.CharField(max_length=70, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Вид операции'}))
        # num_doc = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Номер документа'}))
        # d_make = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Дата составления'}))
        v_product = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Вид товарной ценности'}))


# Форма продукта в акте
class ProductsInActForm(ModelForm):
    class Meta:
        model = ProductsInAct
        fields = ['product', 'amount']

        widgets = {
            'product': Select(attrs={
                'class': 'form-control',
                'placeholder': ' '
            }),
            'amount': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),

        }

# Форма продукта в описи
class ProductsInOpisForm(ModelForm):
    class Meta:
        model = ProductsInOPis
        fields = ['product', 'amount']

        widgets = {
            'product': Select(attrs={
                'class': 'form-control',
                'placeholder': ' '
            }),
            'amount': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '0'
            }),

        }

# Форма добавления клиента в акт
class ClientCompanyAddForm(forms.Form):
    arr = Client.objects.all()
    n=len(arr)
    list_c=[]
    inside = [0, 1]

    for i in range(n):
        list_c.append(i)
        inside[0] = arr[i].client_name
        inside[1] = arr[i]
        f = tuple(inside.copy())
        list_c[i] = f

    list_c.insert(0,['1', ' '])
    CHOICES = tuple(list_c)

    client = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=CHOICES)


