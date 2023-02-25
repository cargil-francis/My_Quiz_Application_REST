from rest_framework import generics
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import QuizSerializer,RegisterSerializer,UsersSerializer,UserprofileSerializer,QuizResultSerializer, UpdateModelSerializer
from quiz.models import Quiz,Question,QuizResult,Choice
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
    queryset=Quiz.objects.all()
    serializer_class = QuizSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic','created_at','difficulty']





class UserProfileAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserprofileSerializer

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        quizzes = Quiz.objects.filter(created_by=user)
        quiz_serializer = QuizSerializer(quizzes, many=True)
        data = {
            'user' : serializer.data,
            # 'quizzes' : quiz_serializer.data  # to avoid repetition of quizs
        }

        return Response(data)

class QuizTakingAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer

    def post(self,request,quiz_id):
        quiz = Quiz.objects.get(pk = quiz_id)
        user = request.user

        if QuizResult.objects.filter(user=user, quiz=quiz).exists():
            return Response({'message': 'Quiz has already been taken by the user'})

        total_questions = quiz.question.count()
        correct_answers = 0
        for question in quiz.question.all():
            answer = request.data.get(str(question.id))
            if not answer :
                return Response({'message' : f'answer is missing for question { quiestion.id }'})
            check_answers = Choice.objects.filter(question_id=question.id)  #filter out choices with question_id
            choice_num = 0
            for check_answer in check_answers:                              #Get the correct choice_num          
                if check_answer.is_correct == True:
                    choice_num += 1
                    break
                choice_num += 1

            # choice = Choice.objects.get(pk = answer)
            if choice_num == int(answer) :
                correct_answers += 1

        score = int((correct_answers/total_questions)*100)
        
        quiz_result = QuizResult.objects.create(user = user, quiz = quiz, score = score)


        
        return Response({'message' : f'Your score is { score }'})



class QuizResultAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizResultSerializer

    def get(self, request):
        user = request.user
        quiz_results = QuizResult.objects.filter(user = user)
        serializer = QuizResultSerializer(quiz_results, many=True)
        data = {
            'user' : serializer,
            
        }

        return Response(serializer.data)


 
class AdminUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateModelSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


       



class AdminCreateView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]

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

    


    








        

    
  















       
        
        

