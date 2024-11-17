from flask import Flask,render_template,jsonify, request,redirect,url_for,session
import prompt

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
message = 'hello'
history = {}



@app.route('/chat', methods=['GET'])
def chat():
    return render_template('chat.html', history=history)

@app.route('/chat/respond', methods=['POST'])
def respond():
    history = []
    user_message = request.json.get('message')
    bot_response = prompt.api_call_bot(user_message)  # Replace with real bot logic
    history.append({"user": user_message, "bot": bot_response})
    return jsonify({"user_message": user_message, "bot_response": bot_response})






@app.route('/mail', methods=['GET', 'POST'])
def gmail():
    # Define the dictionary with placeholder values
    user = {
        "Name": "",
        "ToAdd": "",
        "Mail": "",
        "Type": "",
        "Reciever":"",
    }

    if request.method == 'POST':
        # Get the form data
        user['Name'] = name = request.form.get('name')
        user['ToAdd'] = email = request.form.get('email')
        user['Mail'] =message = request.form.get('message')
        user['Type'] =option = request.form.get('options')
        user["Reciever"] =Reciever = request.form.get('toname')
        
        message  = prompt.api_call_mail(user=user)
        # Redirect to the same page with updated data in the URL
        return redirect(url_for('gmail', name=name,toname = Reciever , email=email, message=message, option=option))

    # Access the data from URL parameters
    name = request.args.get('name', user["Name"])
    email = request.args.get('email', user["ToAdd"])
    message = request.args.get('message', user["Mail"])
    option = request.args.get('option', user["Type"])
    Reciever = request.args.get('toname', user["Reciever"])

    # Update the dictionary with the new values
    user = {
        "Name": name,
        "ToAdd": email,
        "Mail": message,
        "Type": option,
        "Reciever":Reciever
    }

    return render_template('gmail.html', user=user)

if __name__ == '__main__':
    app.run(port=5001, debug=True)