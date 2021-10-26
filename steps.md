    1.  pip install virtualenv
    2.  virtualenv venv
    3.  source venv/bin/activate
    4.  pip3 install requirements.txt
    5.  ```py 
            from flask import Flask
            app = Flask(__name__)

            @app.route('/')
            def hello_world():
             return 'Hello World’

            if __name__ == '__main__':
                app.run()
        ```
    6. All the dependencies go in requirements.txt