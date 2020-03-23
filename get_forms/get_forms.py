
import requests


#TODO: get as an argument; also support tokens?
#for the time being you need to hard-code the commcare username and password
USER_NAME = ''
PASSWORD = ''


#  ----------------------------------------------------------------------------
# we use the List Forms API, documented here: 
#     https://confluence.dimagi.com/display/commcarepublic/List+Forms

# We have 3 types of form submissions in commcare:
#     - Border Registration (Traveler Registration)
#     - Door-to-Door
#     - Patient Registration


# All off these implemented as part of the same commcare application, and stored as 
# part of the same type of form. This module fetches the full "master" table and filter out entires that
# belong to a specific "sub-form"

#  ----------------------------------------------------------------------------



FORM_XMLNS = 'http://openrosa.org/formdesigner/158EB23A-DCFF-4680-90DA-A52D95628A8C'
FROM_APPP_ID = '7c00659a2a5f4ce8aa635c879f54e136'

BASE_URL =  'https://www.commcarehq.org/a/ethiocovid19/api/v0.5/form/?xmlns={0}&app_id={1}'.format(FORM_XMLNS, FROM_APPP_ID)


def fetch_border_registration(limit = 20, offset = 0):
    return fetch_form_submissions('border_registration', limit, offset)

def fetch_patient_registration(limit = 20, offset = 0):
    return fetch_form_submissions('patient_registration', limit, offset)

def fetch_door_to_door(limit = 20, offset = 0):
    return fetch_form_submissions('door_to_door', limit, offset)



def fetch_form_submissions(form_type, limit=20, offset=0):
   
    url = BASE_URL  + "&limit={0}&offset={1}".format(limit, offset)
    print(url)  
    resp = requests.get(url, auth=(USER_NAME, PASSWORD))

    if resp.status_code == 200: return filter_form_submissions(form_type, resp.json())
    else:
        print("Error: " + str(resp.status_code) + '\n\t Requested: ' +  url )
        raise Exception('Error: {0}'.format(resp.status_code))


# there is a registration_type filed which tells us what sub-form a submission belongs
# belongs to
def filter_form_submissions(form_type, json_response):

    forms_submissions = []

    for form_object in json_response['objects']:

        if('registration_type' not in form_object['form']):
            print("WARNING: extra tables being fetched")
            continue

        if form_object['form']['registration_type'] == form_type:
            forms_submissions.append(form_object)

    return forms_submissions
    

if __name__ == "__main__":
    print( fetch_border_registration() )

    print( fetch_patient_registration() )

    print( fetch_door_to_door() )