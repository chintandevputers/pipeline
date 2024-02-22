from mage_ai.data_cleaner.transformer_actions.constants import ImputationStrategy
from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame
import pandas as pd
import numpy as np
from mage_ai.io.file import FileIO

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(dataframes: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.IMPUTE

    Docs: https://docs.mage.ai/guides/transformer-blocks#fill-in-missing-values
    """
    # filepath = 'download_csv/booking_data.csv'
    # data_local = FileIO().load(filepath)
    # df = data_local
    cleansed_data = []

    # df = df[0]

    for df in dataframes:

        action = build_transformer_action(
            df,
            action_type=ActionType.IMPUTE,
            arguments=df.columns,  # Specify columns to impute
            axis=Axis.COLUMN,
            options={'strategy': ImputationStrategy.CONSTANT},  # Specify imputation strategy
        )
        df = BaseAction(action).execute(df)

        if 'booking_id' in df:
            df['booking_date'] = pd.to_datetime(df['booking_date'], format='%Y-%m-%d')
            df['booking_date'] = df['booking_date'].dt.strftime('%Y-%m-%d')

            # df.fillna(0, inplace=True)
            df['total_booking_value'] = df['number_of_passengers'] * df['cost_per_passenger']
            df = df[~((df['booking_id'] == 0) | (df['customer_id'] == 0) | (df['destination_id'] == 0))]
        elif 'customer_id' in df:
            df = df[~((df['customer_id'] == 0))]
        elif 'destination_id' in df :
            df = df[~((df['destination_id'] == 0))]

        cleansed_data.append(df.copy())  # Copy the DataFrame to avoid chained assignment

    return cleansed_data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
