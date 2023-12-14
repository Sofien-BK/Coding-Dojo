from flask_app import app
from flask import render_template , redirect , request , flash , session
from flask_app.models.user_model import User



# * ==================== LOGIN / REGISTER PAGE - VIEW ====================
@app.route("/user/new")
def index():
    return render_template('user_crud.html')

#* ==================== REGISTER - method - ACTION ====================
@app.route('/users/register', methods = ["POST"])
def user_register():
    if not User.validate(request.form):
        return redirect('/user/new')
    
    data = {**request.form,}
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect("/users")  

#* ==================== Content page display ====================
@app.route("/users")
def users():
    all_users = User.get_all()
    data = {"id": session["user_id"]}
    all_them = []
    for one_user in all_users:
        list = [
            one_user.first_name,
            one_user.last_name,
            one_user.email,
            one_user.created_at,
            one_user.updated_at,
            one_user.id
        ]
        all_them.append(list)
        print(all_them)
    return render_template("user_crud_t.html" , one_user=one_user , all_them=all_them , data=data)
# * ==================== edit user ====================

@app.route("/user/edit/<int:id>")
def edit(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/users")
    user = User.get_by_id({"id": id})
    if user:
        first_name = user.name
        last_name = user.descreption
        email = user.instructions
        
        id = user.id
    return render_template(
        "recipe_edit.html", first_name=first_name, last_name=last_name, email=email
    )

# * ==================== Delete user ====================
@app.route("/user/delete/<int:id>")
def delete(id):
    # ! Route Guard
    if "user_id" not in session:
        return redirect("/")
    User.delete({'id':id})
    return redirect("/users")



