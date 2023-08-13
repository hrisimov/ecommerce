from django import forms


class AddProductToBasketForm(forms.Form):
    quantity = forms.ChoiceField()

    def __init__(self, max_quantity, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].choices = [(q, q) for q in range(1, max_quantity + 1)]
