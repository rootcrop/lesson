import matplotlib.pyplot as plt
import mpld3
import numpy as np
import pandas as pd
import requests as rqst
from PIL import Image, ImageDraw

# requests  выводим логин и аватар пользователей гитхаба    # requests.readthedocs.io/en/latest/user/quickstart/
print('requests github: ')
r1 = rqst.get('https://api.github.com/events').json()       # get
for i in range(len(r1)):
    print (r1[i]['actor']['display_login'], r1[i]['actor']['avatar_url'])

output = {'country': 'ru', 'town': 'msk','street':['lenin','11']}
r_get = rqst.get('https://httpbin.org/get', params=output, timeout=5)          # делаем GET и POST запросы
r_post = rqst.post('https://httpbin.org/post', params=output, timeout=5)       #
print('get: ',r_get.json())   # {'args': {'country': 'ru', 'street': ['lenin', '11'], 'town': 'msk'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-66f9320e-2dff2ab65f3d753604d28b51'}, 'origin': '31.172.211.102', 'url': 'https://httpbin.org/get?country=ru&town=msk&street=lenin&street=11'}
print('post: ',r_post.text)


print('requests colormind: ')
# requests получаем случайные цвета              # requests.readthedocs.io/en/latest/
r = rqst.get('http://colormind.io/api/', data='{"model":"default"}')
if r.status_code != 200:
    print('error: ', r.status_code )
else: pass #print('Ok')
file_colors='modules11-colors.txt'
with open(file_colors, 'a', encoding='utf-8') as file:   # открываем файл для добавления контекстым менеджером
    file.write(str(r.json())+'\n')

'''filename='modules11_pip_install.jpg'
with Image.open(filename) as img:
    img.load(); print(img.size)
    img_rotate1=img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img_rotate1.save('new.jpg')     # print(isinstance(img_rotate1, Image.Image))   #img_rotate1.show() '''

f='modules11-colors-palette'
colors=r.json()['result']
count=len(colors)
im = Image.new('RGB', (count * 100, 100),(10, 10, 10))      # color="pink"  color=(10,10,255,127) color='#00004c'
draw = ImageDraw.Draw(im)
for i in range(count):
    c=colors[i]     # <class 'list'>    [107, 14, 19]
    c.append(255)   # add no transparency
    img_new1 = Image.new(mode="RGBA", size=(100, 100), color=tuple(c))
    img_new1.save(f'{f}-img-{i}.png')
    #               x1   y1   x2   y2
    draw.rectangle((100*i, 0, 100*i+100, 100), fill=tuple(c), outline=(0, 0, 0))
im.save(f'{f}-all.jpg', quality=99)
im.show()   #exit()

# pandas        # выводим страну и min/max/mean gdp                                     # from tabulate import tabulate # stackoverflow.com/questions/33181846/programmatically-convert-pandas-dataframe-to-markdown-table # print(tabulate(df, tablefmt="pipe", headers="keys"))
print ('\n pandas : ')
#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv', delimiter=',')
file_pd_data='modules11_gapminder_unfiltered.csv'; df = pd.read_csv(file_pd_data, delimiter=',').round(decimals=1)
d1=df.groupby( 'country', sort=True)['gdpPercap'].agg(['min','max','mean']).round(decimals=0)
print(d1.to_markdown())

# numpy         # из pandas.core.series.Series делаем numpy.ndarray
d2=(d1['mean'].values)
print(f'\n numpy : \n world GDP min:{d2.min().round(decimals=1)} max:{d2.max().round(decimals=1)} mean:{d2.mean().round(decimals=1)}       ')

# matplotlib / pandas             оставляем только максимальный gdpPercap
df_max_gdpPercap = df.sort_values(['country', 'gdpPercap'], ascending=[True, False]).drop_duplicates('country').round(decimals=1)
#print(df_max_gdpPercap.to_markdown())

# данные: country, lifeExp, pop, gdpPercap      # данные отсюда :  https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv
lifeExp=df_max_gdpPercap['lifeExp'].values.round(decimals=1).astype(float)
pop=df_max_gdpPercap['pop'].values.round(decimals=1).astype(float)
gdpPercap=df_max_gdpPercap['gdpPercap'].values.round(decimals=1).astype(float)
country=df_max_gdpPercap['country']     # pandas.core.series.Series
year=df_max_gdpPercap['year']     # pandas.core.series.Series
N=187       # получившееся количество в выборке, нужно для вывода графиков в matplotlib

# выводим в поп_ап подсказку страна/год/gdp
df_country_year = df_max_gdpPercap['country'].astype(str) +', '+ df_max_gdpPercap['year'].astype(str)+', gdpPerCap:'+ df_max_gdpPercap['gdpPercap'].astype(int).astype(str)

np.random.seed(19680801)        # seed the random number generator.
data = {'a': lifeExp,
        'c': np.random.randint(0, 1000, N, ),
        'd': gdpPercap}
data['b'] = gdpPercap                                  # Y: gdpPercap
data['d'] = np.abs(pop) * 0.00005                      # diametr  population

fig, ax = plt.subplots(figsize=(16, 8), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data, cmap=plt.cm.jet)
ax.grid(color='gray', linestyle='dashed')
ax.set_xlabel('X: продолжительность жизни (lifeExp)', size=10)   # a
ax.set_ylabel('Y: ВВП на душу населения (gdpPerCap)', size=10)   # b
ax.set_title("Исторические максимумы gdpPerCap, размер круга: кол-во населения", size=14)
plt.savefig('module11_libs_X-lefeExp__Y-gdpPercap__CircleSize-population.png')      #plt.show()

fig, ax = plt.subplots(subplot_kw=dict(facecolor='#EEEEEE'))
fig, ax = plt.subplots(figsize=(17, 8))
scatter = ax.scatter('a', 'b',
                     c=np.random.random(size=N),
                     s='d', data=data,
                     alpha=0.45, cmap=plt.cm.jet)

# Точечный график (с всплывающими подсказками!)     Scatter Plot (with tooltips!)  mpld3.github.io/examples/scatter_tooltip.html
ax.grid(color='gray', linestyle='dashed')
ax.set_xlabel('X: продолжительность жизни (lifeExp)', size=12)   # a
ax.set_ylabel('Y: ВВП на душу населения (gdpPerCap)', size=12)   # b
ax.set_title("Исторические максимумы gdpPerCap (1952-2007), размер круга: кол-во населения", size=14)

labels = ['{0}'.format(str(val)) for _, val in df_country_year.items()]
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig, tooltip)
mpld3.show()
