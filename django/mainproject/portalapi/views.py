from django.http import JsonResponse

# Create your views here.
def get_version(request):
  versiondata = {
    'version': '0.1'
  }
  return JsonResponse(versiondata)