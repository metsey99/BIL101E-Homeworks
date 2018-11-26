#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

def sum():
	total = 0
	for i in range(2,21):
		total += int(contents[i][5])
	return "Total number of primary school classroom between 2005-2016 is "+str(total)
	
		

def mean(col,school):
	totalnum = 0
	count = 0
	for x in range(2, 21):
		contents[x][col] = float(contents[x][col])
		totalnum += contents[x][1]
		count += 1
	return "The mean of net schooling ratio of "+str(contents[0][school])+": "+str(round(float(totalnum)/count, 2))
	
	
def countif(coln, val):
	countt = 0
	for a in range(2,21):
		if contents[a][coln] >= val:
			countt += 1
	return "Number of values greater or equal to "+str(val)+" is "+str(countt)+ " in # "+str(coln)+" column."
	
listforps = [
("Cell at index 3,5: "+str(contents[3][5])),
("Cell at index 7,10: "+str(contents[7][10])),
("Cell at index 6,15: "+str(contents[6][15])), 
("Cell at index 12,11: "+contents[12][11]),
mean(1, 0),
sum(), countif(1, 95), mean(11,11)]


html = '''
<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="utf-8" />
			<title>Turkey's Education History</title>
			<style>
				table{
					border-collapse: collapse;
					}
				td {
					border: 1px black solid;
				}
				
			</style>
		</head>
		<body>
			%s
			<table>
				%s
			</table>
			%s
		</body>
	</html>
'''
def td(cell):
	return "				<td>"+str(cell)+"</td>"

data = ""
indexes = ""
for rows in range(0, 21):
	for cols in range(0, 20):
		if cols == 0:
			data += ("			<tr>")
		data += td(contents[rows][cols])
		if cols == 19:
			data += ("			</tr>")
for n in range(0, len(listforps)):
	indexes += "<p>"+str(listforps[n])+"</p>"
explanation = '''
	<p>My dataset is about changes in Turkish Primary and Secondary Educations. I included changes in number of schools, number of teachers, number of students, number of classrooms, etc. between 1997-2016. </p>
	<p>When we look at the primary education we see that net schooling ratio has increased because people started to realize that education is very important for children. As students increase number of schools and number of teachers also increased till 2011. If we compare 1997-1998 to 2015-2016 educational years, we see that number of students per division is decreased because, more schools are build and number of students per teacher is also decreased, because people who like to teach started becoming teachers. </p>
	<p>If we look at the secondary education, we can say similar thing like in primary education. Schooling ratio increased so fast. The importance of education made government to build more schools and made teaching job as an attractive job. More schools were build and more teachers demanded to fill those schools. Teachers are selected from the exam called KPSS. Nowadays, it is not hard to be a teacher but it is hard to work as a teacher. </p>
	'''

print(html %(indexes, data, explanation))


