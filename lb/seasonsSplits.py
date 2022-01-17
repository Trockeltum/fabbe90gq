import datetime
from pprint import pprint

def createSeasons():
    s = {'1': {'0': datetime.datetime(2010, 7, 13)},
         '2': {'0':  datetime.datetime(2011, 11, 29)},
         '3': {'0':  datetime.datetime(2013, 2, 1)},
         '4': {'0':  datetime.datetime(2014, 1, 10)},
         '5': {'0':  datetime.datetime(2015, 1, 21)},
         '6': {'0':  datetime.datetime(2016, 1, 20)},
         '7': {'0':  datetime.datetime(2016, 12, 13)},
         '8': {'0':  datetime.datetime(2018, 1, 16)},
         '9': {'0':  datetime.datetime(2019, 1, 23)},
         '10': {'0':  datetime.datetime(2020, 1, 10)},
         '11': {'0':  datetime.datetime(2021, 1, 8)},
         '12': {'0':  datetime.datetime(2022, 1, 7)}
         }

    for season in s.keys():
        for split in range(1, 4):
            s[season][str(split)] = s[season][str(split-1)] + \
                datetime.timedelta(days=104)

    # pprint.pprint(s)

    for season in s.keys():
        for split in range(4):
            s[season][str(split)] = (s[season][str(split)] -
                                     datetime.datetime(1970, 1, 1)).total_seconds()

    # pprint.pprint(s)
    return s

def timeToSeasonSplit(time):
      seasonsDates = {'1': {'0': 1278979200.0,
                      '1': 1287964800.0,
                      '2': 1296950400.0,
                      '3': 1305936000.0},
                '10': {'0': 1578614400.0,
                       '1': 1587600000.0,
                       '2': 1596585600.0,
                       '3': 1605571200.0},
                '11': {'0': 1610064000.0,
                       '1': 1619049600.0,
                       '2': 1628035200.0,
                       '3': 1637020800.0},
                '12': {'0': 1641513600.0,
                       '1': 1650499200.0,
                       '2': 1659484800.0,
                       '3': 1668470400.0},
                '2': {'0': 1322524800.0,
                      '1': 1331510400.0,
                      '2': 1340496000.0,
                      '3': 1349481600.0},
                '3': {'0': 1359676800.0,
                      '1': 1368662400.0,
                      '2': 1377648000.0,
                      '3': 1386633600.0},
                '4': {'0': 1389312000.0,
                      '1': 1398297600.0,
                      '2': 1407283200.0,
                      '3': 1416268800.0},
                '5': {'0': 1421798400.0,
                      '1': 1430784000.0,
                      '2': 1439769600.0,
                      '3': 1448755200.0},
                '6': {'0': 1453248000.0,
                      '1': 1462233600.0,
                      '2': 1471219200.0,
                      '3': 1480204800.0},
                '7': {'0': 1481587200.0,
                      '1': 1490572800.0,
                      '2': 1499558400.0,
                      '3': 1508544000.0},
                '8': {'0': 1516060800.0,
                      '1': 1525046400.0,
                      '2': 1534032000.0,
                      '3': 1543017600.0},
                '9': {'0': 1548201600.0,
                      '1': 1557187200.0,
                      '2': 1566172800.0,
                      '3': 1575158400.0}}
      lastSeasonSplit = {
            'season' : 9,
            'split' : 0
      }
      for season in range(8, 14):
            lastSeasonSplit['season'] = season
            for split in range(4):
                  if seasonsDates[str(season)][str(split)] > time:
                        return lastSeasonSplit
                  lastSeasonSplit['split'] = split

seasonsDates = {'1': {'0': 1278979200.0,
                      '1': 1287964800.0,
                      '2': 1296950400.0,
                      '3': 1305936000.0},
                '10': {'0': 1578614400.0,
                       '1': 1587600000.0,
                       '2': 1596585600.0,
                       '3': 1605571200.0},
                '11': {'0': 1610064000.0,
                       '1': 1619049600.0,
                       '2': 1628035200.0,
                       '3': 1637020800.0},
                '12': {'0': 1641513600.0,
                       '1': 1650499200.0,
                       '2': 1659484800.0,
                       '3': 1668470400.0},
                '2': {'0': 1322524800.0,
                      '1': 1331510400.0,
                      '2': 1340496000.0,
                      '3': 1349481600.0},
                '3': {'0': 1359676800.0,
                      '1': 1368662400.0,
                      '2': 1377648000.0,
                      '3': 1386633600.0},
                '4': {'0': 1389312000.0,
                      '1': 1398297600.0,
                      '2': 1407283200.0,
                      '3': 1416268800.0},
                '5': {'0': 1421798400.0,
                      '1': 1430784000.0,
                      '2': 1439769600.0,
                      '3': 1448755200.0},
                '6': {'0': 1453248000.0,
                      '1': 1462233600.0,
                      '2': 1471219200.0,
                      '3': 1480204800.0},
                '7': {'0': 1481587200.0,
                      '1': 1490572800.0,
                      '2': 1499558400.0,
                      '3': 1508544000.0},
                '8': {'0': 1516060800.0,
                      '1': 1525046400.0,
                      '2': 1534032000.0,
                      '3': 1543017600.0},
                '9': {'0': 1548201600.0,
                      '1': 1557187200.0,
                      '2': 1566172800.0,
                      '3': 1575158400.0}}

if __name__ == '__main__':
    #pprint(createSeasons())
    print(timeToSeasonSplit(1651363199 ))


