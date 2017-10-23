from django.contrib import admin

# Register your models here.
from models import UserProfile, RegistrationPath, Education, Gender, MedicationType, DiabeticsType, Question, QuestionareItem

admin.site.register(UserProfile)
admin.site.register(RegistrationPath)
admin.site.register(Education)
admin.site.register(Gender)
admin.site.register(MedicationType)
admin.site.register(DiabeticsType)
admin.site.register(Question)
admin.site.register(QuestionareItem)
