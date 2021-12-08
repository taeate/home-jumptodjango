from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    # subject : 질문의 제목
    # 제목은 최대 200자 까지 허용 하도록 max_length=200
    # 제목 처럼 글자수 길이가 제한된 텍스트 는 CharField 사용
    content = models.TextField()
    # 내용(content)처럼 글자수 를 제한할 수 없는 텍스트 는 TextField 사용
    create_date = models.DateTimeField()
    # 작성일 시 처럼 날짜와 시간에 관계된 속성은 DateTimeField 를 사용

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField
    create_date = models.DateTimeField()
    # 기존 모델을 속성 으로 연결 하려면 ForeignKey 를 사용.
    # ForeignKey 는 다른 모델과 연결 하기 위해 사용.
    # on_delete = models.CASCADE 의미는 이 답변과 연결된 질문이 삭제 될 경우 답변도 함께 삭제.