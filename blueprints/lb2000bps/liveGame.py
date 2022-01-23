from flask import *
from config import *
from threading import Thread
from bson import json_util
import time
import os
from random import randint
from pymongo import MongoClient, DESCENDING

from lb.api_calls import *
liveGame = Blueprint('liveGame', __name__)


@liveGame.route("/", methods=['GET', 'POST'])
def getLiveGame():
    puuid = request.args.get('puuid', 0, type=str)
    client = MongoClient('localhost', 27017)
    coll = client.lb2000.mastery
    mastery = list(coll.find({'puuid': puuid},
                   sort=[('time', DESCENDING)]))[0]
    return json.loads(json_util.dumps(mastery))
