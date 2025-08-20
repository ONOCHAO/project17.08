from flask import Flask, request, render_template, redirect
from core import Action


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("vhod.html")  

@app.route('/add-client', methods=['POST'])
def add_client_route():
    name = request.form['name']
    status = request.form['status']
    check = int(request.form['check'])

    add_client(name=name, check=check, status=status)

    return redirect('/')

@app.route('/add-note')
def add_note():
    return render_template('add_note.html')

@app.route('/delete-client')
def remove_client():
    return render_template('delete_client.html')

@app.route('/delete-note')
def remove_note():
      return render_template('delete_note.html')

@app.route('/add-note', methods=['GET', 'POST'])
def add_note_route():
    if request.method == 'POST':
        title = request.form['title']
        descrip = request.form['descrip']
        data = request.form['data']
        id_client = request.form['id_client']
        Action.add_note(title, descrip, data, id_client)
        return redirect('/')
    return render_template('add_note.html')


@app.route('/delete-client', methods=['GET', 'POST'])
def delete_client_route():
    if request.method == 'POST':
        client_id = request.form.get('id_client')
        if not client_id:
            error = "Укажите ID клиента"
            return render_template('delete_client.html', error=error)

        success = Action.delete_client(client_id)
        if success:
            return redirect('/')
        else:
            error = "Клиент не найден"
            return render_template('delete_client.html', error=error)

    return render_template('delete_client.html')



@app.route('/delete-note', methods=['GET', 'POST'])
def delete_note_route():
    if request.method == 'POST':
        note_id = request.form.get('note_id')
        if not note_id:
            return render_template('delete_note.html', error="Укажите ID заметки")
        Action.delete_note(note_id)
        return redirect('/')
    return render_template('delete_note.html')




if __name__ == '__main__':
    app.run(debug=True, port=5001)
