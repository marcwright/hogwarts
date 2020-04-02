from .models import House, Student
from django.shortcuts import render, redirect
from .forms import HouseForm, StudentForm
from django.urls import reverse

def house_list(request):
    houses = House.objects.all()
    # print(houses)
    print(request)
    return render(request, 'house_list.html', {'houses': houses})

def house_detail(request, pk):
    house = House.objects.get(pk=id)
    return res(request, 'house_detail.html', {'house': house})

def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid:
            house = form.save()
            return redirect('house_detail', id = house.id)
    else:
        form = HouseForm()
        return render(request, 'house_form.html', {'form': form})

def house_update(request, pk):
    house = House.objects.get(pk=id)
    if request.method == 'POST':
        form = HouseForm(request.body, instance = house)
        if form.is_valid:
            house = form.save()
            return redirect('house_detail', id = house.id)
    else:
        form = HouseForm(instance = house)
        return render(request, 'house_form.html', {'form': form})

def house_delete(request, id):
    if request.method == 'POST':
        House.objects.get(id = id).delete()
    return redirect('house_list')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def student_create(request):
    print(request.body)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)
        if form.is_valid:
            student = form.save()
            # print(student)
            return redirect(reverse('student_detail', args=(student.id,)))
    else:
        form = StudentForm()
        return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid:
            student = form.save()
            return redirect(reverse('student_detail', args=(student.id,)))
    else:
        form = StudentForm(instance = student)
        return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    if request.method == 'POST':
        Student.objects.get(pk=pk).delete()
    return redirect('student_list')


# https: // stackoverflow.com/questions/45135263/class-has-no-objects-member

# INSERT INTO hogwarts_house(name, image_url) VALUES('marc', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Hogwarts_Castle_%2843281949792%29.jpg/1200px-Hogwarts_Castle_%2843281949792%29.jpg')

# 'bytes' no attribute 'get' error
# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/

# _reverse_with_prefix() argument after * must be an iterable, not int
# https: // stackoverflow.com/questions/52575418/reverse-with-prefix-argument-after-must-be-an-iterable-not-int
