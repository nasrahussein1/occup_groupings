"""join all occupations and skills descriptions
    write resulting dataframe to an s3 bucket
"""

import pandas as pd
from occup_groupings.utils.to_s3 import write_to_s3
from occup_groupings.utils.concats import concat_cols
from occup_groupings.pipeline.generate_skills_and_occup_data import generate_occup_data
from occup_groupings.pipeline.generate_skills_and_occup_data import generate_skills_data


def generate_data():
    """join manipulated dataframes with concatenated skills and occupation descriptions columns

    Returns:
        dataframe: joined dataset with full descriptions for each occupation
    """
    occup_skills_join = pd.merge(
        generate_skills_data(),
        generate_occup_data(),
        how="left",
        left_on="occupation",
        right_on="preferredLabel",
    )
    col_list = ["skill_and_description_concat", "occuplabel_and_description_concat"]
    occup_skills_join["skills_and_occup_descr"] = concat_cols(
        occup_skills_join, col_list
    ).str.replace("\d+", "")

    occup_skills_join.drop(
        occup_skills_join.columns.difference(["occupation", "skills_and_occup_descr"]),
        1,
        inplace=True,
    )

    write_to_s3(
        occup_skills_join, "occup-groupings-nh", "data/processed/occup_skills_join.csv"
    )
