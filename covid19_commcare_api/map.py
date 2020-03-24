
#WARNING: this function returns in complete data
# due to inconsistencies in the two forms it tries to map across

#this takes a commcare door-to-door form and maps it to the
#community API spec

def map_to_communityinspection(submissions):

    print('WARNING: returning incomplete data due to inconsistencies in the two forms it tries to map across. needs fixing')

    response = []
    
    for s in submissions:

        template = {"FullName": "string", \
            "Sex": "", \
            "Age": 0, \
            "Region": "", \
            "SubcityOrZone": "", \
            "Woreda": "", \
            "Kebele": "", \
            "HouseNo": "", \
            "PhoneNo": "", \
            "Occupation": "", \
            "CallDate": None, \
            "CallerType": "", \
            "Fever": False, \
            "Cough": False, \
            "Headache": False, \
            "RunnyNose": False, \
            "UnwellnessFeeling": False, \
            "BreathingDifficulty": False, \
            "BodyPain": False, \
            "TravleHx": False, \
            "HaveSex": False, \
            "AnimalMarket": False, \
            "HealthFacility": False, \
            "ReceiverName": "", \
            "FormStatus": "", \
            "Source": "", \
            "Version": 0, \
            "ID": -1, \
            "CreatedDate": "", \
            "ModifiedDate": "" }

        form = s['form']

        template['FullName'] = form['patient_identifier_information']['basic_demo']['patient_first_name']  + \
                            ' ' + form['patient_identifier_information']['basic_demo']['patient_family_name']
        
        age = form['patient_identifier_information']['basic_demo']['age']
        if (age == "") or (not age.isdigit()): age = 0
        template['Age'] = int(age)


        template['Sex'] = form['patient_identifier_information']['basic_demo']['sex']

        template['CreatedDate'] = s['received_on']
        template['ModifiedDate'] = form['case']['@date_modified']
        template['CallDate'] = template['ModifiedDate']


        
        

        template['Region'] = form['patient_identifier_information']['address']['region'] 
        template['SubcityOrZone'] = form['patient_identifier_information']['address']['kifle_ketema_zone']
        #template['Kebele'] = form['patient_identifier_information']['address']['kebele']
        template['HouseNo'] = form['patient_identifier_information']['address']['house_number']
        #template['PhoneNo'] = form['patient_identifier_information']['basic_demo']['phone_number']
        template['Woreda'] = form['patient_identifier_information']['address']['wereda']

        symptoms_str = form['patient_identifier_information']['symptoms_list']['symptoms']
        symptoms_list = symptoms_str.split(" ")
        if 'cough' in symptoms_list: template['Cough'] = True
        if 'fever' in symptoms_list: template['Fever'] = True
        if 'shortness_of_breath' in symptoms_list: template['BreathingDifficulty'] = True
        if 'runny_nose' in symptoms_list: template['RunnyNose'] = True

        response.append(template)

    return response
