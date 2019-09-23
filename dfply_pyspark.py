from functoolz import pipeable
from functools import reduce

@pipeable
def select(cols, df):
    return df.select(*cols)
    
@pipeable
def mutate(df, **kwargs):
    add_next_withColumn = lambda df, tup: df.withColumn(tup[0], tup[1])
    return reduce(add_next_withColumn, kwargs.items(), df)  

@pipeable
def take(num, df):
    return df.take(num)


@pipeable
def collect(df):
    return df.collect()

@pipeable
def filter_by(cond, df):
    return df.where(cond)
