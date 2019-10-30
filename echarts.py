from pyecharts import Bar, EffectScatter, Line, Pie, WordCloud

# bar = Bar('我的第一个图标', '副标题')
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.show_config()
# bar.render('test01.html')

# 条形图
# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# bar = Bar("Bar chart", "precipitation and evaporation one year")
# bar.add("precipitation", attr, v1, mark_line=['average'], mark_point=['max', 'min'])
# bar.add("evaporation", attr, v2, mark_line=['average'], mark_point=['max', 'min'])
# bar.render('test02.html')
# attr：列表 ，名称 ，横向坐标方向
# v1 / v2：列表， 数据，纵坐标方向
# mark_point / mark_line：标记点、标记线。用于标记最大最小值，标记平均值的线，标记的形状、颜色 、大小，自定义标记的点等。标记线可以是任何两点连线
# 文中 mark_line=["average"]：标记平均值 ， mark_point=["max", "min"]：标记最大值、最小值
# render：渲染成文件
# 如果在A、B商家中的bar_add参数中添加is_stack：表示叠加效果，即商家A、商家B数据叠在一起展示
# 横向柱形图：is_convert=True，标识交换X轴和Y轴


# v1 = [10, 20, 30, 40, 50, 60]
# v2 = [25, 20, 15, 10, 60, 33]
# es = EffectScatter("动态散点图")
# es.add('effectScatter', v1, v2)
# es.render('test03.html')

# attr = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
# v1 = [5, 20, 36, 10, 10, 100]
# v2 = [55, 60, 16, 20, 15, 80]
# line = Line('折线图')
# line.add('商家A', attr, v1, mark_point=['average'])
# line.add('商家B', attr, v2, is_smooth=True, mark_line=['max', 'average'])
# line.show_config()
# line.render('test04.html')

# attr = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
# v1 = [11, 12, 13, 10, 10, 10]
# pie= Pie('饼图实例')
# pie.add("", attr, v1, is_label_show=True)
# pie.show_config()
# pie.render('test05.html')

name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
         550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100], shape='diamond')
wordcloud.show_config()
wordcloud.render('test06.html')

