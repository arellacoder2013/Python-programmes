import matplotlib.pyplot as plt

student_id = [1263,7245,8976,6321,2904,9288]
student_marks =[98,76,88,100,65,53]

plt.plot(student_id, color='red',marker='*')
plt.plot(student_marks, color='yellow',marker='o')

plt.xlabel('student_id',fontsize='16')
plt.ylabel('student_marks',fontsize='15')

plt.grid(True)
plt.show()