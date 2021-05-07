"""generate full descriptions of occupations based on skills and descriptions
"""

import pandas as pd
from occup_groupings.pipeline.create_esco_occup_skills_df import esco_occup_skils_df
from occup_groupings.getters.inputs.esco_occup_skills import get_skills
from occup_groupings.getters.inputs.esco_occup_skills import get_occupations
from occup_groupings.utils.concats import concat_cols
from occup_groupings.utils.concats import concat_rows


def generate_skills_data():
    """join esco_occup_skills and skill dataframes and concatenated skills columns

    Returns:
        dataframe: manipulated skills dataframe with concatenated text data
    """
    skills_col_list = ["essential_skill", "description"]
    skills_join = pd.merge(
        esco_occup_skils_df(),
        get_skills(),
        how="left",
        left_on="skills_link",
        right_on="conceptUri",
    )[["occupation", "essential_skill", "description"]]
    skills_join["skill_and_description_concat"] = concat_cols(
        skills_join, skills_col_list
    )
    return concat_rows(skills_join, "occupation", "skill_and_description_concat")


def generate_occup_data():
    """concatenate string columns in occupations dataset

    Returns:
        dataframe:manipulated skills and occupations dataframe with concatenated text data
    """
    occupations = get_occupations()
    occup_col_list = ["preferredLabel", "description"]
    occupations["occuplabel_and_description_concat"] = concat_cols(
        occupations, occup_col_list
    )
    occupations.drop(
        occupations.columns.difference(
            ["occuplabel_and_description_concat", "preferredLabel"]
        ),
        1,
        inplace=True,
    )
    return occupations
