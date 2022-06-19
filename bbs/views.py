from django.shortcuts import render, redirect
from django.views import View

from .models import Topic, Category
from .forms import TopicForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        
        context = {}
        context["topics"] = Topic.objects.order_by("-dt")
        context["categories"] = Category.objects.all()

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


class DeleteView(View):

    def post(self, request, pk, *args, **kwargs):

        topic = Topic.objects.filter(id=pk).first()

        if topic:
            print("削除")
            topic.delete()
        else:
            print("データなし")

        return redirect("bbs:index")

delete = DeleteView.as_view()


class EditView(View):

    def get(self, request, pk, *args, **kwargs):

        context                 = {}
        context["topic"]        = Topic.objects.filter(id=pk).first()
        context["categories"]   = Category.objects.all()

        return render(request, "bbs/edit.html", context)

    def post(self, request, pk, *args, **kwargs):

        topic = Topic.objects.filter(id=pk).first()
        form = TopicForm(request.POST, instance=topic)

        if form.is_valid():
            print("バリデーションOK")
            form.save()
        else:
            print("バリデーションNG")
            print(form.errors)

        return redirect("bbs:index")

edit = EditView.as_view()


