### Tired of vectorization, df.apply and df.map? How about an old school inplace-for-loop? :)

#### Usage - DataFrame

```python
pip install 
```

```python
    from a_pandas_ex_old_school_for_loop import pd_add_old_school_for_loop
    pd_add_old_school_for_loop()
    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

    df
    Out[3]:
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    0              1         0       3  ...   7.2500   NaN         S
    1              2         1       1  ...  71.2833   C85         C
    2              3         1       3  ...   7.9250   NaN         S
    3              4         1       1  ...  53.1000  C123         S
    4              5         0       3  ...   8.0500   NaN         S
    ..           ...       ...     ...  ...      ...   ...       ...
    886          887         0       2  ...  13.0000   NaN         S
    887          888         1       1  ...  30.0000   B42         S
    888          889         0       3  ...  23.4500   NaN         S
    889          890         1       1  ...  30.0000  C148         C
    890          891         0       3  ...   7.7500   NaN         Q
    [891 rows x 12 columns]


    for item in df.ds_set_values_with_loop():
        try:
            if item['get_value']() > 2:
                item['set_value'](10000000)
        except Exception:
            continue


    df
    Out[5]:
         PassengerId  Survived    Pclass  ...        Fare Cabin  Embarked
    0              1         0  10000000  ...  10000000.0   NaN         S
    1              2         1         1  ...  10000000.0   C85         C
    2       10000000         1  10000000  ...  10000000.0   NaN         S
    3       10000000         1         1  ...  10000000.0  C123         S
    4       10000000         0  10000000  ...  10000000.0   NaN         S
    ..           ...       ...       ...  ...         ...   ...       ...
    886     10000000         0         2  ...  10000000.0   NaN         S
    887     10000000         1         1  ...  10000000.0   B42         S
    888     10000000         0  10000000  ...  10000000.0   NaN         S
    889     10000000         1         1  ...  10000000.0  C148         C
    890     10000000         0  10000000  ...  10000000.0   NaN         Q
    [891 rows x 12 columns]
```

#### Usage - Series in a DataFrame

```python
    from a_pandas_ex_old_school_for_loop import pd_add_old_school_for_loop
    pd_add_old_school_for_loop()
    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")

    df
    Out[3]:
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    0              1         0       3  ...   7.2500   NaN         S
    1              2         1       1  ...  71.2833   C85         C
    2              3         1       3  ...   7.9250   NaN         S
    3              4         1       1  ...  53.1000  C123         S
    4              5         0       3  ...   8.0500   NaN         S
    ..           ...       ...     ...  ...      ...   ...       ...
    886          887         0       2  ...  13.0000   NaN         S
    887          888         1       1  ...  30.0000   B42         S
    888          889         0       3  ...  23.4500   NaN         S
    889          890         1       1  ...  30.0000  C148         C
    890          891         0       3  ...   7.7500   NaN         Q
    [891 rows x 12 columns]


    for item in df.PassengerId.ds_set_values_with_loop():
        try:
            if item['get_value']() > 2:
                item['set_value'](10000000)
        except Exception:
            continue

    df
    Out[3]:
         PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
    0              1         0       3  ...   7.2500   NaN         S
    1              2         1       1  ...  71.2833   C85         C
    2       10000000         1       3  ...   7.9250   NaN         S
    3       10000000         1       1  ...  53.1000  C123         S
    4       10000000         0       3  ...   8.0500   NaN         S
    ..           ...       ...     ...  ...      ...   ...       ...
    886     10000000         0       2  ...  13.0000   NaN         S
    887     10000000         1       1  ...  30.0000   B42         S
    888     10000000         0       3  ...  23.4500   NaN         S
    889     10000000         1       1  ...  30.0000  C148         C
    890     10000000         0       3  ...   7.7500   NaN         Q
    [891 rows x 12 columns]
```

#### Update lists and dicts inside cells

```python
from a_pandas_ex_old_school_for_loop import pd_add_old_school_for_loop
from random import randrange
pd_add_old_school_for_loop()
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
getrandomlist = lambda x: [
    [[randrange(1, 100), randrange(1, 100)] * 1] * randrange(1, 10)
]
df["listtest"] = df.PassengerId.map(getrandomlist)
df
Out[4]: 
     PassengerId  ...                                           listtest
0              1  ...         [[[88, 15], [88, 15], [88, 15], [88, 15]]]
1              2  ...  [[[15, 63], [15, 63], [15, 63], [15, 63], [15,...
2              3  ...             [[[46, 9], [46, 9], [46, 9], [46, 9]]]
3              4  ...         [[[71, 12], [71, 12], [71, 12], [71, 12]]]
4              5  ...  [[[55, 44], [55, 44], [55, 44], [55, 44], [55,...
..           ...  ...                                                ...
886          887  ...  [[[81, 15], [81, 15], [81, 15], [81, 15], [81,...
887          888  ...                                       [[[18, 70]]]
888          889  ...                                       [[[16, 35]]]
889          890  ...  [[[48, 54], [48, 54], [48, 54], [48, 54], [48,...
890          891  ...  [[[11, 99], [11, 99], [11, 99], [11, 99], [11,...   


for item in df.listtest.ds_set_values_with_loop():
    try:
        if item['get_value']() > 15:
            item['set_value'](15000000)
    except Exception:
        continue     


df
Out[6]: 
     PassengerId  ...                                           listtest
0              1  ...  [[[15000000, 15], [15000000, 15], [15000000, 1...
1              2  ...  [[[15, 15000000], [15, 15000000], [15, 1500000...
2              3  ...  [[[15000000, 9], [15000000, 9], [15000000, 9],...
3              4  ...  [[[15000000, 12], [15000000, 12], [15000000, 1...
4              5  ...  [[[15000000, 15000000], [15000000, 15000000], ...
..           ...  ...                                                ...
886          887  ...  [[[15000000, 15], [15000000, 15], [15000000, 1...
887          888  ...                           [[[15000000, 15000000]]]
888          889  ...                           [[[15000000, 15000000]]]
889          890  ...  [[[15000000, 15000000], [15000000, 15000000], ...
890          891  ...  [[[11, 15000000], [11, 15000000], [11, 1500000...
[891 rows x 13 columns]
```
