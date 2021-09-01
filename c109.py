import statistics
import csv
import pandas as pd

df=pd.read_csv("c109data.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(height_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(height_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(height_list)

print("mean,median,mode of height list".format(height_mean,height_median,height_mode))
print("mean,median,mode of weight list".format(weight_mean,weight_median,weight_mode))

height_stanDeviation=statistics.stdev(height_list)
weight_stanDeviation=statistics.stdev(weight_list)

# 1,2 ,3 standard deviations for the height

height_first_stanDeviation_start,height_first_stanDeviation_end = height_mean- height_stanDeviation,height_mean+height_stanDeviation

height_second_stanDeviation_start,height_second_stanDeviation_end = height_mean-(2* height_stanDeviation),height_mean+(2* height_stanDeviation)

height_third_stanDeviation_start,height_third_stanDeviation_end = height_mean- (3*height_stanDeviation),height_mean- (3*height_stanDeviation)

# 1,2 ,3 standard deviations for the weight

weight_first_stanDeviation_start,weight_first_stanDeviation_end = height_mean- weight_stanDeviation,height_mean+ weight_stanDeviation,

weight_second_stanDeviation_start,weight_second_stanDeviation_end = height_mean- (2*weight_stanDeviation),height_mean+ weight_stanDeviation

weight_third_stanDeviation_start,weight_third_stanDeviation_end = height_mean-(3* weight_stanDeviation),height_mean+ weight_stanDeviation

height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_stanDeviation_start and result < height_first_stanDeviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_stanDeviation_start and result < height_second_stanDeviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_stanDeviation_start and result < height_third_stanDeviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_stanDeviation_start and result < height_first_stanDeviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_stanDeviation_start and result < height_second_stanDeviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_stanDeviation_start and result < height_third_stanDeviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviations".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviations".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(height_list)))
print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviations".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviations".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(weight_list)))

