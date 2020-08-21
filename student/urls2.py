from django.conf.urls import include, url

from . import views

# Import custom views.
from student.views import announcement
from student.views import syllabus
from student.views import policy
from student.views import lecture
from student.views import lecture_note
from student.views import assignment
from student.views import quiz
from student.views import exam
from student.views import discussion
from student.views import peer_review
from student.views import credit
app_name="student"
urlpatterns = [
    # Announcement
    url(r'^course/(?P<id>\d+)/dashboard/announcements$', announcement.announcements_page, name='announcements_page'),

    # Syllabus
    url(r'^course/(?P<id>\d+)/dashboard/syllabus$', syllabus.syllabus_page, name='syllabus_page'),

    # Grades & Policy
    url(r'^course/(?P<id>\d+)/dashboard/policy$', policy.policy_page,name='policy_page'),

   
   #Curriculumn Module 
    url(r'^course/(?P<id>\d+)/dashboard/modules$', module.modules_page,name='modules_page'),
    url(r'^course/(?P<id>\d+)/dashboard/module$',  module.module,name='module'),
  
    # Curriculumn Module unit
    url(r'^course/(?P<id>\d+)/dashboard/module/(\d+)/units$', module_unit.module_units_page,name='module_units_page'),
    url(r'^course/(?P<id>\d+)/dashboard/module/(\d+)/view_module_unit$', module_unit.view_module_unit,name='view_module_unit'),
                
     # Lecture
    url(r'^course/(?P<id>\d+)/dashboard/lectures$', lecture.lectures_page,name='lectures_page'),
    url(r'^course/(?P<id>\d+)/dashboard/lecture$', lecture.lecture,name='lecture'),
    url(r'^shortcourse/(?P<id>\d+)/lectures$', lecture.shortcourselectures_page,name='shortcourselectures_page'),
    url(r'^shortcourse/(?P<id>\d+)/shortcourselecture$', lecture.shortcourselecture,name='shortcourselecture'),
                
                       
    # Lecture Notes
    url(r'^course/(?P<id>\d+)/dashboard/lecture/(\d+)/notes$', lecture_note.lecture_notes_page,name='lecture_notes_page'),
    url(r'^course/(?P<id>\d+)/dashboard/lecture/(\d+)/view_lecture_note$', lecture_note.view_lecture_note,name='view_lecture_note'),


    # Assignment(s)
    url(r'^course/(?P<id>\d+)/dashboard/assignments$', assignment.assignments_page,name='assignments_page'),
    url(r'^course/(?P<id>\d+)/dashboard/assignments_table$', assignment.assignments_table,name='assignments_table'),
    url(r'^course/(?P<id>\d+)/dashboard/delete_assignment$', assignment.delete_assignment,name='delete_assignment'),
                       
    # Assignment
    url(r'^course/(?P<id>\d+)/dashboard/assignment/(\d+)$', assignment.assignment_page, name='assignment_page'),
    url(r'^course/(?P<id>\d+)/dashboard/assignment/(\d+)/submit_assignment$', assignment.submit_assignment,name='submit_assignment'),
    url(r'^course/(?P<id>\d+)/dashboard/assignment/(\d+)/submit_e_assignment_answer$', assignment.submit_e_assignment_answer,name='submit_e_assignment_answer'),
    url(r'^course/(?P<id>\d+)/dashboard/assignment/(\d+)/submit_mc_assignment_answer$', assignment.submit_mc_assignment_answer,name='submit_mc_assignment_answer'),
    url(r'^course/(?P<id>\d+)/dashboard/assignment/(\d+)/submit_tf_assignment_answer$', assignment.submit_tf_assignment_answer,name='submit_tf_assignment_answer'),
    url(r'^course/(?P<id>\d+)/dashboard/assignment/(\d+)/submit_r_assignment_answer$', assignment.submit_r_assignment_answer,name='submit_r_assignment_answer'),
                       
    # Quiz(zes)
    url(r'^course/(?P<id>\d+)/dashboard/quizzes$', quiz.quizzes_page,name='quizzes_page'),
    url(r'^course/(?P<id>\d+)/dashboard/quizzes_table$', quiz.quizzes_table,name='quizzes_table'),
    url(r'^course/(?P<id>\d+)/dashboard/quiz_delete$', quiz.delete_quiz,name='delete_quiz'),
                       
    # Quiz
    url(r'^course/(?P<id>\d+)/dashboard/quiz/(\d+)$', quiz.quiz_page,name='quiz_page'),
    url(r'^course/(?P<id>\d+)/dashboard/quiz/(\d+)/submit_quiz$', quiz.submit_quiz,name='submit_quiz'),
    url(r'^course/(?P<id>\d+)/dashboard/quiz/(\d+)/submit_tf_quiz_answer$', quiz.submit_tf_assignment_answer,name='submit_tf_assignment_answer'),

    # Exam(s)
    url(r'^course/(?P<id>\d+)/dashboard/exams$', exam.exams_page,name='exams_page'),
    url(r'^course/(?P<id>\d+)/dashboard/exams_table$', exam.exams_table,name='exams_table'),
    url(r'^course/(?P<id>\d+)/dashboard/delete_exam$', exam.delete_exam,name='delete_exam'),
                       
    # Exam
    url(r'^course/(?P<id>\d+)/dashboard/exam/(\d+)$', exam.exam_page,name='exam_page'),
    url(r'^course/(?P<id>\d+)/dashboard/exam/(\d+)/submit_exam$', exam.submit_exam,name='submit_exam'),
    url(r'^course/(?P<id>\d+)/dashboard/exam/(\d+)/submit_mc_exam_answer$', exam.submit_mc_exam_answer,name='submit_mc_exam_answer'),

    # Peer-Review
    url(r'^course/(?P<id>\d+)/dashboard/peer_reviews$', peer_review.peer_reviews_page,name='peer_reviews_page'),
    url(r'^course/(?P<id>\d+)/dashboard/peer_review/(\d+)$', peer_review.assignment_page,name='assignment_page'),
    url(r'^course/(?P<id>\d+)/dashboard/peer_review/(\d+)/peer_review_modal$', peer_review.peer_review_modal,name='peer_review_modal'),
    url(r'^course/(?P<id>\d+)/dashboard/peer_review/(\d+)/save_peer_review$', peer_review.save_peer_review,name='save_peer_review'),
    url(r'^course/(?P<id>\d+)/dashboard/peer_review/(\d+)/delete_peer_review$', peer_review.delete_peer_review,name='delete_peer_review'),
    url(r'^course/(?P<id>\d+)/dashboard/peer_review/(\d+)/update_assignment_marks$', peer_review.update_assignment_marks,name='update_assignment_marks'),
                       
    # Discussion
    url(r'^course/(?P<id>\d+)/dashboard/discussion$', discussion.discussion_page,name='discussion_page'),
    url(r'^course/(?P<id>\d+)/dashboard/threads_table$', discussion.threads_table,name='threads_table'),
    url(r'^course/(?P<id>\d+)/dashboard/new_thread$', discussion.new_thread_modal,name='new_thread_modal'),
    url(r'^course/(?P<id>\d+)/dashboard/insert_thread$', discussion.insert_thread,name='insert_thread'),
    url(r'^course/(?P<id>\d+)/dashboard/delete_thread$', discussion.delete_thread,name='delete_thread'),                   
    url(r'^course/(?P<id>\d+)/dashboard/thread/(\d+)$', discussion.thread_page,name='thread_page'),
    url(r'^course/(?P<id>\d+)/dashboard/thread/(\d+)/posts_table$', discussion.posts_table,name='posts_table'),
    url(r'^course/(?P<id>\d+)/dashboard/thread/(\d+)/new_post$', discussion.new_post_modal,name='new_post_modal'),
    url(r'^course/(?P<id>\d+)/dashboard/thread/(\d+)/insert_post$', discussion.insert_post,name='insert_post'),
                       
    # Credit
    url(r'^course/(?P<id>\d+)/dashboard/credit$', credit.credit_page,name='credit_page'),
    url(r'^course/(?P<id>\d+)/dashboard/submit_credit_application$', credit.submit_credit_application,name='submit_credit_application'),
]
