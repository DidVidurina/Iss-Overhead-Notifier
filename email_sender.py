
import smtplib


class EmailSender:
    def __init__(self):
        super().__init__()
        """update these details with your details, no i dont care that you can see it XD"""
        self.my_email = "100daysofcodemihovil@gmail.com"
        self.my_password = "ilwfyepewllzbylq"

    def send_mail(self):
        with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(from_addr=self.my_email,
                                to_addrs="michaelbaricevic@gmail.com",
                                msg=f"Subject:The ISS is about to cross over!\n\nLook up dummy!")
            connection.close()
