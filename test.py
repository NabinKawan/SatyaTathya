data = '''POST / HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.29.2
Accept: */*
Postman-Token: fd3d86e8-9ac6-4c0c-9b49-6678f2bbd571
Host: localhost:7888
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 11

{"hi":'hi'}'''

content_length_index = data.find('Content-Length')+len('Content-Length')

content_length= int(data[content_length_index+2:content_length_index+2+2])

print(data[-content_length:])
