from http.server import HTTPServer, BaseHTTPRequestHandler 
content="""
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