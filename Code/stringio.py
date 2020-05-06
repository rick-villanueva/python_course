import io

message = 'This is just a normal string'

f = io.StringIO(message)

f.read()

f.write(' Second line written to file like object')

f.seek(0)
f.read()
f.close()