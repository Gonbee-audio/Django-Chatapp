from accounts.models import User

class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    

        request.u = User.objects.all()

        
        response = self.get_response(request)

        return response