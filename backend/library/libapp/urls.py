from django.urls import path
from . import views

urlpatterns = [
    # Book URLs
    path('books/', views.getAllBooks, name='get_all_books'),
    path('books/<str:pk>/', views.getOneBook, name='get_one_book'),
    path('books/create/', views.createBook, name='create_book'),
    path('books/<str:pk>/update/', views.updateBook, name='update_book'),
    path('books/<str:pk>/delete/', views.deleteBook, name='delete_book'),
    
    # Member URLs
    path('members/', views.getAllMembers, name='get_all_members'),
    path('members/<str:pk>/', views.getOneMember, name='get_one_member'),
    path('members/create/', views.createMember, name='create_member'),
    path('members/<str:pk>/update/', views.updateMember, name='update_member'),
    path('members/<str:pk>/delete/', views.deleteMember, name='delete_member'),

    # Transaction URLs
    path('transactions/', views.getAllTransactions, name='get_all_transactions'),
    path('transactions/issue/', views.issue_book, name='issue_book'),
    path('transactions/return/', views.return_book, name='return_book'),
]
