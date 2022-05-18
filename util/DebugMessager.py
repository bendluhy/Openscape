import datetime


#System that manages error and debug messages to be easier to read and see when they occurred

def errormessage(context, err):
    errtime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[ERROR|{errtime}]{context} : {err}")

def debugmessage(context, msg):
    msgtime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[MSG|{msgtime}]{context} : {msg}")