from dfply import make_symbolic, pipe, symbolic_evaluation
import pandas as pd

@make_symbolic
def to_datetime(series, infer_datetime_format=True):
    return pd.to_datetime(series, infer_datetime_format=infer_datetime_format)


@pipe
@symbolic_evaluation(eval_as_selector=[1])
def set_index(df, col, drop = True):
    return df.set_index(col, drop = drop)


@pipe
@symbolic_evaluation
def row_index_slice(df, *args):
    assert len(args) in (1,2), "loc requires 1-2 arguments"
    if len(args) == 1:
        return df.loc[args[0]]
    else:
        return df.loc[args[0]:args[1]]
