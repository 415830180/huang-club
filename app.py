from flask import Flask
from views.views import views
from routes.c_post import connection_bbs
from routes.c_user import connection_user
from routes.c_cloud import connection_cloud
from routes.caj2pdf.c_caj2pdf import connection_caj
from routes.c_service import connection_service



app = Flask(__name__)




app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

app.register_blueprint(views)
app.register_blueprint(connection_bbs)
app.register_blueprint(connection_user)
app.register_blueprint(connection_cloud)
app.register_blueprint(connection_caj)
app.register_blueprint(connection_service)


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=5008, debug='True')

