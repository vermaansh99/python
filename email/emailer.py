import smtplib

smtpObj = smtplib.SMTP("smtp.gmail.com",587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("anshverma2073@gmail.com","ovbzumtnvuyqhizd")

smtpObj.sendmail("anshverma2073@gmail.com","saif816@gmail.com","sending mail through python")
smtpObj.quit()