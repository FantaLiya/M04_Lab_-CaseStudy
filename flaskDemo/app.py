from flask import Flask

app=Flask(_name_)

@app.route('/')
def index():
    return "Hello world"

    if _name_=="_main_":
        app.run(debug=True)