from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['text', 'rating'] # тут мы указываем только те поля, которые должен заполнять сам пользователь
        
    def clean_rating(self): 
        rating = self.cleaned_data.get('rating') 
        if rating is not None and (rating < 1 or rating > 5): 
            raise forms.ValidationError("Оценка должна быть от 1 до 5 звезд!") 
        return rating

