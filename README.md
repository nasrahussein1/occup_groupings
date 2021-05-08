# occup_groupings

## Introduction

###The Challenge

There is currently no transparent skills mapping to identify occupations with adjacent skills that workers could easily transition to. While this is the case, worker career opportunities are limited and occupations may be understaffed due to perceived barriers to entry.

Moreover, the current occupation classification framework, ISCO (International Standard Classification of Occupations), which groups occupations requiring similar skills and duties, may not be optimal. This could leave occupations with overlapping skill
requirements classified independently.

### Methodology

An alternative occupation classification was produced. The following methodology was use:

- Produce a data driven alternative classification to ISCO to challenge the existing framework

- Use Natural Language Processing on skills and role descriptions to identify "meaningful" words and find occupations which share these words

- Use hierarchical clustering to group together occupations which share these "meaningful" words to an extent which is statistically significant

##Data Inputs

- ISCO occupations
- Description of skills in the ESCO framework
- ESCO skills dictionary

## Setup

- Meet the data science cookiecutter [requirements](http://nestauk.github.io/ds-cookiecutter), in brief:
  - Install: `git-crypt`
  - Have a Nesta AWS account configured with `awscli`
- Run `make install` to configure the development environment:
  - Setup the conda environment
  - Configure pre-commit
  - Configure metaflow to use AWS

## Contributor guidelines

[Technical and working style guidelines](https://github.com/nestauk/ds-cookiecutter/blob/master/GUIDELINES.md)

---

<small><p>Project based on <a target="_blank" href="https://github.com/nestauk/ds-cookiecutter">Nesta's data science project template</a>
(<a href="http://nestauk.github.io/ds-cookiecutter">Read the docs here</a>).
</small>
