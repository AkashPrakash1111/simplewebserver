# EX01 Developing a Simple Webserver

## Date:09-04-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
<!DOCTYPE html>
<html>
<head>
    <title>WEB APPLICATION</title>
</head>
<body>
    <table border="6" bgcolor="lightcyan">
        <caption><strong>TCP/IP MODEL LAYERS</strong></caption>
        <tr bgcolor="lightblue">
            <th>S.no</th>
            <th>Layer</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>1.</td>
            <td>Application</td>
            <td>Provides network services to applications</td>
        </tr>
        <tr>
            <td>2.</td>
            <td>Transport</td>
            <td>Provides reliable/unreliable delivery</td>
        </tr>
        <tr>
            <td>3.</td>
            <td>Internet</td>
            <td>Handles logical addressing and routing</td>
        </tr>
        <tr>
            <td>4.</td>
            <td>Network Access</td>
            <td>Manages physical addressing and access to the media</td>
        </tr>
    </table>
</body>
</html>

"""
class myhandler (BaseHTTPRequestHandler):
     def do_GET(self):
        print("request received") 
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-04-09 161727.png>)
![alt text](<Screenshot 2025-04-09 161749.png>)
>>>>>>> 32ae910 (Success)

## RESULT:
The program for implementing simple webserver is executed successfully
