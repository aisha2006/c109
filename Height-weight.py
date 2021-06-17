import csv
import pandas as pd
import statistics as st

df = pd.read_csv("height-weight.csv")
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

#Mean for height and weight
mean_height = st.mean(height_list)
mean_weight = st.mean(weight_list)

#Median
median_height = st.median(height_list)
median_weight = st.median(weight_list)
#Mode
mode_height = st.mode(height_list)
mode_weight = st.mode(weight_list)



#print ( mean_height, median_height, mode_height)
#print ( mean_weight, median_weight, mode_weight)

sd_height = st.stdev(height_list)
sd_weight = st.stdev(weight_list)

#1, 2 & 3 standard deviations for height
height_1_sd_start, height_1_sd_end = mean_height-sd_height, mean_height +sd_height
height_2_sd_start, height_2_sd_end = mean_height-(2*sd_height), mean_height +(2*sd_height)
height_3_sd_start, height_3_sd_end = mean_height-(3*sd_height), mean_height +(3*sd_height)

#1, 2 & 3 standard deviations for weight
weight_1_sd_start, weight_1_sd_end = mean_weight-sd_weight, mean_weight +sd_weight
weight_2_sd_start, weight_2_sd_end = mean_weight-(2*sd_weight), mean_weight +(2*sd_weight)
weight_3_sd_start, weight_3_sd_end = mean_weight-(3*sd_weight), mean_weight +(3*sd_weight)


list_for_1height = [result for result in height_list if result > height_1_sd_start and result < height_1_sd_end]

list_for_2height = [result for result in height_list if result > height_2_sd_start and result < height_2_sd_end]

list_for_3height = [result for result in height_list if result > height_3_sd_start and result < height_3_sd_end]

list_for_1weight = [result for result in weight_list if result > weight_1_sd_start and result < weight_1_sd_end]

list_for_2weight = [result for result in weight_list if result > weight_2_sd_start and result < weight_2_sd_end]

list_for_3weight = [result for result in weight_list if result > weight_3_sd_start and result < weight_3_sd_end]

print("{}% of data for height within 1 sd " .format(len(list_for_1height)*100/len(height_list)))
print("{}% of data for height within 2 sd " .format(len(list_for_2height)*100/len(height_list)))
print("{}% of data for height within 3 sd " .format(len(list_for_3height)*100/len(height_list)))
print("{}% of data for weight within 1 sd " .format(len(list_for_1weight)*100/len(weight_list)))
print("{}% of data for weight within 2 sd " .format(len(list_for_2weight)*100/len(weight_list)))
print("{}% of data for weight within 3 sd " .format(len(list_for_3weight)*100/len(weight_list)))
