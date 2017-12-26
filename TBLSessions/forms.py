from pagedown.widgets import PagedownWidget
from .models import TBLSession
from django import forms


class TBLSessionForm(forms.ModelForm):
    """
    Form to create a new tbl session.
    """

    class Meta:
        model = TBLSession
        fields = ['title', 'description', 'is_closed']

        # Widgets about some fields
        widgets = {
            'description': PagedownWidget(
                css=("core/css/markdown.css"),
                show_preview=False
            )
        }
