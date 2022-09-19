import poplib
import re
import os
from email.parser import BytesParser
from email.policy import default
from config import Main_Attribute
from connecting_pop import Conection_to_pop
from ceate_dir import Create_diraction


def pop_condition():
    user = input("Введите ваш e-mail: ")
    password = input("Введите ваш пароль: ")
    mkdir = input("Введите путь в папку: ")

    attrubut = Main_Attribute(user_name=user, password=password)

    server = Conection_to_pop(user_name=attrubut.user, password=attrubut.passw_)
    server.connection_to_mail()

    try:
        diraction = Create_diraction(mkdir)
        diraction.creat_dir()
        dir = diraction.dir
    except Exception as ex:
        return ' The Diraction is failde '

    pop_server = server.pop_server

    #pop_server_name = 'pop3.mail.ru'
    #user_name = 'test-pop3_ssl@mail.ru'
    #passw_ = 'KP39LA7y8Shh1GNaFAwX'

    resp = len(pop_server.list()[1])

    r = pop_server.retr(resp)
    bp = BytesParser(policy=default).parsebytes(b'\r\n'.join(r[1]))

    for part in bp.walk():
        xml_file_name = part.get_filename()
        if part.get_content_maintype() == 'application':

            r_xml = re.findall(r"\.xlsx|\.xls", xml_file_name)# list
            body = part.get_payload(decode=True)# сохраняем file xlsx в переменную
            with open(f'{diraction.dir}/{xml_file_name}', 'wb') as file:
                file.write(body)

    server.quit()


def main():
    pop_condition()


if __name__ == '__main__':
    main()