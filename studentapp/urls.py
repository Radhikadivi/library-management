from django.urls import path
from .views import BookList,renew_booking,Studentborrowings,view_borrowing_information,mark_borrowed,mark_returned

urlpatterns = [
    path('books/',BookList.as_view(),name = 'book_list'),
    path('borrowing/renew/<int:borrowing_id>',renew_booking,name = 'renew_borrowing'),
    path('<str:student_name>/borrowings/',Studentborrowings.as_view(),name='student-borrowings'),
    path('borrowing_info/',view_borrowing_information,name = 'borrowing_info'),
    path('mark_borrowed/',mark_borrowed,name = 'mark_borrowed'),
    path('mark_returned/',mark_returned,name = 'mark_returned')

]