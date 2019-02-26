import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

class SendMail():
   def __init__(self,sender_email,recevier_email,cc_email):
      self.sender_email = sender_email
      self.recevier_email = recevier_email
      self.cc_email = cc_email

   def send_mail_with_attachment(self,filepath):
      """creating a obj MIMEMultipart """
      msg = MIMEMultipart() 

      """storing the sender and recevier mail with subject"""
      msg['From'] = self.sender_email
      msg['To'] = self.recevier_email
      msg['Cc'] = self.cc_email
      msg['Subject'] = "Test mail with attachment"
	
      """attach the body"""
      body = "kindly find the attachment"
      msg.attach(MIMEText(body, 'plain')) 

      """attachment"""
      attachment = open(filepath, "rb") 
      mail_attach = MIMEBase('application', 'octet-stream') 
      mail_attach.set_payload((attachment).read()) 
      encoders.encode_base64(mail_attach) 
      mail_attach.add_header('Content-Disposition', "attachment; filename= %s" % "practise2.csv") 
      msg.attach(mail_attach) 

      """creating a session"""
      mail_server = smtplib.SMTP('**************', ***)
      """start TLS for security """
      mail_server.starttls()
      mail_server.login("@@@@@@@@@@@@@@@", "@@@@@@@@@@@") 
      text = msg.as_string() 
      mail_server.sendmail(msg['From'],msg['To'],text) 
      mail_server.quit() 


if __name__ == '__main__':
   a = SendMail("##############","##########","###########")
   a.send_mail_with_attachment("/home/user/Documents/practise2.csv")
