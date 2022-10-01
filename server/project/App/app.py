from flask import Flask, request, jsonify, abort, render_template
from App.database import init_db, db
from App.models import Task

PREFIX = "/api"


def create_app():
    app = Flask(__name__)
    app.config.from_object('App.config.Config')

    init_db(app)

    @app.route(PREFIX + '/task/<id>')
    def show(id):
        task = Task.query.filter_by(id=id).first()
        if not task:
            abort(404)
        return jsonify({
            'id': task.id,
            'content': task.content
        }), 200

    @app.route(PREFIX + '/task', methods=['POST'])
    def create():
        task = Task(content=request.form['content'])
        db.session.add(task)
        db.session.commit()
        return jsonify(), 201

    @app.route(PREFIX + '/task/<id>', methods=['DELETE'])
    def delete(id):
        task = Task.query.filter_by(id=id).first()
        if task is not None:
            db.session.delete(task)
            db.session.commit()
            return jsonify(), 200
        else:
            return abort(404)

    @app.route(PREFIX + '/task/file', methods=['POST'])
    def write():
        count = Task.query.count()
        f = open('task.txt', 'w', encoding='UTF-8')
        f.write('タスク数 ' + str(count))
        f.close()
        return jsonify(), 201

    @app.route(PREFIX + '/task/file')
    def read():
        try:
            data = ''
            f = open('task.txt', 'r', encoding='UTF-8')
            line = f.readline()
            while line:
                data += line
                line = f.readline()
            f.close
        except Exception:
            # 例外を握りつぶす
            return jsonify()
        else:
            return jsonify({'content': data}), 200

    @app.route('/for')
    def get_for():
        return render_template('index.html')

    return app


app = create_app()
