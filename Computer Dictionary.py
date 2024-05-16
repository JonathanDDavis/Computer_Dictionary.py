#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     19/09/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
computer1= {
    "Make:": "Alienware/Dell",
    "Model:": "Aurora",
    "Year:": "2019",
    "CPU:": "Intel",
    "RAM:": "64GB",
    "GPU:": "Nvidia",
    "isWorking" : True,
}

computer2= {
    "Make:": "Toshiba",
    "Model:": "Satellite A505-S6980",
    "Year:": "2009",
    "CPU:": "Intel Core 2",
    "RAM:": "4GB",
    "GPU:": "Intel GMA 4500MHD",
    "isWorking" : True,
}

computer3= {
    "Make:": "Lenovo",
    "Model:": "ThinkPad E590",
    "Year:": "2015",
    "CPU:": "Intel Core i5-8265U 1.60 GHz",
    "RAM:": "4GB",
    "GPU:": "Intel UHD Graphics 620",
    "isWorking" : False,
}

computer4= {
    "Make:": "Acer",
    "Model:": "Aspire 5",
    "Year:": "2016",
    "CPU:": "Intel Core i5-8265U 1.60 GHz",
    "RAM:": "8GB",
    "GPU:": "NVIDIA GeForce MX250",
    "isWorking" : True,
}

computer5= {
    "Make:": "ASUS",
    "Model:": "ZenBook",
    "Year:": "Nvidia",
    "CPU:": "Intel Core i7-8565U 1.80 GHz",
    "RAM:": "16GB",
    "GPU:": "NVIDIA GeForce GTX 1050 Max-Q",
    "isWorking" : True,
}

computers= {
    "computer1": computer1,
    "computer2": computer2,
    "computer3": computer3,
    "computer4": computer4,
    "computer5": computer5,
}

computersBackup = computers.copy()

print(computers)

dict.clear(computers)

print(computersBackup)
