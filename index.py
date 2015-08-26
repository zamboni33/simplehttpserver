import time
import BaseHTTPServer


HOST_NAME = '' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        # s.send_response(200)
        # s.send_header("Content-type", "text/html")
        # s.end_headers()
        # mainPage = open("index.html", "rb")
        # content = mainPage.read()
        # s.wfile.write(content)
        # # s.wfile.write("<html><head><title>Title goes here.</title></head>")
        # # s.wfile.write("<body><p>This is a test.</p>")
        # # # If someone went to "http://something.somewhere.net/foo/bar/",
        # # # then s.path equals "/foo/bar/".
        # # s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        # # s.wfile.write("</body></html>")

        if s.path=="/":
            s.path="index.html"

        try:
            #Check the file extension required and
            #set the right mime type

            sendReply = False
            if s.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if s.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if s.path.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            if s.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if s.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(s.path) 
                s.send_response(200)
                s.send_header('Content-type',mimetype)
                s.end_headers()
                s.wfile.write(f.read())
                f.close()
            return

        except IOError:
            s.send_error(404,'File Not Found: %s' % s.path)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    server_class.allow_reuse_address = True
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)