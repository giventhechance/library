from books import forms
from people.models import Reader


class ReaderModelForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = [
            'surname',
            'name',
            'patronymic',
            'passport_number',
            'email',
            'address',
            'birth_date',
        ]
