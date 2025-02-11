
import pandas as pd
data = pd.read_csv(r'/home/xfazze/moin/netflix_analysis/NetflixViewingHistory.csv')
titles = pd.DataFrame(data, columns=['Title'])
titles = titles.values.tolist()
dates = pd.DataFrame(data, columns=['Date'])
dates = dates.values.tolist()
nice_data = [titles, dates]

# gör om listorna till en lista med dictionaries
data = []
for i in range(len(nice_data[0])):
    data.append({"titles" : titles[i][0], "dates" : dates[i][0]})

# tar bort nan
new_data = []
for i in data:
    if isinstance(i["titles"], str):
        new_data.append(i)

# gör 2 listor på  filmer och serier
series = []
movies = []
for i in new_data:
    times = 0
    for o in new_data:
        if i["titles"][0:10] == o["titles"][0:10]:
            times += 1
    if times != 1:
        series.append(i)
    else:
        movies.append(i)

# clmuping togheter
unique_title =[1]
unique_series = []
for i in series:
    same = True
    for o in series:
        if o["titles"][0:10] == i["titles"][0:10]:
            for p in unique_title:
                if i["titles"][0:10] == p:
                    same = False
    if same:
        unique_title.append(i["titles"][0:10])
        unique_series.append(i["titles"])
        same = False

print("here")
data = series
series = []
for o in unique_title:
    for i in data:
        if i["titles"][0:10] == o:
            series.append(i)
print("Series:")
for i in unique_series:
    print(i)
print("\n\nMovies\n")
for i in movies:
    print(i["titles"])
print("längde, series", len(unique_series))       
print("längde, moveis", len(movies))
