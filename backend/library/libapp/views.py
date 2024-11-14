from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Book, Member, Transaction
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status
import datetime

from django.db.models import Q
# Create your views here.


#Book Views

#All Books Views
@api_view(['GET'])
def getAllBooks(request):
    search_book = request.query_params.get('q','')
    books=Book.objects.filter(
        Q(title__icontains=search_book) |
        Q(author__icontains=search_book)
    ).order_by('title')

    page= request.query_params.get('page')
    paginator =Paginator(books, 7)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = BookSerializer(books, many=True)
    return Response({
        'books': serializer.data, 
        'page': page, 
        'total_pages': paginator.num_pages
        })

@api_view(['GET'])
def getOneBook(request, pk):
    book = Book.objects.get(isbn=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createBook(request):
    book = Book.objects.create(

        title='Test Book', 
        author='Test Author',
        year_publication='0000',
        isbn = '111111111',
        quantity='300',
        description='Testing 12 12',
        borrow_fee='40.00',

    )
    serializer=BookSerializer(book, many=False)
    return Response(serializer.data)

def updateBook(request, pk):
    try:
        book = Book.objects.get(isbn=pk)  # Assuming ISBN is unique
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update fields based on request data
    data = request.data
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year_publication = data.get('year_publication', book.year_publication)
    book.isbn = data.get('isbn', book.isbn)
    book.quantity = data.get('quantity', book.quantity)
    book.description = data.get('description', book.description)
    book.borrow_fee = data.get('borrow_fee', book.borrow_fee)
    
    book.save()  # Save the updated book instance

    # Serialize the updated book
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['DELETE'])
def deleteBook(request, pk):
    try:
        book = Book.objects.get(isbn=pk)  # Assuming ISBN is unique
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    book.delete()  # Delete the book

    return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



#get All members view
@api_view(['GET'])
def getAllMembers(request):
    search_member = request.query_params.get('q','')
    members=Member.objects.filter(
        Q(name__icontains=search_member) |
        Q(email__icontains=search_member)
    ).order_by('name')

    page= request.query_params.get('page')
    paginator =Paginator(members, 7)

    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = MemberSerializer(members, many=True)
    return Response({
        'members': serializer.data, 
        'page': page, 
        'total_pages': paginator.num_pages
        })
@api_view(['GET'])
def getOneMember(request, pk):
    member = Member.objects.get(member_number=pk)
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data)

#create Member

@api_view(['POST'])
def createMember(request):
    data = request.data
    member = Member.objects.create(
        name=data.get('Name', 'Default Name'),
        email=data.get('email', 'another@another.com'),
        member_number=data.get('member_number', ),
        
        registration_date=data.get('registration_date', ),
        debt=data.get('debt', '0.00'),
       
    )
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def updateMember(request, pk):
    try:
        member = Member.objects.get(member_number=pk)  # Assuming member_number is unique
    except Member.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

    # Update fields based on request data
    data = request.data
    member.name = data.get('name', member.name)
    member.email = data.get('email', member.email)
    member.member_number = data.get('member_number', member.member_number)
    member.registration_date = data.get('registration_date', member.registration_date)
    member.debt = data.get('debt', member.debt)
    
    member.save()  # Save the updated member instance

    # Serialize the updated member
    serializer = MemberSerializer(member, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def deleteMember(request, pk):
    try:
        member = Member.objects.get(member_number=pk)  # Assuming member_number is unique
    except Member.DoesNotExist:
        return Response({"error": "Member not found"}, status=status.HTTP_404_NOT_FOUND)

    member.delete()  # Delete the member

    return Response({"message": "Member deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getAllTransactions(request):
    transactions = Transaction.objects.all().order_by('issue_date')
    page = request.query_params.get('page', 1)
    paginator = Paginator(transactions, 10)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    serializer = TransactionSerializer(page_obj, many=True)
    return Response({
        'results': serializer.data,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number
    })
@api_view(['POST'])
def issue_book(request):
    member_number = request.data.get('member_number')
    isbn = request.data.get('isbn')

    # Fetch member and book objects
    member = get_object_or_404(Member, pk=member_number)
    book = get_object_or_404(Book, pk=isbn)

    # Check if member has outstanding debt over KES 500
    if not member.can_borrow():
        return Response({'error': 'Member has outstanding debt above KES 500'}, status=status.HTTP_400_BAD_REQUEST)

    # Check if book is in stock
    if book.quantity < 1:
        return Response({'error': 'Book is out of stock'}, status=status.HTTP_400_BAD_REQUEST)

    # Create the transaction
    transaction = Transaction.objects.create(
        member=member,
        book=book,
        issue_status='ISSUED'
    )
    
    # Update book quantity
    book.quantity -= 1
    book.save()

    serializer = TransactionSerializer(transaction)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['POST'])
def return_book(request):
    transaction_id = request.data.get('transaction_id')
    transaction = get_object_or_404(Transaction, pk=transaction_id)

    # Ensure the book hasn't already been returned
    if transaction.issue_status == 'RETURNED':
        return Response({'error': 'This book has already been returned'}, status=status.HTTP_400_BAD_REQUEST)

    # Calculate the rental fee based on days borrowed
    days_borrowed = (datetime.date.today() - transaction.issue_date).days
    rental_fee = days_borrowed * transaction.book.borrow_fee

    # Update transaction details
    transaction.return_date = datetime.date.today()
    transaction.issue_status = 'RETURNED'
    transaction.fee_charged = rental_fee
    transaction.save()

    # Update member's outstanding debt
    transaction.member.debt += rental_fee
    transaction.member.save()

    # Update book quantity
    transaction.book.quantity += 1
    transaction.book.save()

    serializer = TransactionSerializer(transaction)
    return Response(serializer.data, status=status.HTTP_200_OK)