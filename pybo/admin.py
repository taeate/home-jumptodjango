from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

# Question 모델에 세부 기능을 추가할 수 있는 QuestionAdmin 클래스 를 생성 하고
# 제목 검색을 위해 search_fields 속성에 'subject(제목)' 을 추가 했다.