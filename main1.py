#import from our website module
from website import create_app

#create instance and setup Flask
app = create_app()

#executes if script runs directly
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
