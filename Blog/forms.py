from django import forms

from .models import Article


class ArticleForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    descr = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "cols": 120,
            }
        )
    )
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Article
        fields = [
            'title',
            'descr',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("THis is not a valid title")
        return title

    def cleaned_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise forms.ValidationError("This is not a valid priceTag")
        return price


class RawArticleForm(forms.Form):
    # Django HTML attributes
    title = forms.CharField(
        label="I'm a title, change me", initial="I'm a astart value")
    descr = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "class": "new-class-name two",
            "rows": 20,
            "cols": 12
        })
    )
    price = forms.DecimalField(initial=199.99)
