from flask import Flask, render_template
from utils import *
json_file = 'candidates.json'

app = Flask(__name__)


@app.route("/")
def list_candidates():
    candidates = get_alls(json_file)
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<pk>/")
def candidate_page(pk):
    candidate = get_by_pk(pk, get_alls(json_file))
    return render_template('card.html', candidate=candidate)


@app.route("/search/<name>/")
def name_candidate_page(name):
    candidates_list = get_by_name(name, get_alls(json_file))
    len_list = len(candidates_list)
    return render_template('search.html', candidates=candidates_list, len_list=len_list)


@app.route("/skill/<skill_name>/")
def skill_candidate_page(skill_name):
    candidates_list = get_by_skill(skill_name, get_alls(json_file))
    len_candidates = len(candidates_list)
    return render_template('skill.html', candidates=candidates_list, len_list=len_candidates, skill=skill_name)


app.run()
