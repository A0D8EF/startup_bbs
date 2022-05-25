from django.shortcuts import render, redirect
from django.views import View

from .models import Topic
from .forms import TopicForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        """
        topics = Topic.objects.all()
        # topics = [{"id": id, "comment": comment},{"id": id, "comment": comment},...]
        # topicsは、辞書型のリスト
        context = {"topics": topics}
        """
        context = {}
        context["topics"] = Topic.objects.all()

        # renderはレンダリングした結果をレスポンスオブジェクトとして返す。
        return render(request, "bbs/index.html", context)
    
    def post(self, request, *args, **kwargs):
        """
        posted = Topic( comment = request.POST["comment"] )
        posted.save()
        """
        
        form = TopicForm(request.POST)
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("bbs:index")
        
        print("バリデーションOK")
        form.save()

        return redirect("bbs:index")


index = IndexView.as_view()
