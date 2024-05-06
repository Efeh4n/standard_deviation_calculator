#                   Standard Deviation calculator
# enter data
data = []
def std_calc(data):
    #calculating mean of data 
    mean_data = sum(data)/len(data)
    data_minus_mean_sqr = []
    # lets calculate differences of data from the mean 
    for i in data:
        data_minus_mean_sqr.append((i-mean_data)**2)
    # calculate sum of squared difference
    sum_data_minus_mean_sqr = sum(data_minus_mean_sqr)
    numerator = sum_data_minus_mean_sqr
    denominator = len(data)
    return (numerator/denominator)**(0.5)
print("standard deviation :",std_calc(data))