"""Functions to concatenate string columns in a dataframe
"""


def concat_cols(df, col_list):
    """concatenate columns in a dataframe

    Args:
        df: dataframe
        col_list: list of columns in df to concat

    Returns:
        dataframe with concatenated columns
    """
    concat = df[col_list[0]]
    for i in range(1, len(col_list)):
        concat = concat + " " + df[col_list[i]]
        return concat


def concat_rows(df, groupby_col, concat_col):
    """concatenate rows in a dataframe

    Args:
        df: dataframe
        groupby_col: column to groupby
        concat_col: column with rows to concatenate

    Returns:
        array with concatenated values
    """
    row_concat = (
        df.groupby([groupby_col])[concat_col].apply(lambda x: " ".join(x)).reset_index()
    )
    return row_concat
