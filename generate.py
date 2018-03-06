import random
def Grade():
  for count in range (1,11):
    grade = random.randint(59,101)
    if 60 >= grade:
      print "grade:", grade , "; Your grade is D"
    elif 70 >= grade:
      print "grade:", grade , "; Your grade is C"
    elif 80 >= grade:
      print "grade", grade , "; Your grade is B"
    elif 90 >= grade: 
      print "grade", grade , "; Your grade is A"		

Grade()