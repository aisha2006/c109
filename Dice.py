import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

#Calculating sum of dice
diceresult=[]
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1+dice2)

#calculating mean
mean = sum(diceresult)/len(diceresult)

#calculating standard deviation
standardDeviation = st.stdev(diceresult)

median = st.median(diceresult)
mode = st.mode(diceresult)

# print(median,mode)

fig = ff.create_distplot(
    [diceresult],["result"], show_hist=False
)
# fig.show()

#finding 1 stdDev start & end values, & 2 stdDev start and end values
first_sd_start, first_sd_end = mean-standardDeviation, mean+standardDeviation
second_sd_start, second_sd_end = mean-(2*standardDeviation), mean+(2*standardDeviation)
third_sd_start, third_sd_end = mean-(3*standardDeviation), mean+(3*standardDeviation)

#Lists on data in the range
list_of_data_within_1_sd = [result for result in diceresult if result > first_sd_start and  result < first_sd_end]
list_of_data_within_2_sd = [result for result in diceresult if result > second_sd_start and result <second_sd_end ]
list_of_data_within_3_sd = [result for result in diceresult if result > third_sd_start and result <third_sd_end]

print("Mean is {}".format(mean))
print("{}% of data within first standard deviation" .format(len(list_of_data_within_1_sd)*100/ len(diceresult)))

print("{}% of data within second standard deviation".format(len(list_of_data_within_2_sd)*100/ len(diceresult)))

print("{}% of data within third standard deviation" .format(len(list_of_data_within_3_sd)*100/ len(diceresult)))
