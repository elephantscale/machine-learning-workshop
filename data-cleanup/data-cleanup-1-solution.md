# Dealing with unclean data

We're going to look at data that may require some cleansing.


```python
import numpy as np
import pandas as pd
import os
```

## Read the admissions data that is not so clean


```python
data_location = "../data/college-admissions/admission-data-dirty.csv"
if not os.path.exists (data_location):
    data_location = 'https://elephantscale-public.s3.amazonaws.com/data/college-admissions/admission-data-dirty.csv'
print('data_location:', data_location)
    
admissions = pd.read_csv(data_location)

print ("admissions shape : ", admissions.shape)
admissions
```

    data_location: ../data/college-admissions/admission-data-dirty.csv
    admissions shape :  (20, 4)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>400.0</td>
      <td>3.23</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>700.0</td>
      <td>3.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>800.0</td>
      <td>4.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.53</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>560.0</td>
      <td>3.78</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>NaN</td>
      <td>3.35</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>520.0</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>440.0</td>
      <td>3.17</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>760.0</td>
      <td>3.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>600.0</td>
      <td>2.82</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>500.0</td>
      <td>3.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.95</td>
      <td>4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>680.0</td>
      <td>3.27</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>560.0</td>
      <td>3.59</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.65</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>520.0</td>
      <td>2.98</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.0</td>
      <td>620.0</td>
      <td>4.00</td>
      <td>x</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>640.0</td>
      <td>3.51</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>600.0</td>
      <td>3.58</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Get Summary
See what we get.  It will skip null values


```python
admissions.describe(include = 'all')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>18.000000</td>
      <td>19.000000</td>
      <td>19.000000</td>
      <td>19</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.500000</td>
      <td>594.736842</td>
      <td>3.499474</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.514496</td>
      <td>109.309368</td>
      <td>0.353467</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>400.000000</td>
      <td>2.820000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>510.000000</td>
      <td>3.250000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.500000</td>
      <td>600.000000</td>
      <td>3.560000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.000000</td>
      <td>690.000000</td>
      <td>3.715000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.000000</td>
      <td>800.000000</td>
      <td>4.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
## TODO : Describe more than one column : gre and gpa
## Hint : add 'gpa' column
admissions[['gre', 'gpa']].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gre</th>
      <th>gpa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>19.000000</td>
      <td>19.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>594.736842</td>
      <td>3.499474</td>
    </tr>
    <tr>
      <th>std</th>
      <td>109.309368</td>
      <td>0.353467</td>
    </tr>
    <tr>
      <th>min</th>
      <td>400.000000</td>
      <td>2.820000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>510.000000</td>
      <td>3.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>600.000000</td>
      <td>3.560000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>690.000000</td>
      <td>3.715000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>800.000000</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>



## Drop all null values


```python
print("raw data shape : ", admissions.shape)
dropped_na = admissions.dropna()
print()
print("after drop shape : ", dropped_na.shape)
dropped_na

```

    raw data shape :  (20, 4)
    
    after drop shape :  (16, 4)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>400.0</td>
      <td>3.23</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>700.0</td>
      <td>3.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>800.0</td>
      <td>4.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.53</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>560.0</td>
      <td>3.78</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>440.0</td>
      <td>3.17</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>760.0</td>
      <td>3.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>500.0</td>
      <td>3.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.95</td>
      <td>4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>560.0</td>
      <td>3.59</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.65</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>520.0</td>
      <td>2.98</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.0</td>
      <td>620.0</td>
      <td>4.00</td>
      <td>x</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>640.0</td>
      <td>3.51</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>600.0</td>
      <td>3.58</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# only drop nulls from admit & gre column
print("raw data shape : ", admissions.shape)

print()

dropped2 = admissions.dropna(subset=['admit', 'gre'])
print("after drop shape : ", dropped2.shape)
dropped2
```

    raw data shape :  (20, 4)
    
    after drop shape :  (17, 4)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>400.0</td>
      <td>3.23</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>700.0</td>
      <td>3.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>800.0</td>
      <td>4.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.53</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>560.0</td>
      <td>3.78</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>520.0</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>440.0</td>
      <td>3.17</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>760.0</td>
      <td>3.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>500.0</td>
      <td>3.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.95</td>
      <td>4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>560.0</td>
      <td>3.59</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.65</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>520.0</td>
      <td>2.98</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.0</td>
      <td>620.0</td>
      <td>4.00</td>
      <td>x</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>640.0</td>
      <td>3.51</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>600.0</td>
      <td>3.58</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Fill in the values


