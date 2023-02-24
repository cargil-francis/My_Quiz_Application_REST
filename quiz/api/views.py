from rest_framework import generics
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import QuizSerializer,UserSerializer,RegisterSerializer,UsersSerializer
from quiz.models import Quiz,Question,QuizResult
from django.contrib.auth.models import User
from rest_framework import filters

from rest_framework_simplejwt.views import TokenObtainPairView



#registeration

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            "message": "User created successfully",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }
        return Response(response_data)




class ObtainTokenPairWithCookieView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']
        print(token)
        response.set_cookie('jwt', token, max_age=3600, httponly=True)
        return response





class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        response = JsonResponse({'message': 'Successfully logged out'}, status=200)
        response.delete_cookie('jwt')
        return response


class QuizCreateAPIView(generics.CreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class QuizListAPIView(generics.ListAPIView):
    serializer_class = QuizSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        current_user = self.request.user
        return Quiz.objects.filter(created_by=current_user)


class UserProfileAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        quizzes = Quiz.objects.filter(created_by=user)
        quiz_serializer = QuizSerializer(quizzes, many=True)
        data = {
            'user' : serializer.data,
            'quizzes' : quiz_serializer.data
        }

        return Response(data)













# class UserListView(generics.ListAPIView):
#         queryset = User.objects.all()
#         # queryset = Quiz.objects.all()
#         serializer_class = UserSerializer

#         def list(self, request):
#             queryset = self.get_queryset()
#             serializer = UserSerializer(queryset, many=True)
#             return Response(serializer.data)

# class UserProfileAPIView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user

#     def get_serializer_context(self):
#         user = self.get_object()
#         context = super().get_serializer_context()
#         context['quizzes'] = Quiz.objects.filter(created_by=user)
#         return context
       
        
        

