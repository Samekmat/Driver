from django.contrib import admin
from .models import Question, Answer, Advice, Training, Category


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Advice)
admin.site.register(Training)
admin.site.register(Category)
