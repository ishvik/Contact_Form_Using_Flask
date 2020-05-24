from flask import Flask, render_template, request, flash
from flask_mail import Mail
import json


with open('config.json', 'r') as c:
	params=json.load(c)["param"]

local_server=True
app=Flask(__name__)
app.secret_key="It's Personal"
app.config.update(
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT='465',
	MAIL_USE_SSL=True,
	MAIL_USERNAME=params['gmail-user'],
	MAIL_PASSWORD=params['gmail-password']

)
	
mail=Mail(app)




@app.route("/",methods=['GET','POST'])
def signin():
	if(request.method=='POST'):
		fn=request.form.get('fn')
		ln=request.form.get('ln')
		email=request.form.get('email')
		password=request.form.get('password')
		PhoneNo=request.form.get('PhoneNo')
		mail.send_message('New Entry', 
			sender=email, 
			recipients = [params['gmail-user']],
			body='First Name = ' + fn + ' ' + 'Last Name = ' + ln + ' ' + 'Email = ' + email + ' ' +'Contact No. = ' 
			+ PhoneNo)
		if(mail.send_message):
			flash("Registered Successfully....!!!")
			return render_template('msg.html')
		else:
			flash("Something went wrong :(")
	return render_template('sign.html',param=params)

# @app.route('/message')
# def message():
	
#     return redirect(url_for('signin')


app.run(debug=True)
