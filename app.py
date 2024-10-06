from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

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

        if choice == 1:  # Transfer Money
            return redirect(url_for('transfer'))
        elif choice == 2:  # MomoPay & Pay Bills
            flash("MomoPay & Pay Bills functionality not implemented yet.")
            return redirect(url_for('menu'))
        elif choice == 3:  # Airtime & Bundles
            flash("Airtime & Bundles functionality not implemented yet.")
            return redirect(url_for('menu'))
        elif choice == 4:  # Allow Cash Out
            cash_out = request.form.get('cash_out') == '1'
            flash("Cash Out status updated." if cash_out else "Cash Out not allowed.")
            return redirect(url_for('menu'))
        elif choice == 5:  # Financial Service
            flash("Financial Services functionality not implemented yet.")
            return redirect(url_for('menu'))
        elif choice == 6:  # My Wallet
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

@app.route('/my_wallet', methods=['GET', 'POST'])
def my_wallet():
    global amount, pin

    if request.method == 'POST':
        choice = int(request.form['wallet_choice'])

        if choice == 1:  # Check Balance
            flash(f"Your current balance is: GHS {amount:.2f}")
            return redirect(url_for('my_wallet'))
        elif choice == 2:  # Change & Reset PIN
            return redirect(url_for('change_pin'))

    return render_template('my_wallet.html')

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

if __name__ == '__main__':
    app.run(debug=True)
