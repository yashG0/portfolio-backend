from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FormData
import logging
from .models import Project


logger = logging.getLogger(__name__)

# Create your views here.

def home(req):
    return HttpResponse("<h2> Hello welcome to my home page </h2>")

@csrf_exempt
def getFormData(req):
    if req.method == 'POST':
        try:
            data = json.loads(req.body)
            logger.info("Received data: %s", data)  # Log the received data
            form_data = FormData(
                name=data.get('name'),
                email=data.get('email'),
                message=data.get('message')
            )
            form_data.save()
            return JsonResponse({"message": "Data saved successfully"})
        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except KeyError as e:
            logger.error("Missing key: %s", e)
            return JsonResponse({"error": f"Missing key: {str(e)}"}, status=400)
        except Exception as e:
            logger.error("An error occurred: %s", e)
            return JsonResponse({"error": str(e)}, status=500)
    else:
        logger.error("GET method not allowed")
        return JsonResponse({"error": "GET method not allowed"}, status=405)

def getprojectdata(req):
    projects = Project.objects.all()
    data = []
    for project in projects:
        project_data = {
            'project_name': project.project_name,
            'project_description': project.project_description,
            'project_img_url': req.build_absolute_uri(project.project_img.url) if project.project_img else '',
            'project_source_code': project.project_source_code
        }
        data.append(project_data)
    
    return JsonResponse({"data":data}, safe=False)

