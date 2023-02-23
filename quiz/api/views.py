from rest_framework import generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import QuizSerializer
from quiz.models import Quiz,Question,QuizResult
from rest_framework import filters
from rest_framework_simplejwt.views import TokenObtainPairView


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






class QuizListView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        filter_backends = [filters.SearchFilter]
        search_fields = ['topic', 'difficulty','created_at']
        return Response(serializer.data)