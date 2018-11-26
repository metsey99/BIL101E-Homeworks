
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, request
from csv import reader

contents = []
input_file = open("a2_input.csv","r")
for row in reader(input_file):
	contents = contents + [row]
	
def full_table(year):
	hdr = "<tr>\n"
	for n in range(0,20):
		hdr += "<td>"+contents[0][n]+"</td>\n"
	hdr += "</tr>\n"
	hdr += "<tr>\n"
	for ir in range(0,20):	
		hdr += "<td>"+contents[1][ir]+"</td>\n"
	hdr += "</tr>"
	data = "<tr>\n"
	for rows in range(2,21):
		if contents[rows][0] == year:
			for i in range(0,20):
				data += "<td>"+contents[rows][i]+"</td>\n"
	data += "</tr>"
	return htmltable % (year, hdr+data)
def pe(year):
	hdr = "<tr>\n"
	for n in range(0,10):
		hdr += "<td>"+contents[0][n]+"</td>\n"
	hdr += "</tr>\n"
	hdr += "<tr>\n"
	for ir in range(0,10):	
		hdr += "<td>"+contents[1][ir]+"</td>\n"
	hdr += "</tr>"
	data1 = "<tr>\n"
	for rows in range(2,21):
		if contents[rows][0] == year:
			for i in range(0,10):
				data1 += "<td>"+contents[rows][i]+"</td>\n"
	data1 += "</tr>"
	return htmltable % (year, hdr+data1)
def se(year):
	hdr = "<tr>\n"
	for n in range(11,20):
		hdr += "<td>"+contents[0][n]+"</td>\n"
	hdr += "</tr>\n"
	hdr += "<tr>\n"
	for ir in range(11,20):	
		hdr += "<td>"+contents[1][ir]+"</td>\n"
	hdr += "</tr>"
	data2 = "<tr>\n"
	for rows in range(2,21):
		if contents[rows][0] == year:
			for i in range(11,20):
				data2 += "<td>"+contents[rows][i]+"</td>\n"
	data2 += "</tr>"
	return htmltable % (year, hdr+data2)
	
def contactus():
	return htmlcont
	
def fulltable():
	datas = ""
	for rows in range(0, 21):
		for cols in range(0, 20):
			if cols == 0:
				datas += ("			<tr>")
			datas += "<td>"+str(contents[rows][cols])+"</td>"
			if cols == 19:
				datas += ("			</tr>")
	return htmltable % ("Full table", datas)

def feedback():
	feedback_file = open("feedback.txt","a") 
	nam = request.POST['name']
	fedback = request.POST['feedback']
	gender = request.POST['gender']
	if gender == "male":
		gender = "Mr. "
	elif gender == "female":
		gender = "Ms. "
	elif gender == "":
		gender = ""
	feedback_file.write("\n"+nam+" sended: ")
	feedback_file.write(fedback)
	feedback_file.close() 
	greet = "Thanks "+gender+nam+"\n"+" <a href='./'>Go to main page</a>"
	return greet
	
htmltable = '''<!DOCTYPE html>
<html lang="en"> 
	<head>
		<title>%s</title>
		<link rel="stylesheet" type="text/css" href="style.css">
		<style>
			body{
				background-color: white;
			}
		</style>
	</head>
	<body>
		<div id="header">
			<div id="logo">
				<h1>Assignment#3</h1>
			</div>
			<div id="menu">
				<h2>
					<a href="./">Search |</a>
					<a href="/fulltable">Full Table |</a>
					<a href="https://www.youtube.com/watch?v=Gc2u6AFImn8">About |</a>
					<a href="/contactus">Contact Us </a>
				</h2>
			</div>
		</div>
		<table>
			%s
		</table>
	</body>
</html>
'''
	
	
htmltemp = '''<!DOCTYPE html>
<html lang="en">
	<head>
		<title>%s</title>
		<meta charset="utf-8" />
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
		<div id="header">
			<div id="logo">
				<h1>Assignment#3</h1>
			</div>
			<div id="menu">
				<h2>
					<a href="./">Search |</a>
					<a href="/fulltable">Full Table |</a>
					<a href="https://www.youtube.com/watch?v=Gc2u6AFImn8">About |</a>
					<a href="/contactus">Contact Us </a>
				</h2>
			</div>
		</div>
		<div id="content">
			<form action="/year" method="GET">
				<p>Type a year between 1997-2015</p>
				<input type="text" name="year1" /> <p> or select from below:</p> %s<br /><br />
				<input type="radio" name="edu" value="priedu" />Primary Education<br /><br />
				<input type="radio" name="edu" value="secedu" />Secondary Education<br /><br />
				<input type="radio" name="edu" value="both" checked/>Both<br /><br />
				<input type="submit" name="submit" value="Search!">
			</form>
		</div>
	</body>
</html>
''' 
htmlcont = '''<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Contact Us</title>
		<meta charset="utf-8" />
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
	<div id="header">
			<div id="logo">
				<h1>Assignment#3</h1>
			</div>
			<div id="menu">
				<h2>
					<a href="./">Search |</a>
					<a href="/fulltable">Full Table |</a>
					<a href="https://www.youtube.com/watch?v=Gc2u6AFImn8">About |</a>
					<a href="/contactus">Contact Us </a>
				</h2>
			</div>
		</div>
		<div id="content">
			<form action="/contactus" method="POST">
				<p>Your Name:</p><input type="text" name="name" /><br />
				<input type="checkbox" name="gender" value="male" checked >Male
				<input type="checkbox" name="gender" value="female">Female<br />
				<p>Feedback:</p><br />
				<textarea name="feedback"></textarea><br />
				<input type="submit" name="submit" Value="Send!" />
			</form>
		</div>
	</body>
</html>
'''
def form():
	selector = "<select name='year2'>"
	for i in range(1997,2016):
		selector += '				<option value="'+str(i)+'">'+str(i)+'</option>\n'
	selector += '			</select>'
	return htmltemp % ("Search!", selector)

def asdasd():
	year1 = request.GET["year1"]
	year2 = request.GET["year2"]
	edu = request.GET['edu']
	if year1 != "":
		if edu == "priedu":
			return pe(year1)
		elif edu == "secedu":
			return se(year1)
		elif edu == "both":
			return full_table(year1)
	elif year1 == "":
		if edu == "priedu":
			return pe(year2)
		elif edu == "secedu":
			return se(year2)
		elif edu == "both":
			return full_table(year2)
	elif year1 != "" and year1 != year2:
		if edu == "priedu":
			return pe(year1)
		elif edu == "secedu":
			return se(year1)
		elif edu == "both":
			return full_table(year1)
	
def css(path):	
	return static_file(path, root="./")
	
route("/", "GET", form)
route('/<path>', 'GET', css)
route("/year", "GET", asdasd)
route('/fulltable', "GET", fulltable)
route("/contactus", "GET", contactus)
route("/contactus", "POST", feedback)
#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

