import pandas as pd
import multiprocess as mp
from tqdm import tqdm
from typing import Callable, Any


def parmap(input: pd.Series, fn: Callable[[Any], Any]) -> pd.Series:
    """
    Apply a function to each element in a pandas Series using parallel processing.

    Args:
    input (pd.Series): The input series.
    fn (Callable[[Any], Any]): The function to apply to each element of the series.

    Returns:
    pd.Series: A pandas Series containing the results of applying fn to each element of the input series.
    """
    with mp.Pool() as pool:
        result_iterator = pool.imap(fn, input.tolist())
        output = list(tqdm(result_iterator, total=len(input)))
    return pd.Series(output, index=input.index)
