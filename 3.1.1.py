# 3.1.1 AIM: Familiarize different vector operations in python
import numpy as np
vector = np.array([22,34,345,23,33])
vector1 = np.array([1,2,3,7,5])
print(f'''sum = {vector + vector1}
diff = {vector - vector1}
product = {vector * vector1}
dot = {vector.dot(vector1)}''')
