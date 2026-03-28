import pandas as pd

df = pd.read_csv("adult.data.csv", header=None)

df.columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week',
    'native-country', 'salary'
]

# 🔥 THIS LINE MUST BE HERE
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1
    )

    higher_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_edu_rich = round(
        (higher_edu[higher_edu['salary'] == '>50K'].shape[0] / higher_edu.shape[0]) * 100, 1
    )

    lower_edu = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_edu_rich = round(
        (lower_edu[lower_edu['salary'] == '>50K'].shape[0] / lower_edu.shape[0]) * 100, 1
    )

    min_work_hours = df['hours-per-week'].min()

    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1
    )

    country_percent = (
        df[df['salary'] == '>50K']['native-country'].value_counts() /
        df['native-country'].value_counts() * 100
    )

    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }