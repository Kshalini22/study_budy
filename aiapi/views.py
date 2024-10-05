from django.views import View
from  django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from aiapi.route.connection import generate_questions, summarize_topic
# Create your views here.

class Questions(APIView):
    def post(self,request):
        ques = request.data.get("question")
        keyword = request.data.get("keyword")
        # que = "1. What is photosynthesis?\nA. The process by which animals breathe\nB. The process by which plants produce food using sunlight, water, and carbon dioxide \nC. The process in which plants absorb water through their roots\nD. The breakdown of glucose to produce energy\n\n2. Which substance do plants need for photosynthesis to occur?\nA. Oxygen\nB. Carbon Monoxide\nC. Nitrogen\nD. Carbon Dioxide\n\n3. What is the primary function of photosynthesis?\nA. To provide energy for plant growth and development\nB. To produce oxygen for animals to breathe\nC. To help plants move in response to light\nD. To transport water in plants\n\n4. What is the by-product of photosynthesis?\nA. Carbon Dioxide\nB. Oxygen\nC. Nitrogen\nD. Methane\n\n5. What role does sunlight play in photosynthesis?\nA. It provides the heat necessary for the reaction \nB. It is converted"   
        if ques:
            if keyword == "1":
                sum = summarize_topic(ques)
                return JsonResponse({ "text": sum })
            elif keyword == "2":
                ans = generate_questions(ques)
                return JsonResponse({ "text": ans })
            else:
                return JsonResponse({"text": "Please select keyword"})
        else:
            return JsonResponse({"text":"Question did not appear!"})
    def get(self, request):
        return HttpResponse("Api is working...")
