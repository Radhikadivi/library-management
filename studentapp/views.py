from django.shortcuts import render
from rest_framework import generics
from .models import Book,Student,Borrowing
from .serializers import BookSerializer,BorrowSerializer
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from rest_framework import status
from rest_framework.decorators  import  api_view
from datetime import datetime,timedelta
from time import timezone
# Create your views here.
# see the books availability 
class BookList(generics.ListAPIView):    
        queryset = Book.objects.all()
        serializer_class  = BookSerializer

        def get(self,request,*args,**kwargs):
            books =self.get_queryset()
            response_data = []
            for book in books:
                borrowings = Borrowing.objects.filter(book =book)
                copies_available = book.quantity - borrowings.count()

                if copies_available > 0:
                    response_data.append({
                        'title':book.title,
                        'author':book.author,
                        'copies_available':copies_available
                    })
                else:
                    next_returned_date = borrowings.latest('returned_date').returned_date
                    response_data.append({
                        'title':book.title,
                        'author':book.author,
                        'next_returned_date':next_returned_date
                    })
            return Response(response_data)
# see the student borrowings by student name
class Studentborrowings(generics.ListAPIView):
    serializer_class = BorrowSerializer

    def get_queryset(self):
        student_name = self.kwargs['student_name']
        return Borrowing.objects.filter(student__name = student_name)

    def list(self,request,*args,**kwargs):
        query_set = self.get_queryset()
        serialized_data = self.serializer_class(query_set,many = True).data
        return Response(serialized_data)
    
#renewl the borrowings or books
@api_view(['PUT'])
def renew_booking(request,borrowing_id):
     try:
        borrowing = Borrowing.objects.get(id = borrowing_id)
        if borrowing.returned:
            return Response({"message":"already book has been returned"},status = status.HTTP_400_BAD_REQUEST)
        if borrowing.renewed:
            return Response({"message":"book has already been renewd once "},status = status.HTTP_400_BAD_REQUEST)
        #check borrowing within 30 days or not
        borrowing_date = borrowing.borrowed_date
        renewel_period = timedelta(days=30)
        if datetime.now().date()>(borrowing_date+renewel_period).date():
            return Response({"message":"Borrowing is not eligible for renewel"},status=status.HTTP_400_BAD_REQUEST)

        #update borrow instance
        borrowing.renewed = True
        borrowing.save() 

        return Response({"message":"boorowing renewl suucessfull"},status=status.HTTP_200_OK)
     except Borrowing.DoesNotExist:
        return Response({"message":"borrowing not found"},status=status.HTTP_400_BAD_REQUEST) 
# views the borrowings by the librarian
@api_view(["GET"])
def view_borrowing_information(request):
    borrowings = Borrowing.objects.all()
    serializer = BorrowSerializer(borrowings, many = True)
    return Response(serializer.data)

# make it as mark borrowed by the librarian
@api_view(['POST'])
def mark_borrowed(request):
    student_id = request.data.get('student_id')
    book_id = request.data.get('book_id')

    try:
        student = Student.objects.get(id= student_id)
        book = Book.objects.get(id = book_id)

        if book.borrowed:
            return Response({"message":"book is already borrowed"})

        borrowing = Borrowing.objects.create(student=student,book = book)

        book.borrowed = True
        book.save()
        return Response({"message":"Book marked succesfully"},status = status.HTTP_200_OK)

    except Student.DoesNotExist:
        return Response({"message":"Student not found"},status=status.HTTP_404_NOT_FOUND)
    
# make it as mark returned by the librarian
        
@api_view(['PUT'])
def mark_returned(request):
    borrowing_id = request.data.get('borrowing_id')

    try:
        borrowing = Borrowing.objects.get(id= borrowing_id)
        if borrowing.returned:
            return Response({"message":"Book is already returned"},status=status.HTTP_400_BAD_REQUEST)
        #update borrowing instance
        borrowing.returned = True
        borrowing.returned_date = datetime.now()
        borrowing.save()

        #updating the book status

        book = borrowing.book
        book.borrowed = False
        book.save()
        return Response({"message":"book marked as returned"},status = status.HTTP_200_OK)
    except Borrowing.DoesNotExist:
        return Response({"message":"boorwing  not found"},status= status.HTTP_404_NOT_FOUND)


    