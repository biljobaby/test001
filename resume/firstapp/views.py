from django.db.models.query import QuerySet
from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View
from .filters import ResumeFilter

# Create your views here.
class IndexView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()

  myFilter = ResumeFilter(request.GET, queryset=candidates)
  candidates = myFilter.qs
  return render(request, 'index.html',{'candidates':candidates, 'form':form, 'myFilter':myFilter})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'index.html', {'form':form})

class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'candidate.html', {'candidate':candidate})