# the given library management project having the below commands ti run the project succesfully
 requirements to install
 install venv with the "libraryenv" name
** **the project  name** **
 django-admin startproject library_management 
 **app name**
 python manage.py startapp studentapp
 
 pip instal djangorestframework
 pip install psycopg2
 pip install django


the below are the urls to run in the postman
# to see the available books in the library
path('books/',BookList.as_view(),name = 'book_list'),
http://127.0.0.1:8000/student/books/

#  to renewl the books or borrowings
path('borrowing/renew/<int:borrowing_id>',renew_booking,name = 'renew_borrowing'),
http://127.0.0.1:8000/student/borrowing/renew/1
{
"borrowing_id":1
}

# to see the student borrowed books
path('<str:student_name>/borrowings/',Studentborrowings.as_view(),name='student-borrowings'),
http://127.0.0.1:8000/student/anil/borrowings/

# to see the all borrowings by the librarian
path('borrowing_info/',view_borrowing_information,name = 'borrowing_info'),
http://127.0.0.1:8000/student/borrowing_info/

# to mark borrwed books by the librarian
path('mark_borrowed/',mark_borrowed,name = 'mark_borrowed'),
http://127.0.0.1:8000/student/mark_borrowed/
{
"student_id":1,
"book_id":2
}
## to mark borrwed books by the librarian
path('mark_returned/',mark_returned,name = 'mark_returned')
http://127.0.0.1:8000/student/mark_returned/
{
"student_id":1,
"book_id":2
}

 
 
