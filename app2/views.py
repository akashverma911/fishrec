import decimal
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
import requests
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from .forms import FishForm
import json
import base64

URL = "http://127.0.0.1:8000/app1/"

class FishListView(View):
    def get(self, request, *args, **kwargs):
        r = requests.get(url=URL)
        context = r.json()
        return render(request, "app2/list.html", {"data": context})


class FishDetailView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        ur = "http://127.0.0.1:8000/app1/"+str(id)+"/"
        r = requests.get(url=ur)
        context = r.json()
        return render(request, "app2/detail.html", {"data": context})


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (decimal(o) for o in [o])
        return super(DecimalEncoder, self).default(o)
class FishCreateView(View):
  def get(self, request, *args, **kwargs):
      context = {'form': FishForm()}
      return render(request, 'app2/fishcreate.html', context)

  def post(self, request, *args, **kwargs):
      form = FishForm(request.POST,request.FILES)
    
      if form.is_valid():
          print(request.FILES)
          files=form.cleaned_data["image"].read()
          im_b64 = base64.b64encode(files).decode("utf8")
          data = { 
              'name': form.cleaned_data['name'],
              'specie': form.cleaned_data['specie'],
              'weight': form.cleaned_data['weight'],
              'length': form.cleaned_data['length'],
              'long': str(form.cleaned_data['long']),
              'lat': str(form.cleaned_data['lat']),
              'image':im_b64
          }
          json_data = json.dumps(data)
          headers = {'Content-type': 'application/json'}
          r = requests.post(url=URL, data=json_data, headers=headers)
          return render(request, 'app2/fishcreate.html', {'form': form})
          
          # return HttpResponseRedirect(reverse_lazy('list'))
      else:
        print(form.errors)
      return render(request, 'app2/fishcreate.html', {'form': form})
