import smtplib

smtpObj = smtplib.SMTP("smtp.gmail.com",587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("anshverma2073@gmail.com","ovbzumtnvuyqhizd")

smtpObj.sendmail("anshverma2073@gmail.com","sb78639@gmail.com","Testing Message")
smtpObj.quit()