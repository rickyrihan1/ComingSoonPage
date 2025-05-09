from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def save_email(email):
    conn = sqlite3.connect('emails.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO subscribers (email) VALUES (?)", (email,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Duplicate email, ignore
    finally:
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def coming_soon():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            save_email(email)
        return redirect('/')  # Prevent form resubmission
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
