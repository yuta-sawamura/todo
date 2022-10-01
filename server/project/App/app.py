from flask import Flask
from App.database import init_db, db
from App.models import Task


def create_app():
    app = Flask(__name__)
    app.config.from_object('App.config.Config')

    init_db(app)

    @app.route('/show')
    def show_tasks():
        all_peter = Task.query.filter_by(content='peter').all()
        how_many_peter = len(all_peter)
        return '今Peterは{}人います'.format(how_many_peter)

    @app.route('/add')
    def add_task():
        peter = Task(content='peter')
        db.session.add(peter)
        db.session.commit()
        return 'Peterを増やしました。'

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
