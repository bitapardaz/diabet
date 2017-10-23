from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utilities import send_sms_to_mobile
from models import UserProfile, RegistrationPath, Gender, Education, MedicationType, DiabeticsType
from models import Question,QuestionareItem

from django.contrib.auth.models import User
import random

def generate_random():
    return random.randrange(1000, 9999)

def process_answer(answer):
    if answer == "0":
        return False
    if answer == "1":
        return True

def process_questionare(request,profile):
    a_1 = process_answer(request.data.get('question_1'))
    question = Question.objects.get(front_end_short_code = "question_1")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_1)
    questionare_item.save()

    a_2 = process_answer(request.data.get('question_2'))
    question = Question.objects.get(front_end_short_code = "question_2")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_2)
    questionare_item.save()

    a_3 = process_answer(request.data.get('question_3'))
    question = Question.objects.get(front_end_short_code = "question_3")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_3)
    questionare_item.save()

    a_4 = process_answer(request.data.get('question_4'))
    question = Question.objects.get(front_end_short_code = "question_4")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_4)
    questionare_item.save()

    a_5 = process_answer(request.data.get('question_5'))
    question = Question.objects.get(front_end_short_code = "question_5")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_5)
    questionare_item.save()

    a_6 = process_answer(request.data.get('question_6'))
    question = Question.objects.get(front_end_short_code = "question_6")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_6)
    questionare_item.save()

    a_7 = process_answer(request.data.get('question_7'))
    question = Question.objects.get(front_end_short_code = "question_7")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_7)
    questionare_item.save()


    a_8 = process_answer(request.data.get('question_8'))
    question = Question.objects.get(front_end_short_code = "question_8")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_8)
    questionare_item.save()


    a_9 = process_answer(request.data.get('question_9'))
    question = Question.objects.get(front_end_short_code = "question_9")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_9)
    questionare_item.save()

    a_10 = process_answer(request.data.get('question_10'))
    question = Question.objects.get(front_end_short_code = "question_10")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_10)
    questionare_item.save()

    a_11 = process_answer(request.data.get('question_11'))
    question = Question.objects.get(front_end_short_code = "question_11")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_11)
    questionare_item.save()

    a_12 = process_answer(request.data.get('question_12'))
    question = Question.objects.get(front_end_short_code = "question_12")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_12)
    questionare_item.save()

    a_13 = process_answer(request.data.get('question_13'))
    question = Question.objects.get(front_end_short_code = "question_13")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_13)
    questionare_item.save()

    a_14 = process_answer(request.data.get('question_14'))
    question = Question.objects.get(front_end_short_code = "question_14")
    questionare_item = QuestionareItem(user=profile.user,
                                   question=question,
                                   answer = a_14)
    questionare_item.save()


@api_view(['POST'])
def register_customer_data(request):

    #registration path = "healthy, 2"
    #registration path = "susceptible, 1"
    #registration path = "infected, 0"

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
    print "you are here"
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

        # remove all answers from the database from the user.
        relevant_question_items = QuestionareItem.objects.filter(user=profile.user)
        for item in relevant_question_items:
            item.delete()

        # insert user data and append teh questionare items to the profile.
        process_questionare(request,profile)

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
