from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utilities import send_sms_to_mobile
from models import UserProfile, RegistrationPath, Gender, Education, MedicationType, DiabeticsType

from django.contrib.auth.models import User


import random

def generate_random():
    return random.randrange(1000, 9999)

@api_view(['POST'])
def register_customer_data(request):

    #registration path = "healthy, 0"
    #registration path = "susceptible, 1"
    #registration path = "infected, 2"


    registration_path = RegistrationPath.objects.get( code = int(request.data.get('registration_path_code'))  )
    mobile_number = request.data.get('mobile_number')
    profile = UserProfile.objects.get(mobile_number = mobile_number)

    print "registration_path.code"
    print registration_path.code

    # healthy
    if registration_path.code == 2 :

        profile.user.first_name = request.data.get('name')
        profile.user.email = request.data.get('email')
        profile.user.save()

        profile.registration_path = registration_path

        profile.birth_day = int( request.data.get('birth_day') )
        profile.birth_month = int( request.data.get('birth_month') )
        profile.birth_year = int( request.data.get('birth_year') )
        profile.national_code = request.data.get('national_code')

        gender_code = request.data.get('gender_code')
        profile.gender = Gender.objects.get(code = gender_code)

        education_code = request.data.get('education_code')
        profile.education = Education.objects.get(code = education_code)

        profile.postal_code = request.data.get('postal_code')


        profile.save()

        output= {}
        output['status'] = 0
        return Response(output)

    # infected
    if registration_path.code == 0:

        profile.user.first_name = request.data.get('name')
        profile.user.email = request.data.get('email')
        profile.user.save()

        profile.registration_path = registration_path
        profile.birth_day = int( request.data.get('birth_day') )
        profile.birth_month = int( request.data.get('birth_month') )
        profile.birth_year = int( request.data.get('birth_year') )
        profile.national_code = request.data.get('national_code')

        gender_code = request.data.get('gender_code')
        profile.gender = Gender.objects.get(code = gender_code)

        education_code = request.data.get('education_code')
        profile.education = Education.objects.get(code = education_code)

        profile.postal_code = request.data.get('postal_code')

        profile.height = int(request.data.get('height'))
        profile.weight = int(request.data.get('weight'))
        profile.diagnosis_year = int(request.data.get('diagnosis_year'))
        profile.fasting_blood_sugar = int(request.data.get('fasting_blood_sugar'))
        profile.medication_type = MedicationType.objects.get(code = int(request.data.get('medication_type_code') ) )
        profile.diabetics_type = DiabeticsType.objects.get(code = int(request.data.get('diabetics_type_code') ) )

        profile.save()

        output= {}
        output['status'] = 0
        return Response(output)


    # susceptible
    if registration_path.code == 1:

        print "you are here."
        profile.user.first_name = request.data.get('name')
        profile.user.email = request.data.get('email')
        profile.user.save()

        profile.registration_path = registration_path
        profile.birth_day = int( request.data.get('birth_day') )
        profile.birth_month = int( request.data.get('birth_month') )
        profile.birth_year = int( request.data.get('birth_year') )
        profile.national_code = request.data.get('national_code')

        gender_code = request.data.get('gender_code')
        profile.gender = Gender.objects.get(code = gender_code)

        education_code = request.data.get('education_code')
        profile.education = Education.objects.get(code = education_code)

        profile.postal_code = request.data.get('postal_code')

        profile.height = int(request.data.get('height'))
        profile.weight = int(request.data.get('weight'))
        profile.diagnosis_year = int(request.data.get('diagnosis_year'))
        profile.fasting_blood_sugar = int(request.data.get('fasting_blood_sugar'))
        profile.medication_type = MedicationType.objects.get(code = int(request.data.get('medication_type_code') ) )
        profile.diabetics_type = DiabeticsType.objects.get(code = int(request.data.get('diabetics_type_code') ) )

        profile.save()

        output= {}
        output['status'] = 0
        return Response(output)


    return Response("You cannot register.")


@api_view(['POST'])
def send_sms(request):

    # creates a user if does not exist
    # does not create a new user if it already exists

    output = {}

    mobile_number=request.data.get('mobile_number')

    try:
        profile = UserProfile.objects.get(mobile_number=mobile_number)
        output["customer_status"]= "returning_customer"
        output["status"]= "0"
        return Response(output)

    except UserProfile.DoesNotExist:

        user = User.objects.create_user(username=mobile_number,password=mobile_number)
        otp_token = generate_random()
        otp_valid = True

        profile = UserProfile(user=user,
                              mobile_number=mobile_number,
                              otp_token=otp_token,
                              otp_valid = otp_valid)
        profile.save()

        result = send_sms_to_mobile(mobile_number,otp_token)

        if result == 0:
            output["customer_status"]= "new_customer"
            output["status"] = "0"
        else:
            output["customer_status"]= "new_customer"
            output["status"] = "1"

        return Response(output)


@api_view(['POST'])
def verify_code(request):

    output = {}
    mobile_number = request.data.get('mobile_number')
    token = request.data.get('token')
    print token
    print type(token)

    try:
        profile = UserProfile.objects.get(mobile_number=mobile_number)
        print "OTP valid status"
        print profile.otp_valid

        print str(profile.otp_token)
        print type(unicode(profile.otp_token))

        if unicode(profile.otp_token) == token:
            output['status'] = '0'
            output['message'] = 'customer_verified'
            profile.otp_valid = False
            profile.save()

        #if unicode(profile.otp_token) == token  :
        #    output['status'] = '0'
        #    output['message'] = 'account_already_created_or_deactivated'

        else:
            output['status'] = '1'
            output['message'] = 'wrong_code'
            profile.otp_valid = False
            profile.save()

        return Response(output)

    except UserProfile.DoesNotExist:
        output['status'] = '1'
        output['message'] = 'customer_not_found'
