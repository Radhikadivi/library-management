from rest_framework import serializers
from .models import Book,Student,Borrowing

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = '__all__'
        
        