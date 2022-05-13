from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):

        message = "Hello!"

        context = { "content": message }

        return render(request, "bbs/index.html", context)

index = IndexView.as_view()
