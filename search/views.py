from django.shortcuts import render
from home.models import Alumni_Profile
from django.db.models import Q
# Create your views here.

def search_view(request):
    disciplines = list(set(Alumni_Profile.objects.values_list('discipline',flat=True).filter(is_verified=True)))
    disciplines.sort()
    disciplines.insert(0,'All (in AMSKU)')
    print(disciplines)
    
    batch = list(set(Alumni_Profile.objects.values_list('batch',flat=True).filter(is_verified=True)))
    batch.sort()
    batch.insert(0,'All (in AMSKU)')
    
    context={
        'disciplines': disciplines,
        'batches': batch,
    }
    return render(request,"search/search_view.html",context)

def search_result(request):
    discipline = request.POST['discipline']
    batch = request.POST['batch']

    searched_dict = {
        'discipline':discipline,
        'batch':batch,
    }
    
    final_query = Alumni_Profile.objects.filter(is_verified=True)
    for x in searched_dict:
        if searched_dict[x]!='All (in AMSKU)':
            query = Alumni_Profile.objects.filter(**{x: searched_dict[x]})
            final_query = final_query.intersection(query)
        else:
            pass
    # print(final_query)
    context={
        'profiles':final_query,
    }
    return render(request,"search/search_results.html",context)


def advance_search_results(request):
    field_list = ['full_name','discipline','batch','student_id','job_type','job_position','higher_study','present_address','present_country','parmanent_address']

    value = request.POST['search']
    context = {}

    if value:
        for x in field_list:
            field_column = x
            st = field_column + '__icontains'
            query = Alumni_Profile.objects.filter(Q(**{st:value}) & Q(is_verified=True))
            
            if query.exists():
                context[field_column]=query
            else:
                pass
    else:
        pass

    return render(request,"search/advance_search_results.html",{'profiles':context})