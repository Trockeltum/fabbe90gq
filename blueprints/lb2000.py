
from flask import *
from config import *
from threading import Thread
from bson import json_util
import time
import os
from random import randint

from lb.api_calls import *
from lb.match_history import *
from lb.championIdtoname import *
from forms.lb2000_form import *
from lb.runes import *
from lb.analysis import *
from lb.popular import *
from lb.regions import *
from lb.newSaveMatch import *
from lb.ranks import *
from lb.recentData import *
from lb.summoner import *
from lb.mastery import *

from blueprints.lb2000bps.progress import progress
from blueprints.lb2000bps.wr import wr
from blueprints.lb2000bps.match import match
from blueprints.lb2000bps.recentData import recentData
from blueprints.lb2000bps.ranks import ranks
from blueprints.lb2000bps.multiAcc import multiAcc
from blueprints.lb2000bps.mastery import mastery
from blueprints.lb2000bps.liveGame import liveGame

lb2000 = Blueprint('lb2000', __name__)
lb2000.register_blueprint(progress, url_prefix='/progress')
lb2000.register_blueprint(wr, url_prefix='/wr')
lb2000.register_blueprint(match, url_prefix='/match')
lb2000.register_blueprint(recentData, url_prefix='/recentData')
lb2000.register_blueprint(ranks, url_prefix='/ranks')
lb2000.register_blueprint(multiAcc, url_prefix='/multiAcc')
lb2000.register_blueprint(mastery, url_prefix='/mastery')
lb2000.register_blueprint(liveGame, url_prefix='/liveGame')


# TODO player Tags
# champs player wr for champs/length
# TODO timeframes in analysis

# TODO Live game viewing

# TODO Lp graph search every night

# TODO summoner top champ background


# TODO rank distribution
# TODO average rank of champion
# TODO users top %

# TODO user not found page

# TODO calendar of matches

# TODO search bar examples

@lb2000.route("/", methods=['GET', 'POST'])
@lb2000.route("/<region>/<summonername>", methods=['GET', 'POST'])
def lb2000_index(region='noregion', summonername='nouser'):
    if request.method == 'POST':
        username = request.form.get('userName')
        region = regionConverter3[request.form.get('region')]
        return redirect('/lb2000/' + region + '/' + username)

    popular = getPopular(region)

    res = render_template('lb2000/lb2000_search.html',
                          error=False, popular=popular)
    if summonername != 'nouser' or region != 'noregion' or region == 'multiAcc':
        res = returnprofile(summonername, region, popular)
    if not res:
        res = render_template('lb2000/lb2000_search.html', error=True)
    return res


def returnprofile(summonername, region, popular):
    print('region', region)
    region_large = regionConverter1[region]
    summoner = get_summoner(region, summonername, riot_api_key)
    if not summoner:
        return False
    else:
        Thread(target=updateSummoner, args=(summoner, region)).start()
        Thread(target=updateMasterySummoner, args=(
            summoner['id'], region, summoner['puuid'], riot_api_key)).start()
        addPopular(summonername, region)
        Thread(target=getMatches, args=(
            summoner['puuid'], region_large, region, riot_api_key)).start()
        Thread(target=get_recentData, args=(summoner['puuid'],)).start()
        Thread(target=getRankedPlayers, args=(
            region, summoner['id'], riot_api_key)).start()
        multiAccId, multiAccUrl = multiAccGet(summoner['id'])

        # match_history =  get_match_history(region_large, summoner['puuid'], riot_api_key, 0, 9)
        # Thread(target=download_matches, args=(match_history, region, riot_api_key, runeIdToName)).start()
        # Thread(target=get_details, args=(summoner['puuid'], region_large, riot_api_key)).start()
        timenow = time.time()

        print('profile success')
        return render_template('lb2000/lb2000_base.html', summoner=summoner, region=region, region_large=region_large, niceRegion=regionConverter4[region], champ_id_to_name=champ_id_to_name, timenow=timenow,
                               summonerid=str(summoner['id']),   popular=popular, multiAccUrl=multiAccUrl)


def multiAccGet(puuid):
    multiAccId = randint(1, 27)
    multiAccUrl = f'https://raw.communitydragon.org/latest/game/assets/ux/summonericons/profileicon{ multiAccId }.png'
    client = MongoClient('localhost', 27017)
    coll = client.lb2000.multiAcc
    coll.replace_one({'puuid': puuid}, {
        'puuid': puuid, 'pfpId': multiAccId}, upsert=True)
    return multiAccId, multiAccUrl


'''
@lb2000.route("/riot.txt", methods=['GET', 'POST'])
def riot():
    filename = 'static/riot.txt'
    return send_file(filename, mimetype='txt')
'''
