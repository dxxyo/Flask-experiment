from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, User
from . import db

views = Blueprint("views", __name__)


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        text = request.form.get('text')
        if not text:
            flash("Text harus diisi!", category="error")
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Pesan berhasil dikirim !")
            return redirect(url_for('views.home'))
        
    return render_template("create_post.html", user=current_user)


@views.route("/")
@views.route("/home")
@login_required
def home():
    return render_template("home.html", user=current_user)




