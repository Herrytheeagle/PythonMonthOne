
    # Summary of service firms' type and operational levels of respondents.
    def ss_firms():
    # printing strings
    print("SUMMARY OF SERVICE FIRMS'TYPE AND OPERATION LEVEL OF RESPONDENTS")
    print("Type of Firms","No of Firms","Operational management","Middle management","Senior management","Total type","% Types of Firms")
   
    # declaration of variables for number of firms under each service.
    noConsultancyServices = 0
    noBankingServices = 0
    noTechnologyServices = 0
    noTelecommunicationServices = 0
    noInsuranceServices = 0
    total_type = (noConsultancyServices + noBankingServices + noTechnologyServices + noTelecommunicationServices + noInsuranceServices)

    # declaration of variables for the operational management of each service.
    noConsultancyServices_OP = 0
    noBankingServices_OP = 0
    noTechnologyServices_OP = 0
    noTelecommunicationServices_OP = 0
    noInsuranceServices_OP = 0
    total_OP = (noConsultancyServices_OP + noBankingServices_OP + noTechnologyServices_OP + noTelecommunicationServices_OP + noInsuranceServices_OP)

    # declaration of variables for the middle management of each service.
    noConsultancyServices_MM = 0
    noBankingServices_MM = 0
    noTechnologyServices_MM = 0
    noTelecommunicationServices_MM = 0
    noInsuranceServices_MM = 0
    total_MM = (noConsultancyServices_MM + noBankingServices_MM + noTechnologyServices_MM + noTelecommunicationServices_MM + noInsuranceServices_MM)

    # declaration of variables for the Senior management of each service.
    noConsultancyServices_SM = 0
    noBankingServices_SM = 0
    noTechnologyServices_SM = 0
    noTelecommunicationServices_SM = 0
    noInsuranceServices_SM = 0
    total_SM = (noConsultancyServices_SM + noBankingServices_SM + noTechnologyServices_SM + noTelecommunicationServices_SM + noInsuranceServices_SM)

    # declaration of variables for the  total type of each service.
    noConsultancyServices_TT = (noConsultancyServices_OP + noConsultancyServices_MM + noConsultancyServices_SM)
    noBankingServices_TT = (noBankingServices_OP + noBankingServices_MM + noBankingServices_SM)
    noTechnologyServices_TT = (noTechnologyServices_OP + noTechnologyServices_MM + noTechnologyServices_SM)
    noTelecommunicationServices_TT = (noTelecommunicationServices_OP + noTelecommunicationServices_MM + noTelecommunicationServices_SM)
    noInsuranceServices_TT = (noInsuranceServices_OP + noInsuranceServices_MM + noInsuranceServices_SM)
    total_TT = (noConsultancyServices_TT + noBankingServices_TT + noTechnologyServices_TT + noTelecommunicationServices_TT + noInsuranceServices_TT)

    # printing the "summary of service" from firms.
    print("Consultancy and service", noConsultancyServices, noConsultancyServices_OP, noConsultancyServices_MM, noConsultancyServices_SM, noConsultancyServices_TT)
    print("Banking", noBankingServices, noBankingServices_OP, noBankingServices_MM, noBankingServices_SM, noBankingServices_TT)
    print("Technology", noTechnologyServices, noTechnologyServices_OP, noTechnologyServices_MM, noTechnologyServices_SM, noTechnologyServices_TT)
    print("Telecommunications service", noTelecommunicationServices, noTelecommunicationServices_OP, noTelecommunicationServices_MM, noTelecommunicationServices_SM, noTelecommunicationServices_TT)
    print("Insurance", noInsuranceServices, noInsuranceServices_OP, noInsuranceServices_MM, noInsuranceServices_SM)
    print("Total", total_type, total_OP, total_MM, total_SM, total_TT)

    # calling the function.
    ss_firms()