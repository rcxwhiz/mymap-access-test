import pickle
import os
import sys
from pathlib import Path
from classroom import semester_getter

pickles_path = os.path.join(os.path.dirname(sys.argv[0]), 'pickles')
if not os.path.exists(pickles_path):
	os.makedirs(pickles_path)
os.chdir(pickles_path)

test_semester = semester_getter.get('Fall 2019')
print('it worked')

pickle.dump(test_semester, open('test semester', 'wb'))

print('I was able to save the semester file!')
