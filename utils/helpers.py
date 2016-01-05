from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(queryset,page_no,page_size):
    paginator = Paginator(queryset, page_size)
    try:
        data = paginator.page(page_no)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    return data
