from django.db import models
import datetime
import uuid




class Book(models.Model):
    title=models.CharField(max_length=200, blank=False, )
    author=models.CharField(max_length=200, default='Kipkalia Kones')
    year_publication=models.IntegerField()
    isbn = models.AutoField(primary_key=True, editable=False)
    quantity=models.IntegerField(null=True, blank=True,default=1)
    description=models.TextField(null=True, default='This is a great book about stuff and many things.')
    borrow_fee=models.DecimalField(max_digits=4, decimal_places=2, default=30.00)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member(models.Model):
    name=models.CharField(max_length=50, default='Gaidi Fulani')
    email=models.EmailField(unique=True)
    member_number=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    registration_date=models.DateTimeField(auto_now_add=True)
    debt=models.DecimalField(max_digits=7, decimal_places=2 ,default=0.00)

    def can_borrow(self):
        return self.debt <500

    def __str__(self):
        return self.name


ISSUED ='ISSUED'
RETURNED ='RETURNED'
STATUS_CHOICES = [(ISSUED, 'Issued'),(RETURNED, 'Returned')]
                  
class Transaction(models.Model):
    member=models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    book=models.ForeignKey(Book,models.SET_NULL, null=True )
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    issue_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ISSUED)
    fee_charged = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    transaction_id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.name} on {self.issue_date}"


