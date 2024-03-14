# Assignment-1 
#Data Wrangling
import numpy as np
import pandas as pd


data_frame=pd.read_csv("G:\sheetal\Iris.csv")
print(data_frame)
'''
      Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
0      1            5.1           3.5            1.4           0.2     Iris-setosa
1      2            4.9           3.0            1.4           0.2     Iris-setosa
2      3            4.7           3.2            NaN           0.2     Iris-setosa
3      4            4.6           3.1            1.5           0.2     Iris-setosa
4      5            5.0           3.6            1.4           0.2     Iris-setosa
..   ...            ...           ...            ...           ...             ...
145  146            6.7           3.0            5.2           2.3  Iris-virginica
146  147            6.3           2.5            5.0           1.9  Iris-virginica
147  148            6.5           3.0            5.2           2.0  Iris-virginica
148  149            6.2           3.4            5.4           2.3  Iris-virginica
149  150            5.9           3.0            5.1           1.8  Iris-virginica

[150 rows x 6 columns]
'''

print(data_frame.head())
'''
Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0   1            5.1           3.5            1.4           0.2  Iris-setosa
1   2            4.9           3.0            1.4           0.2  Iris-setosa
2   3            4.7           3.2            NaN           0.2  Iris-setosa
3   4            4.6           3.1            1.5           0.2  Iris-setosa
4   5            5.0           3.6            1.4           0.2  Iris-setosa
'''

print(data_frame.tail())

'''
Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
145  146            6.7           3.0            5.2           2.3  Iris-virginica
146  147            6.3           2.5            5.0           1.9  Iris-virginica
147  148            6.5           3.0            5.2           2.0  Iris-virginica
148  149            6.2           3.4            5.4           2.3  Iris-virginica
149  150            5.9           3.0            5.1           1.8  Iris-virginica
'''
print(data_frame.describe())

'''
         Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
count  150.000000     150.000000    150.000000     149.000000    150.000000
mean    75.500000       5.843333      3.054000       3.775168      1.198667
std     43.445368       0.828066      0.433594       1.758720      0.763161
min      1.000000       4.300000      2.000000       1.000000      0.100000
25%     38.250000       5.100000      2.800000       1.600000      0.300000
50%     75.500000       5.800000      3.000000       4.400000      1.300000
75%    112.750000       6.400000      3.300000       5.100000      1.800000
max    150.000000       7.900000      4.400000       6.900000      2.500000
'''
print(data_frame.info())

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Id             150 non-null    int64
 1   SepalLengthCm  150 non-null    float64
 2   SepalWidthCm   150 non-null    float64
 3   PetalLengthCm  149 non-null    float64
 4   PetalWidthCm   150 non-null    float64
 5   Species        150 non-null    object
dtypes: float64(4), int64(1), object(1)
'''
print(data_frame.shape)

'''
(150, 6)
'''
print(data_frame.isnull().any().any())
'''
True
'''
print(data_frame.isnull().sum())

'''
Id               0
SepalLengthCm    0
SepalWidthCm     0
PetalLengthCm    1
PetalWidthCm     0
Species          0
'''
avg_val=data_frame["PetalLengthCm"].astype("float").mean()
print(avg_val)
'''
3.7751677852348995
'''
data_frame["PetalLengthCm"].replace(np.NaN,avg_val, inplace=True)
print(data_frame["PetalLength"])
'''
0      1.400000
1      1.400000
2      3.775168
3      1.500000
4      1.400000
         ...
145    5.200000
146    5.000000
147    5.200000
148    5.400000
149    5.100000
'''

print(data_frame.dtypes)

'''
Name: PetalLengthCm, Length: 150, dtype: float64
Id                 int64
SepalLengthCm    float64
SepalWidthCm     float64
PetalLengthCm    float64
PetalWidthCm     float64
Species           object
dtype: object
'''


data_frame["Species"]=data_frame["Species"].replace({"Iris-setosa":1, "Iris-versicolor":2,"Iris-virginica":3})
print(data_frame["Species"])

'''
Species           object
dtype: object
0      1
1      1
2      1
3      1
4      1
      ..
145    3
146    3
147    3
148    3
149    3
'''
