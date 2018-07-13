import my_first_flask_web
from flask import Flask

#def home():
  #  print("This is home")

if __name__ == '__main__':
    my_first_flask_web.app.run(debug=True, host='0.0.0.0')
