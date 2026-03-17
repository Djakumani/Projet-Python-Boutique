from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article


INPUT_STYLE = (
    "width:100%; padding:13px 16px; border:none; border-radius:12px; "
    "font-size:14px; font-family:inherit; background:#E0E4E7; "
    "box-shadow: inset 4px 3px 3px 0px #b8c7dd, inset -2px -4px 4px 0px #fff;"
)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "designation",
            "representation",
            "quantite_disponible",
            "prix_unitaire",
            "categorie",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("style", INPUT_STYLE)


class AchatForm(forms.Form):
    quantite = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "min": "1",
                "value": "1",
                "style": "width:90px; padding:12px 14px; border:none; border-radius:12px; "
                "font-size:14px; text-align:center; background:#E0E4E7; "
                "box-shadow: inset 4px 3px 3px 0px #b8c7dd, inset -2px -4px 4px 0px #fff;",
            }
        ),
        label="Quantité",
    )


class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault("style", INPUT_STYLE)
