import pandas as pd
from occup_groupings.getters.inputs.esco_occup_skills import get_esco_occup_skills


def esco_occup_skils_df() -> pd.DataFrame:
    """create occup_skills dataframe with fields: occupation, skills_link, essential_skill

    Returns:
        dataframe: esco occup skills data restructured
    """

    esco_occup_skills = get_esco_occup_skills()

    esco_occup_skills_df = pd.DataFrame(
        columns=["occupation", "skills_link", "essential_skill"]
    )

    occup_list = esco_occup_skills.columns.tolist()

    # Append values to esco_occup_skils dataframe

    for occup in occup_list:
        try:
            number_of_elements = len(
                esco_occup_skills[occup]["_links"]["hasEssentialSkill"]
            )

            for i in range(number_of_elements):
                skills_link = esco_occup_skills[occup]["_links"]["hasEssentialSkill"][
                    i
                ]["uri"]
                essential_skill = esco_occup_skills[occup]["_links"][
                    "hasEssentialSkill"
                ][i]["title"]

                esco_occup_skills_df = esco_occup_skills_df.append(
                    pd.DataFrame(
                        {
                            "occupation": occup,
                            "skills_link": skills_link,
                            "essential_skill": essential_skill,
                        },
                        index=[0],
                    ),
                    ignore_index=True,
                )

        except KeyError:
            continue

    return esco_occup_skills_df
