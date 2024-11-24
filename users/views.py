# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .forms import UserRegistrationForm
from django.shortcuts import render
import pandas as pd

from django.shortcuts import redirect
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')  # Redirect to a login page or another page
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/register.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
#from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login as auth_login



# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('success_url')  # This should now work correctly
#     else:
#         form = UserRegistrationForm()
    
#     return render(request, 'users/register.html', {'form': form})
def home_view(request):
    return render(request,'users/home_page.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debugging line
            user = form.save()
            print("User saved to database:", user)  # Debugging line
            return redirect('success_url')
        else:
            print(form.errors)  # This will show form errors in the terminal
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})


def success_view(request):
    return render(request, 'users/success.html')  # Create a success.html template



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)  # Log the user in
                # Redirect based on user role
                if user.role == 'fleet_manager':
                    return redirect('fleet_manager_home')  # Replace with your fleet manager page
                elif user.role == 'driver':
                    return redirect('driver_home')  # Replace with your driver page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})



def fleet_manager_home_view(request):
    # Logic for the fleet manager's home page
    return render(request, 'users/fleet_manager_home.html')

def driver_home_view(request):
    # Logic for the driver's home page
    return render(request, 'users/driver_home.html')



from django.shortcuts import render

def introduction_to_ev(request):
    return render(request, 'users/introduction_to_ev.html')

def dataset(request):
    return render(request, 'users/dataset.html')

def distribution(request):
    return render(request, 'users/distribution.html')

def relationship(request):
    return render(request, 'users/relationship.html')

def vehicle_status(request):
    return render(request, 'users/vehicle_status.html')

def prediction_view(request):
    return render(request, 'users/prediction.html')  # Adjust as needed




# def distribution_view(request):
#     return render(request, 'users/distribution.html')


def redirect_to_distribution(request):
    return redirect('http://127.0.0.1:5000/')  # Redirect to Flask app running on port 5000
import pandas as pd
from django.shortcuts import render

def vehicle_status(request):
    # Load the dataset
    df = pd.read_csv('Datasets/Final_EV_Fleet_Dataset.csv')  # Adjust the path to your CSV file
    
    # Check if 'Status' column exists
    if 'Status' not in df.columns:
        return render(request, 'users/vehicle_status.html', {'error': "'Status' column not found in the dataset."})

    # Count the occurrences of each status
    status_counts = df['Status'].value_counts()

    # Prepare the data for the bar chart
    data = {
        'labels': ['No', 'Yes'],  # Assume 0 -> 'No' and 1 -> 'Yes'
        'values': [status_counts.get(0, 0), status_counts.get(1, 0)]  # Default to 0 if not found
    }

    # Pass the data to the template
    return render(request, 'users/vehicle_status.html', {'data': data})
from django.shortcuts import redirect

def relationship_view(request):
    # Redirect to the Gradio app running on localhost:7860
    return redirect("http://127.0.0.1:8502/")


def predict_electric_range(request):
    # Redirect to the Gradio app running on localhost:7860
    return redirect("http://127.0.0.1:8503/")

# from django.shortcuts import render
# from django.http import JsonResponse
# import pickle
# import os
# from django.conf import settings

# # Load the model from pickle
# model_path = os.path.join(settings.BASE_DIR, 'users', 'models', 'evmod (1).pkl')
# with open(model_path, 'rb') as file:
#     model = pickle.load(file)

# def predict_electric_range(request):
#     if request.method == 'POST':
#         # Get input values from the form
#         make = request.POST.get('make')
#         battery_level = request.POST.get('battery_level')
        
#         # You can add more preprocessing steps if required (e.g., encoding categorical features)
        
#         # Create input data for prediction
#         # Ensure the input data format matches the model's expected input
#         prediction_input = [[make, battery_level]]  # Ensure this matches the training data format

#         # Predict using the loaded model
#         predicted_range = model.predict(prediction_input)
        
#         # Render the result in the template
#         return render(request, 'users/prediction.html', {'predicted_range': predicted_range[0]})

#     return render(request, 'users/prediction.html')  # If GET request, just show the form
