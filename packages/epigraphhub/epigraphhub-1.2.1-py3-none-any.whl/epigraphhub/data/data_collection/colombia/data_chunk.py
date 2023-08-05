"""
Created on Mon Jan 31 08:53:59 2022
@author: eduardoaraujo

Last change on 2022/09/22
This module is responsible for slicing data found in Colombia Governmental
COVID database through Socrata API and parse rows to the same pattern before
inserting into the SQL Database. Receives the data and uses a date range to
create chunk slices and yield them with the updated values.

Methods
-------

chunked_fetch():
    Returns a DataFrame with the chunk of Colombia data with parsed values
    in order to load them into SQL DB.
"""
from datetime import datetime, timedelta

import pandas as pd

from epigraphhub.data.data_collection.config import COLOMBIA_CLIENT

client = COLOMBIA_CLIENT


def chunked_fetch(maxrecords, start=0, chunk_size=10000):
    """
    Connects to Colombia database through Socrata API and generates
    slices of data in chunks in order to insert them into
    positive_cases_covid_d table. Updates the different values into
    a pattern to be easily queried.

    Args:
        maxrecords (int)   : Total rows count in the Colombia data.
        start (int)        : Parameter used to delimit the start of the
                             records in Colombia data.
        chunk_size (int)   : Size of the chunk to be inserted into SQL DB.

    Yields:
        df_new (DataFrame) : Dataframe with updated rows of fixed size.
    """
    slice_date = datetime.date(datetime.today()) - timedelta(200)

    slice_date = slice_date.strftime("%Y-%m-%d")

    while start < maxrecords:

        # Fetch the set of records starting at 'start'
        # create a df with this chunk files
        df_new = pd.DataFrame.from_records(
            client.get(
                "gt2j-8ykr",
                offset=start,
                limit=chunk_size,
                order="fecha_reporte_web",
                where=f'fecha_reporte_web > "{slice_date}"',
            )
        )

        df_new = df_new.rename(columns=str.lower)

        if df_new.empty:
            break

        df_new.set_index(["id_de_caso"], inplace=True)

        df_new = df_new.convert_dtypes()

        # change some strings to a standard
        df_new.replace(
            to_replace={
                "ubicacion": {"casa": "Casa", "CASA": "Casa"},
                "estado": {"leve": "Leve", "LEVE": "Leve"},
                "sexo": {"f": "F", "m": "M"},
            },
            inplace=True,
        )

        # transform the datetime columns in the correct time
        for c in df_new.columns:
            if c.lower().startswith("fecha"):
                df_new[c] = pd.to_datetime(df_new[c], errors="coerce")

        # eliminate any space in the end and start of the string values
        for i in df_new.select_dtypes(include=["string"]).columns:
            df_new[i] = df_new[i].str.strip()

        # Move up the starting record
        start = start + chunk_size

        yield df_new
