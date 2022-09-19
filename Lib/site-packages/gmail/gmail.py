__author__ = 'Sujit Mandal'
#Date : 07-09-2020
import smtplib 

'''
# Author : Sujit Mandal
Github : https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
'''

#E-mail login credential
gmail_id = ('') #sender g-mail id
gmail_password = ('') #sender g-mail password

#receiver mail id's 
destination_addresses = [
                    'receiver_mail_id_1@gmail.com',
                    'receiver_mail_id_2@gmail.com',
                    'receiver_mail_id_3@gmail.com',
                    '............................',
                    '.............................',
                    'receiver_mail_id_N number@gmail.com',
                    ]
#main subject
subject = ('') #mail subject
#mail message
message = ('') #mail message


class loginCredential:
    def login(self, gmail_id, gmail_password):
        self.gmail_id = gmail_id
        self._password = gmail_password

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.gmail_id, self._password) 
        return(server)

class receiverCredential(loginCredential):
    def receiver_mail(self, destination_addresses):
        self.destination_addresses = destination_addresses

        mail_id = []
        for i in destination_addresses:
            mail_id.append(i)
        return(mail_id)

class gmail(receiverCredential):
     def send_mail(self, subject, message):
        server = self.login(self.gmail_id, self._password)
        destination_addresses = self.receiver_mail(self.destination_addresses)

        content = (f'subject: {subject}\n\n{message}')

        server.sendmail(
            self.gmail_id, 
            destination_addresses, 
            content
        )
        print('An Email has been sent to : {}'.format(' and '.join(destination_addresses)))
        server.quit()

   

if __name__ == '__main__':
    mail = gmail()
    mail.login(gmail_id, gmail_password)
    mail.receiver_mail(destination_addresses)
    mail.send_mail(subject, message)