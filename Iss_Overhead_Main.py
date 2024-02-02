import time
from email_sender import EmailSender
from night_checker import NightChecker
from iss_checker import IssChecker


iss_checker = IssChecker()
night_checker = NightChecker()
email_sender = EmailSender()

checker_on = True
while checker_on:
    iss_checker.fetch_data()
    iss_checker.check_proximity()
    night_checker.checker_return()
    night = night_checker.night
    long_close = iss_checker.long_close
    lat_close = iss_checker.lat_close
    iss_close = iss_checker.close
    if iss_close:
        if night:
            print("Iss Close!")
            print("is night!")
            print(iss_checker.iss_longitude, iss_checker.iss_latitude)
            email_sender.send_mail()
        else:
            print("iss close!")
            print("is not night!")
            print(iss_checker.iss_longitude, iss_checker.iss_latitude)
            email_sender.send_mail()
    else:
        print(f"Iss Far!")
        print(iss_checker.iss_longitude,iss_checker.iss_latitude)
    iss_checker.fetch_data()
    iss_checker.check_proximity()
    night_checker.checker_return()

    time.sleep(60)
