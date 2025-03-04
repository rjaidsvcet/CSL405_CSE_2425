from flask import Flask, render_template

app = Flask (__name__)

@app.route ('/vcet', methods = ['GET'])
def genericFunction ():
    return 'Hello World'

@app.route ('/mcu', methods = ['GET'])
def welcomeFunction ():
    return '<h1>Hello Iron Man</h1>'

@app.route ('/', methods = ['GET'])
def genericPage ():
    return render_template ('index.html')

if __name__ == '__main__':
    app.run (debug=True)