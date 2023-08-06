```python
pip install a-pandas-ex-df-updater
```

```python
#    Update a DataFrame/Series with the values of another.
    from a_pandas_ex_df_updater import pd_add_df_updater
    pd_add_df_updater()

    df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                       columns=['a', 'b', 'c'])
    df2 = pd.DataFrame(np.array([[11, 2, 3], [4, 55, 6], [7, 8, 9], [17, 2, 93]]),
                       columns=['a', 'x', 'y'])


    df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=False,add_new_rows=False)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a  b  c
    0  11  2  3
    1   4  5  6
    2   7  8  9




    df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=False)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a  b  c   x  y
    0  11  2  3   2  3
    1   4  5  6  55  6
    2   7  8  9   8  9




    df3=df1.ds_update(forupdate=df2,update_existing_values=True, add_new_columns=True,add_new_rows=True)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a    b    c   x   y
    0  11  2.0  3.0   2   3
    1   4  5.0  6.0  55   6
    2   7  8.0  9.0   8   9
    3  17  NaN  NaN   2  93




    df1.ds_update(forupdate=df2,update_existing_values=False, add_new_columns=True,add_new_rows=True)

    df1
       a  b  c
    0  1  2  3
    1  4  5  6
    2  7  8  9
    df2
        a   x   y
    0  11   2   3
    1   4  55   6
    2   7   8   9
    3  17   2  93
    df3
        a    b    c   x   y
    0   1  2.0  3.0   2   3
    1   4  5.0  6.0  55   6
    2   7  8.0  9.0   8   9
    3  17  NaN  NaN   2  93

        Parameters:
            df: Union[pd.Series, pd.DataFrame]
            forupdate: Union[pd.Series, pd.DataFrame]
            update_existing_values:bool
                (default=True)
            add_new_columns=True
                (default=True)
            add_new_rows=True
                (default=True)

        Returns:
            Union[pd.Series, pd.DataFrame]
```
