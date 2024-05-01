from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []

for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() 
    results.append(result)

#Al tirar dos dados d8 tenemos una distribucion simetrica con nueve siendo la mediana

frequencies = []
for number in range(1, die_1.num_sides+die_2.num_sides+1):
    frequency = results.count(number)
    frequencies.append(frequency)

x_values = list(range(1, die_1.num_sides+die_2.num_sides+1))

data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {'title': 'Result', 'color':'red'}
y_axis_config = {'title': 'Frequency of result'}

my_layout = Layout(title = 'Results of rolling two d8 1000 times', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data':data, 'layout' : my_layout}, filename= 'd8_2.html')

