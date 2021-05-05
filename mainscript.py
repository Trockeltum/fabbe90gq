import os
import json
import ast
import requests
import time
from flask import *
from flask_wtf import FlaskForm
from wtforms import Form, SelectField, validators, SubmitField, IntegerField
from wtforms.validators import DataRequired
from ratio_code.basic_copy import *
from forms.osu_form import *
from forms.pappa_form import *
from forms.factorio_form import *
from forms.lb2000_form import *
from ludvig_blabarsylt.api_calls import *
from ludvig_blabarsylt.championIdtoname import *

# Initializing flask and sql
app = Flask(__name__,  static_folder='static')
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route("/")
def index():
    return render_template('index.html')

# Bjornbanan


@app.route("/bjornbanan")
def bjornbanan():
    return render_template('bjornbanan/bjornbanan.html')


@app.route("/bjornbanan/help")
def bjornbanan_help():
    return render_template('bjornbanan/bjornbanan_help.html')


@app.route("/bjornbanan/music_help")
def bjornbanan_music_help():
    return render_template('bjornbanan/bjornbanan_m_help.html')

# projects files


@app.route("/projects/files")
def files():
    files = os.listdir("/home/pi/website/static/projects/")
    return render_template('files.html', files=files)


@app.route('/projects/files/<path:filename>')
def sendfile(filename):
    projects_path = app.static_folder + "/projects/"
    return send_from_directory(projects_path, filename)

# projects


@app.route("/projects/")
def projects():
    files = os.listdir("/home/pi/website/static/projects/")
    return render_template('projects.html', files=files)


@app.route("/projects/pappa", methods=['GET', 'POST'])
def pappa():
    return render_template('produktutveckling/pappa.html')

@app.route("/projects/pappa/login", methods=['GET', 'POST'])
def pappa_login():
    form = pappa_login_form()
    return render_template('produktutveckling/pappa_login.html', form=form)

@app.route("/projects/pappa/register", methods=['GET', 'POST'])
def pappa_register():
    form = pappa_register_form()
    if request.method == "POST":
        return redirect('/hejda')
    return render_template('produktutveckling/pappa_register.html', form=form)



@app.route("/games/osu", methods=['GET', 'POST'])
def osu():
    form = osuform()
    if form.validate_on_submit():
        print("suvbl")
        '''with open('/home/pi/website/static/leaderboards/osu.json', 'r+') as f:
            leaderboard = f.read()
            leaderboard = ast.literal_eval(leaderboard)
            for place in range(len(leaderboard)):
                if leaderboard[place]["value" ] < value
        return form.name.data'''
    with open('/home/pi/website/static/leaderboards/osu.json', 'r+') as f:
        leaderboard = f.read()
        leaderboard = ast.literal_eval(leaderboard)
    return render_template('games/osu.html', form=form, leaderboard=leaderboard)

# proportions calc
@app.route("/projects/factorio",  methods=['GET', 'POST'])
def prop_calc():
    form = factorioform()
    if form.validate_on_submit():
        component = form.component.data
        result = get_components(form.component.data, form.amount.data,
                                form.smeliting_mod.data, form.assembler_mod.data)
        print(result)
        ratio = str(result["ratio"])
        sop = stage(result, 1, [])
        print(result)
        return render_template('factorio_proportions.html', form=form, ratio=ratio, component=component, submitted=True,  sop=sop)
    return render_template('factorio_proportions.html', form=form, ratio="wee", component="component", submitted=False, sop="sop")


@app.route("/ludvig_blabarsylt_2000", methods=['GET', 'POST'])
def lb2000():
    api_key='RGAPI-8b2450d3-f27b-487f-a114-77839bfc1e90'
    form = lb2000_getuser()
    if form.validate_on_submit():
        username = form.username.data
        region = form.region.data
        large_region = form.large_region.data
        summoner = get_summoner(region, username, api_key)
        print(summoner['id'])
        if "status" in summoner.keys():
            return render_template('lb2000/lb2000_search.html', form=form, error=True)
        else:
            mastery = get_mastery(region, summoner['id'], api_key)
            total_mastery = get_total_mastery(region, summoner['id'], api_key)
            ranks = get_rank(region, summoner['id'], api_key)
            timenow = time.time()
            form = lb2000_getuser()
            return render_template('lb2000/lb2000_base.html', summoner=summoner, region=region, mastery=mastery, total_mastery=total_mastery, champ_id_to_name=champ_id_to_name, timenow=timenow,ranks=ranks,form=form)
    return render_template('lb2000/lb2000_search.html', form=form, error=False)



# Run the site
if __name__ == "__main__":
    app.run()
