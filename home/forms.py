from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["name", "description", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Title"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Description"}),
        }

    def clean_image(self):
        img = self.cleaned_data["image"]
        if img.size > 3 * 1024 * 1024:  # 3 MB
            raise forms.ValidationError("Image too large (max 3 MB).")
        return img
    
class ReviewForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        queryset=Movie.objects.order_by("name"),
        widget=forms.Select(attrs={"class": "select-movie"})
    )
    review = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Your review"})
    )
    
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ["movie", "review", "rating"]

