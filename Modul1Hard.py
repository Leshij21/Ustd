grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}

a = (sum(grades[0])/len(grades[0]))
b = (sum(grades[1])/len(grades[1]))
c = (sum(grades[2])/len(grades[2]))
d = (sum(grades[3])/len(grades[3]))
e = (sum(grades[4])/len(grades[4]))


St=sorted(students)
jornal = {St[0]:a}
jornal.update({St[1]:b})
jornal.update({St[2]:c})
jornal.update({St[3]:d})
jornal.update({St[4]:e})

print(jornal)
