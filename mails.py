from credenciales import mail, password
import yagmail

print(mail)
print(password)

yag = yagmail.SMTP(mail, password) 

contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('desouza030689@gmail.com', 'subject', contents)

# Alternatively, with a simple one-liner:
# yagmail.SMTP(USERNAME).send('to@someone.com', 'subject', contents)