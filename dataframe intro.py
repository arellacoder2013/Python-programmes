import pandas as pd
import numpy as np

exam_data = {'name': ['Ella','Matthew','Catherine','Alicia','Tom','Ben','Isabelle','Elijah','Michael','Krystal'],
             'score':[12.5,9,16.5, np.nan,9,20,14.5,np.nan,8,19],
             'attempts':[1,3,2,3,2,3,1,1,2,1],
             'qualify':['yes' ,'no','yes','no','no','yes','yes','no','no','yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']
examdf = pd.DataFrame(exam_data,index=labels)
print("Summary of the basic information about this dataFrame and its data: ")
print(examdf.info())
print(examdf)
