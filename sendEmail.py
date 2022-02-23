# This program waits until the network is up, get's the IP address of the Raspberry PI and
# emails it to you. This is written in Python 3.


# Required Python 3 modules
def sendEmail(to, subject,body):
	import smtplib
	import subprocess
	import urllib.request
	import time
	from email.message import EmailMessage

	# Configuration parameters. Since we put the password for the email account in
	# the program is why we use a throw away gmail account.
	# Configure the following 3 lines as needed for your istallation.
	gmail_user = "rpihi1219@gmail.com"
	gmail_password = "Bimbim1?"


	# This makes sure the network is up by trying to access google.com via http. If it fails
	# it waits 30 seconds and trys again. This is an infinite loop. It will never exit if the network
	# doesn't come up.

	while True:
		try:
			urllib.request.urlopen("http://www.google.com").close()
		except urllib.request.URLError:
			print("Network not up yet")
			time.sleep(30)
		else:
			print("Network connected")
			break

	# Get the IP address, hostname and create the email message parameters.

	# Try and send it. It will print out an error message if it can't be sent. This is
	# most likely a firewall issue.
	msg = EmailMessage()
	msg.set_content(body)

	msg['Subject'] = subject
	msg['From'] = gmail_user
	msg['To'] = to


	try:
		# Send the message
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(gmail_user, gmail_password)
		server.send_message(msg)
		server.quit()
		print("Email sent!")
	except:
		print("Something went wrong")