from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import time

app = Flask(__name__)

# Initial variables
amount = 500.00
pin = 1234
wrong_pin_count = 0
cash_out = False

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/action', methods=['GET', 'POST'])
def action():
    global amount, pin, wrong_pin_count, cash_out

    if request.method == 'POST':
        choice = int(request.form['choice'])

        if choice == 1:  
            return redirect(url_for('transfer.html'))
        elif choice == 2:  
            flash("MomoPay & Pay Bills functionality not implemented yet.")
            return redirect(url_for('pay-bills'))
        elif choice == 3:  
            flash("Airtime & Bundles functionality not implemented yet.")
            return redirect(url_for('airtime.html'))
        elif choice == 4:  
            cash_out = request.form.get('cash_out') == '1'
            flash("Cash Out status updated." if cash_out else "Cash Out not allowed.")
            return redirect(url_for('menu'))
        elif choice == 5:  
            flash("Financial Services functionality not implemented yet.")
            return redirect(url_for('menu'))
        elif choice == 6:  
            return redirect(url_for('my_wallet'))

    return render_template('action.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    global amount, wrong_pin_count, pin

    if request.method == 'POST':
        reciever_number = request.form['reciever_number']
        transfer_amount = float(request.form['transfer_amount'])
        entered_pin = int(request.form['pin'])

        if len(reciever_number) != 10 or not reciever_number.isdigit():
            flash("Invalid receiver number. Try again.")
            return redirect(url_for('transfer'))
        
        if transfer_amount > amount:
            flash("Insufficient funds. Your transfer was incomplete.")
            return redirect(url_for('transfer'))

        if entered_pin != pin:
            wrong_pin_count += 1
            if wrong_pin_count >= 5:
                flash("Your account has been locked.")
                return redirect(url_for('menu'))
            flash("Incorrect PIN. Try again.")
            return redirect(url_for('transfer'))

        amount -= transfer_amount
        flash(f"Transaction successful. GHS {transfer_amount} has been transferred to {reciever_number}.")
        return redirect(url_for('menu'))

    return render_template('transfer.html')


@app.route('/change_pin', methods=['GET', 'POST'])
def change_pin():
    global pin

    if request.method == 'POST':
        current_pin = int(request.form['current_pin'])
        if current_pin == pin:
            new_pin = int(request.form['new_pin'])
            confirm_pin = int(request.form['confirm_pin'])
            if new_pin == confirm_pin:
                pin = new_pin
                flash("PIN changed successfully.")
                return redirect(url_for('my_wallet'))
            else:
                flash("PINs do not match. Try again.")
        else:
            flash("Incorrect current PIN. Try again.")
    
    return render_template('change_pin.html')

@app.route('/airtime', methods=['GET', 'POST'])
def airtime():
    return render_template('airtime.html')


@app.route('/pay-bills', methods=['GET', 'POST'])
def pay_bills():
    return render_template('pay-bills.html')
    

@app.route('/financial-services', methods=['GET', 'POST'])
def financial_services():
    return render_template('financial-services.html')


@app.route('/cashout', methods=['GET', 'POST'])
def cashout():
    return render_template('cashout.html')


@app.route('/my-wallet', methods=['GET', 'POST'])
def my_wallet():
    return render_template('my-wallet.html')



if __name__ == '__main__':
    app.run(debug=True)
