from flask import Flask, render_template, request,json
import time
# Import the ADXL345 module.
import Adafruit_ADXL345

app = Flask(__name__)


# Create an ADXL345 instance.
accel = Adafruit_ADXL345.ADXL345()
position = 'foward'


@app.route('/')
def root():
    return render_template('intro.html')

@app.route('/maze1')
def maze1():
    return render_template('maze1.html')

@app.route('/maze2')
def maze2():
    return render_template('maze2.html')

@app.route('/ball')
def ball():
    return render_template('ball.html')

@app.route('/json')
def index():
    x, y, z = accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))

    if x > 0 and y < 0:
        position = "Right"
    elif x > 0 and y > 0:
        position = "Foward"
    elif x < 0 and y > 0:
        position = "Left"
    elif x < 0 and y < 0:
        position = "Back"
    else:
        position = "No direction"
            
    data = {"position": position}
    return position   


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


