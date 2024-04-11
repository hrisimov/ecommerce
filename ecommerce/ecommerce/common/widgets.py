from django import forms


class ImageInput(forms.widgets.ClearableFileInput):
    template_name = 'widgets/image_input.html'
