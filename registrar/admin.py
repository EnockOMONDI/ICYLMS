from django.contrib import admin
# from registrar.models import Order, CartItem, LineItem
from registrar.models import FileUpload
from registrar.models import Course
from registrar.models import CourseSubmission
from registrar.models import CourseDiscussionPost
from registrar.models import CourseDiscussionThread
from registrar.models import CourseSetting
from registrar.models import CourseFinalMark
from registrar.models import Announcement
from registrar.models import Syllabus
from registrar.models import Policy
from registrar.models import Lecture
from registrar.models import Assignment
from registrar.models import AssignmentSubmission
from registrar.models import Exam
from registrar.models import ExamSubmission
from registrar.models import Quiz
from registrar.models import QuizSubmission
from registrar.models import EssayQuestion
from registrar.models import EssaySubmission
from registrar.models import MultipleChoiceQuestion
from registrar.models import MultipleChoiceSubmission
from registrar.models import TrueFalseQuestion
from registrar.models import TrueFalseSubmission
from registrar.models import ResponseQuestion
from registrar.models import ResponseSubmission
from registrar.models import PeerReview
from registrar.models import Category
from registrar.models import Quick_Overview
from registrar.models import Module
from registrar.models import Unit




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(FileUpload)
admin.site.register(Course)
admin.site.register(CourseSubmission)
admin.site.register(CourseDiscussionPost)
admin.site.register(CourseDiscussionThread)
admin.site.register(CourseSetting)
admin.site.register(CourseFinalMark)
admin.site.register(Announcement)
admin.site.register(Syllabus)
admin.site.register(Policy)
admin.site.register(Lecture)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Exam)
admin.site.register(ExamSubmission)
admin.site.register(Quiz)
admin.site.register(Quick_Overview)
admin.site.register(Module)
admin.site.register(Unit)
admin.site.register(QuizSubmission)
admin.site.register(PeerReview)
admin.site.register(EssayQuestion)
admin.site.register(EssaySubmission)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(MultipleChoiceSubmission)
admin.site.register(TrueFalseQuestion)
admin.site.register(TrueFalseSubmission)
admin.site.register(ResponseQuestion)
admin.site.register(ResponseSubmission)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(CartItem, OrderItemAdmin)
# admin.site.register(LineItem, LineItemAdmin)




# Register your models here.





