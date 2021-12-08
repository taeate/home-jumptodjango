from django.shortcuts import render
from .models import Question



def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')

      # 질문 목록 데이터 는  Question.objects.order_by('create_date') 로 얻을수있다
      # order_by는 조회 결과를 정렬 하는 함수 이다.
      # order_by('-create_date')는 작성일 시 역순 으로 정렬 하라는 의미.
      # - 기호가 붙어 있으면 역방향, 없으면 순방향 정렬을 의미 한다.

    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

      # render 함수는 파이썬 데이터 를 템플릿 에 적용 하여 HTML 로 반환 하는 함수.
      # 여기서 render 은  question_list 데이터 를 pybo/question_list.html 파일에 적용 하여 HTML 을 리턴 한다.
      # pybo/question_list.html 과 같은 파일을 템플릿(Template)이라고 부른다.