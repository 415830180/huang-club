from flask import Blueprint,render_template,make_response,redirect,url_for,request
import uuid

views = Blueprint("views",__name__)


#
#
# @views.route('/sign', methods=['GET', 'POST'])
# def sign():
#     return render_template("./bbs/sign.html")


@views.route('/', methods=['GET', 'POST'])
def index():
    return render_template("zhanshiye.html")


@views.route('/sign', methods=['GET', 'POST'])
def sign():
    return render_template("sign.html")

@views.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")





@views.route('/signout', methods=['GET', 'POST'])
def signout():
    # 删除cookie
    response = make_response(redirect(url_for("views.sign")))
    response.delete_cookie("token")
    response.set_cookie("token","", 3600)
    # response.delete_all_cookies()
    return response


@views.route('/trouble', methods=['GET', 'POST'])
def trouble():
    return render_template("trouble.html")


@views.route('/about/me', methods=['GET', 'POST'])
def about_me():
    return render_template("about_me.html")


@views.route('/edit', methods=['GET', 'POST'])
def edit():
    return render_template("edit_tool.html")


@views.route('/bbs', methods=['GET', 'POST'])
def post():
    return render_template("post.html")


@views.route('/tools', methods=['GET', 'POST'])
def tools():
    id = str(uuid.uuid4())[0:8]
    response = make_response(render_template("caj2pdf.html"))
    response.set_cookie("id", id, 3600)
    return response


@views.route('/cloud', methods=['GET', 'POST'])
def cloud():
    response = make_response(render_template("cloud.html"))
    response.set_cookie("more_file",'10', 3600)
    return response



@views.route('/content/<name>', methods=['GET', 'POST'])
def content(name):
    response = make_response(render_template("/post_content.html"))
    response.set_cookie("file_name",name, 3600)
    return response



@views.route("/search",methods = ['get'])
def response_search():

    search_value = str(request.values.get("s"))
    response = make_response(render_template("search.html"))
    response.set_cookie("search_value", search_value, 3600)
    return response



#----------------------------------------------------------------



@views.route("/file/<name>",methods = ["get","POST"])
def get_file_inf(name):
    file_name = name
    response = make_response(render_template("file.html"))
    response.set_cookie("file_name", file_name, 3600)
    return response




@views.route("/up_file",methods = ["get","POST"])
def up_file():
    id = str(uuid.uuid4())[0:8]
    response = make_response(render_template("up_file.html"))
    response.set_cookie("id",id, 3600)
    return response

