from flask import Flask, render_template, request
website = Flask(__name__)

def is_low(value):
    membership_value = 0
    if value <= 3:
        membership_value = 1
    elif value <= 10: #if it doesn't meet this condition, it is greater than 10
        membership_value = (10 - value)/(10 - 3)
    return membership_value

def is_medium(value):
    membership_value = 0
    if value >=4 and value <= 16:
        if value < 11:
            membership_value = (value - 4)/(11 - 4)
        else:
            membership_value = (16 - value)/(16 - 11)
    return membership_value

def is_high(value):
    membership_value = 0
    if value >= 12:
        if value >= 17:
            membership_value = 1
        else:
            membership_value = (17 - value)/(17 - 12)
    return membership_value

def membership_function(value):
    return {
        'low': is_low(value),
        'medium': is_medium(value),
        'high': is_high(value)
    }

@website.route('/<page_name>', methods=['GET', 'POST'])
def index(page_name):
    values_of_interest = {}
    givens = {
        'A1': 0,
        'A2': 0,
        'A3': 0
    }
    if request.method == 'POST':
        for value in ['A1', 'A2', 'A3']:
            values_of_interest[value] = membership_function(int(request.form[value]))
            givens[value] = request.form[value]
    return render_template('main.html', page_name=page_name, values_of_interest=values_of_interest,
                           givens=givens, ip=request.remote_addr)

if __name__=='__main__':
    website.run(debug=True);

