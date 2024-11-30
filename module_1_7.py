# школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)
q =sum(grades[0])/len(grades[0])
w =sum (grades[1])/len(grades[1])
e =sum(grades[2])/len(grades[2])
r= sum(grades[3])/len(grades[3])
t= sum(grades[4])/len(grades[4])

students = {students[0]: q, students[1]: w, students[2]: e, students[3]: r, students[4]:t }
print(students)