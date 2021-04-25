from django.shortcuts import render, redirect
from .models import Book, request_detail
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
from .forms import RequestPeriodForm
from background_task import background
import datetime
import time, threading
@login_required
def RequestDeclineView(request, **kwargs):
    current_request = request_detail.objects.filter(id=kwargs['pk'])[0]
    current_user = request.user

    if request.method =='POST':
        current_request.request_status = 'Declined'
        current_request.save()
        return redirect('/admin/')

    if current_user.has_perm('books.change_book'):
        return render(request, 'books/temp.html')
    else:
        raise PermissionDenied


def RequestApproveView(request, **kwargs):
    current_request = request_detail.objects.filter(id=kwargs['pk'])[0]
    current_user = request.user
    if request.method =='POST':
            current_request.book_detail.available = False
            current_request.request_status ='Approved'
            current_request.save()
            current_request.book_detail.save()
            # notify_user(current_request.id, repeat=60, repeat_until=None)
            time.sleep(5)
            # timer(kwargs['pk'])
            thread = threading.Timer(10, verify, args=request_id)
            thread.start
            return redirect('/admin/')

    else:
        if current_user.has_perm('books.change_book'):
            return render(request, 'books/request_approve.html')
        else:
            raise PermissionDenied

# async def timer(request_id):
# 	# while True:
#
#             # break

def verify(request_id, thread):
    current_date = datetime.datetime.now()
    current_date_string = current_date.strftime("%Y-%m-%d")
    current_request = request_detail.objects.filter(id=request_id)[0]
    return_date_string = current_request.return_date.strftime("%Y-%m-%d")
    if current_date_string == return_date_string:
        current_time_hour = current_date.strftime("%H")
        current_time_minute = current_date.strftime("%M")
        if (int(current_time_hour) == 13 and int(current_time_minute) == 56):
            current_request.request_status = 'Overdue'
            current_request.save()
            thread.end
# @background(schedule=1)
# def notify_user(request_id):
#     current_date = datetime.datetime.now()
#     current_date_string = current_date.strftime("%Y-%m-%d")
#     current_request=request_detail.objects.filter(id=request_id)[0]
#     return_date_string = current_request.return_date.strftime("%Y-%m-%d")
#     if current_date_string==return_date_string:
#         current_time_hour = current_date.strftime("%H")
#         current_time_minute = current_date.strftime("%M")
#         if(int(current_time_hour)==16 and int(current_time_minute)==2):
#             current_request.request_status='Overdue'
#             current_request.save()


    # notify_time=current_request.duration
    # if timezone.now() - notify_time > timezone.timedelta(hours=2):
    #     messages.info(request,f'Return the book please')
    # else:
    #     pass
    # return redirect('dummy.html')

