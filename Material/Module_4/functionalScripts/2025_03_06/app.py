from flask import Flask, render_template, request

app = Flask (__name__)

@app.route ('/')
def basic ():
    return render_template ('index.html')

@app.route ('/postHandling', methods = ['POST'])
def postHandling ():
    if request.method == 'POST':
        username = request.form ['username']
        password = request.form ['password']
        print (password, username)
        return '<h1>Post Method Sucessful</h1>'
    return render_template ('index.html')

# @app.route ('/getHandling', methods = ['GET'])
# def getHandling ():
#     if request.method == 'GET':
#         username = request.args ['username']
#         password = request.args ['password']
#         print (username, password)
#         return '<h1>Hello</h1>'
#     else:
#         return render_template ('index.html')

if __name__ == '__main__':
    app.run (debug=True)