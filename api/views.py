from django.http import JsonResponse


# Create your views here.
def view_student(request):
    student = {"id":1,"name":"John Doe","Subject":"Math"}
    return JsonResponse(student)
