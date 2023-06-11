from challenge.PropertyManager import PropertyManager

if __name__ == '__main__':
    name = input("Enter Your Name: ")
    IDX = input("Enter Your ID: ")
    pm = PropertyManager(name, IDX)

    print("Hello ", pm.name)
    option_property = pm.prefered_activity("Please select any of the given option: \n[1] = Add a new property \n[2] = Delete an existing property \n")
    if option_property == 1:
        pm.create_property()
    else:
        raise Exception("Sorry, this option hasn't been implmented yet")

    option_application = pm.prefered_activity("Please select any of the given option: \n[1] = Add a new applicant \n[2] = Delete an existing applicant \n")

    if option_application == 1:
        [pm.create_applicant() for _ in range(0,2)]
    else:
        raise Exception("Sorry, this method hasn't been implmented yet") 
    applicant_name = pm.best_applicant()
    print("The best applicant is: ", applicant_name) #if two applicants has same r2i, the first applicant is recommended