# Exercise 23
# From the given file name:

# filename = 'view.jpg'

# extract extension and print it to the console.

# Expected result:

# jpg

filename = 'view.jpg'


import pathlib

print(pathlib.Path('yourPath.example').suffix) # '.example'
print(pathlib.Path("hello/foo.bar.tar.gz").suffixes) # ['.bar', '.tar', '.gz']
print(pathlib.Path('/foo/bar.txt').stem) # 'bar