```python
# fill every thing with zero
zero_fill = admissions.fillna(0)
zero_fill
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>400.0</td>
      <td>3.23</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>700.0</td>
      <td>3.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>800.0</td>
      <td>4.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.53</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>560.0</td>
      <td>3.78</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>520.0</td>
      <td>0.00</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>440.0</td>
      <td>3.17</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>760.0</td>
      <td>3.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.0</td>
      <td>600.0</td>
      <td>2.82</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>500.0</td>
      <td>3.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.95</td>
      <td>4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.0</td>
      <td>680.0</td>
      <td>3.27</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>560.0</td>
      <td>3.59</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.65</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>520.0</td>
      <td>2.98</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.0</td>
      <td>620.0</td>
      <td>4.00</td>
      <td>x</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>640.0</td>
      <td>3.51</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>600.0</td>
      <td>3.58</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# or we can specify per column default value
## TODO : specify different default values per column
##        default value for gre = -100
fill2 = admissions.fillna({'admit': -1, 'gre':-100 , 'gpa':-1, 'rank':10})
fill2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>400.0</td>
      <td>3.23</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>700.0</td>
      <td>3.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>800.0</td>
      <td>4.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.53</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>560.0</td>
      <td>3.78</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>-100.0</td>
      <td>3.35</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>520.0</td>
      <td>-1.00</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>440.0</td>
      <td>3.17</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>760.0</td>
      <td>3.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.0</td>
      <td>600.0</td>
      <td>2.82</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>500.0</td>
      <td>3.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.95</td>
      <td>4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>-1.0</td>
      <td>680.0</td>
      <td>3.27</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>560.0</td>
      <td>3.59</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.65</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>520.0</td>
      <td>2.98</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.0</td>
      <td>620.0</td>
      <td>4.00</td>
      <td>x</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>640.0</td>
      <td>3.51</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>600.0</td>
      <td>3.58</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Replace values


```python
print (admissions)

admissions2 = admissions.copy(deep=True)
admissions2['gre'].replace(800, 1000, inplace=True)

print()
print (admissions2)
```

        admit    gre   gpa rank
    0     1.0  400.0  3.23    4
    1     1.0  700.0  3.56    1
    2     1.0  800.0  4.00    2
    3     0.0  500.0  3.53    4
    4     0.0  560.0  3.78    2
    5     0.0    NaN  3.35  NaN
    6     1.0  520.0   NaN    3
    7     0.0  440.0  3.17    2
    8     1.0  760.0  3.00    2
    9     NaN  600.0  2.82    4
    10    1.0  500.0  3.60    3
    11    0.0  500.0  3.95    4
    12    NaN  680.0  3.27    2
    13    1.0  560.0  3.59    2
    14    0.0  700.0  3.65    2
    15    0.0  520.0  2.98    2
    16    0.0  700.0  3.92    2
    17    1.0  620.0  4.00    x
    18    0.0  640.0  3.51    2
    19    1.0  600.0  3.58    1
    
        admit     gre   gpa rank
    0     1.0   400.0  3.23    4
    1     1.0   700.0  3.56    1
    2     1.0  1000.0  4.00    2
    3     0.0   500.0  3.53    4
    4     0.0   560.0  3.78    2
    5     0.0     NaN  3.35  NaN
    6     1.0   520.0   NaN    3
    7     0.0   440.0  3.17    2
    8     1.0   760.0  3.00    2
    9     NaN   600.0  2.82    4
    10    1.0   500.0  3.60    3
    11    0.0   500.0  3.95    4
    12    NaN   680.0  3.27    2
    13    1.0   560.0  3.59    2
    14    0.0   700.0  3.65    2
    15    0.0   520.0  2.98    2
    16    0.0   700.0  3.92    2
    17    1.0   620.0  4.00    x
    18    0.0   640.0  3.51    2
    19    1.0   600.0  3.58    1


## Clean out RANK column


```python

admissions3 = admissions[admissions['rank'].isin(['1','2','3','4'])]
admissions3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>admit</th>
      <th>gre</th>
      <th>gpa</th>
      <th>rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>400.0</td>
      <td>3.23</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>700.0</td>
      <td>3.56</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>800.0</td>
      <td>4.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.53</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>560.0</td>
      <td>3.78</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>520.0</td>
      <td>NaN</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>440.0</td>
      <td>3.17</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>760.0</td>
      <td>3.00</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>600.0</td>
      <td>2.82</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.0</td>
      <td>500.0</td>
      <td>3.60</td>
      <td>3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>500.0</td>
      <td>3.95</td>
      <td>4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>NaN</td>
      <td>680.0</td>
      <td>3.27</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.0</td>
      <td>560.0</td>
      <td>3.59</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.65</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.0</td>
      <td>520.0</td>
      <td>2.98</td>
      <td>2</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.0</td>
      <td>700.0</td>
      <td>3.92</td>
      <td>2</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.0</td>
      <td>640.0</td>
      <td>3.51</td>
      <td>2</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.0</td>
      <td>600.0</td>
      <td>3.58</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
