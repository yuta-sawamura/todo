from flask import Flask, request, jsonify, abort
from App.database import init_db, db
from App.models import Task


def create_app():
    app = Flask(__name__)
    app.config.from_object('App.config.Config')

    init_db(app)

    @app.route('/task/<id>')
    def show(id):
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort(404)
        return jsonify({
            'id': task.id,
            'content': task.content
        }), 200

    @app.route('/task', methods=['POST'])
    def create():
        task = Task(content=request.form['content'])
        db.session.add(task)
        db.session.commit()
        return jsonify(), 201

    @app.route('/delete')
    def delete_task():
        peter = Task.query.filter_by(content='peter').first()
        if peter is not None:
            db.session.delete(peter)
            db.session.commit()
            return 'Peterを減らしました。'
        else:
            return 'Peterはひとりもいません'

    return app


app = create_app()
