from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):

    class Meta:
        model  = Topic
        fields = ["comment"]
        # fields はタプル型（書き換え不可能なリスト型）でもOK
        # fields = ( "comment" )
