from flask import  render_template,flash,redirect,url_for,request, jsonify
from blog import app
from blog import db

from blog.forms import RegisterationForm,LoginForm
from models import User,Post,Map

posts=[
{
    'id':'1',
    'author':'Agasa cristy',
    'title':'some murder',
    'content':'hellloooosmakdmsklamclsmclsmd,smdsamdksamd'
}
,
{
     'id':'2',
    'author':'mmmmm',
    'title':'sdsdsdsdssds',
    'content':'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
}
]


@app.route("/")
def hello_world():
    print('kmkmkm')
    return render_template('home.html',posts=posts)

@app.route("/blog/<id>/")
def blog(id=id):
    blog1 = [num for num in posts if num['id']==id]

    return render_template('blog.html',blog=blog1,id=id)

@app.route("/map/")
def map( ):
     
    return render_template('map.html')

@app.route("/mapp/")
def map2( ):
    langs=Map.query.all()
    return render_template('map2.html',langs=langs)
 
@app.route("/register/",methods=['GET','POST'])
def register():
    form=RegisterationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('account created for {form.username.data}','success')
        return redirect(url_for('users'))
    return render_template('register.html',title='register',form=form)
@app.route("/login/")
def login():
    form=LoginForm()
    return render_template('login.html',title='login',form=form)


@app.route("/users/")
def users():
    users=User.query.all()
    return render_template('users.html',title='users',users=users)

@app.route("/save_lang/",methods=['GET','POST'])
def save_lang():
     if request.method == "POST":
         data = request.get_json()
        # print(data['lat'],data['lng'])
         if data:
             map=Map(l1=data['lat'],l2=data['lng'])
             db.session.add(map)
             db.session.commit()
             print (Map.query.all())


 
     results = {'processed': 'true'}
     return jsonify(results)



     
           
