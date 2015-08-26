import time
import BaseHTTPServer
from os import curdir, sep


HOST_NAME = '' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000 # Maybe set this to 9000.


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_POST(s):
        print "Posting"
        s.do_GET()

    def do_GET(s):
        """Respond to a GET request."""

        if s.path=="/":
            s.path="index.html"
        elif s.path=="/SampleRedir":
            s.path="SampleRedir.html"

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
                f = open(curdir + sep + s.path) 
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