#!/usr/bin/env python3
"""Not importing anything. checker has the imports"""


def array(df):
    """Function grabs two columns and there last 10 rows
    then converts it into a numpy.ndarray"""

    # Grabbing named columns High, Close
    grab_col = df[["High", "Close"]]

    # in those columns this is grabbing the last ten rows
    grab_rowcol = grab_col.tail(n=10)

    # converts to numpy.ndarrary
    np_arrary = grab_rowcol.to_numpy()

    return np_arrary
