from . import sms
def sms_notify(message):
    username = input("UserName :")
    password = input("Password :")
    q=sms.Sms(username,password)
    mobile_number_to_send = input("Mobile Number to send :")
    q.send(mobile_number_to_send,message)
    # n=q.msgSentToday()
    q.logout()