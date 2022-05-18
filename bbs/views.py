from django.shortcuts import render, redirect
from django.views import View
from .models import Topic

class IndexView(View):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        context = { "topics": topics }

        # renderはレンダリングした結果をレスポンスオブジェクトとして返す。
        return render(request, "bbs/index.html", context)
    
    def post(self, request, *args, **kwargs):
        posted = Topic( comment = request.POST["comment"] )
        posted.save()

        # ↓はPOSTメソッドのリクエストを返してしまうので、更新ボタンをオスと繰り返される。
        # topics = Topic.objects.all()
        # context = {"topics":topics}
        # return render(request, "bbs/index.html", context)

        # POSTメソッドで受け取った後はリダイレクトをする。
        return redirect("bbs:index")


index = IndexView.as_view()
