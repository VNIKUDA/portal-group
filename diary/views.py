from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.views.generic.dates import MonthArchiveView
from .models import Mark
from .forms import MarkForm


class UserMarksMonthArchiveView(MonthArchiveView):
    model = Mark
    date_field = "date"
    month_format = '%m'
    context_object_name = 'marks'
    template_name = "diary/diary.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        if self.request.user != user and not self.request.user.is_staff:
            raise PermissionDenied
        return queryset.filter(student=user)



# @login_required
# def add_mark(request):
#     if not request.user.is_staff:
#         raise PermissionDenied('Ви не маєте доступа')
#     if request.method == 'POST':
#         form = MarkForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('marks_list')
#     else:
#         form = MarkForm()
#     return render(request, 'marks/add_mark.html', {'form': form})






# @login_required
# def edit_mark(request, pk):
#     mark = get_object_or_404(Mark, pk=pk)
#     if not request.user.is_staff:
#         raise PermissionDenied('Ви не маєте доступа')
#     if request.method == 'POST':
#         form = MarkForm(request.POST, instance=mark)
#         if form.is_valid():
#             form.save()
#             return redirect('marks_list')
#     else:
#         form = MarkForm(instance=mark)
#     return render(request, 'marks/edit_mark.html', {'form': form})






# @login_required
# def delete_mark(request, pk):
#     mark = get_object_or_404(Mark, pk=pk)
#     if not request.user.is_staff:
#         raise PermissionDenied('Ви не маєте доступа')

#     if request.method == 'POST':
#         mark.delete()
#         return redirect('marks_list')
#     return render(request, 'marks/delete_mark.html', {'mark': mark})





    


