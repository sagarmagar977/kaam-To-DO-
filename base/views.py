from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect #(this is done to import redirect function)





from .models import ToDo

# Create your views here.

def home(request):
     #return HttpResponse("This is homepage!")
     todo_objects = ToDo.objects.all()
     content = {'todos' : todo_objects}
     return render(request,'index.html' , context=content)

def create(request):
     if request.method == 'POST' :
          name = request.POST.get('name')
          description = request.POST.get('description')
          status = request.POST.get('status')
          #print(name,description,status)
          ToDo.objects.create(name=name,description=description,status=status)
          return redirect(home)
     content={'mode':'create'}
     return render(request,'create.html',context=content)
def edit(request,pk):
     todo_object=ToDo.objects.get(id=pk)
     content={'mode':'edit', 'todo':todo_object}
     if request.method== 'POST':
          name=request.POST.get('name')
          description=request.POST.get('description')
          status=request.POST.get('status')
          todo_object.name=name
          todo_object.description=description
          todo_object.status=status
          todo_object.save()
          return redirect('home')
          print(name,description,status)
     return render(request,'create.html',context=content)
def delete(request,pk):
     todo_object=ToDo.objects.get(id=pk)
     todo_object.delete()
     return redirect('home')
def deleteall(request):
      todo_object=ToDo.objects.all()
      todo_object.delete()
      return redirect('home')




####################################################


def summary(request):
    not_done_tasks = ToDo.objects.filter(status='Not Done')
    in_progress_tasks = ToDo.objects.filter(status='In progress')
    done_tasks = ToDo.objects.filter(status='Done')
    
    print(f"Not Done Tasks: {not_done_tasks}")
    print(f"In Progress Tasks: {in_progress_tasks}")
    print(f"Done Tasks: {done_tasks}")
    
    context = {
        'not_done_tasks': not_done_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
    }
    
    return render(request, 'summary.html', context)
