from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/sub", methods=['GET', 'POST'])
def submit(): 
	if request.method == 'POST':
		try:
			grade_1 = int(request.form.get('grade_1'))
			grade_2 = int(request.form.get('grade_2'))
			grade_3 = int(request.form.get('grade_3'))
			grade_4 = int(request.form.get('grade_4'))
			credit_1 = int(request.form.get('credit_1'))
			credit_2 = int(request.form.get('credit_2'))
			credit_3 = int(request.form.get('credit_3'))
			credit_4 = int(request.form.get('credit_4'))
			
			grade_total = (grade_1*credit_1)+(grade_2*credit_2)+(grade_3*credit_3)+(grade_4*credit_4)
			credit_total = credit_1+credit_2+credit_3+credit_4
			gpa = grade_total/credit_total
		except:
			error_message = "All fields must be completed. Please try again"
			return render_template('index.html',error_message=error_message)
		return render_template('index.html',gpa="Your Calculated GPA is "+repr(round(gpa,2)))
