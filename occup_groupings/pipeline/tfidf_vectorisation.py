"""generate dataframe with tfidf values for words in the corpus for each occupation
"""

import pandas as pd
from occup_groupings.utils.to_s3 import write_to_s3
from occup_groupings import config
from occup_groupings.getters.outputs.joined_skills_data import get_joined_skills
from sklearn.feature_extraction.text import TfidfVectorizer

min_df = config["tfidf_vectorisation"]["params"]["min_df"]
max_df = config["tfidf_vectorisation"]["params"]["max_df"]
stop_words = config["tfidf_vectorisation"]["params"]["stop_words"]


def vectorisation():
    """generate dataframe with words from a document and corresponding tf-idf values
    write dataframe to s3 bucket
    """
    v = TfidfVectorizer(stop_words=stop_words, min_df=min_df, max_df=max_df)
    vectorised_df = pd.DataFrame(
        v.fit_transform(get_joined_skills()["skills_and_occup_descr"]).toarray(),
        columns=v.get_feature_names(),
    )
    tfidf_values = pd.concat([get_joined_skills(), vectorised_df], axis=1)
    write_to_s3(tfidf_values, "occup-groupings-nh", "data/processed/tfidf_values.csv")
