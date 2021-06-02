
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()



with open_file('sample.txt', 'w') as f:
    f.write("adams sample text ye ya")


print(f.closed)

            
