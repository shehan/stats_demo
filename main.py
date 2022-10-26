import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import mannwhitneyu

df_v1 = pd.read_csv('data/jenkins-jenkins-2.328.csv')
# df_v2 = pd.read_csv('data/jenkins-jenkins-2.375.csv')
df_v2 = pd.read_csv('data/jenkins-jenkins-2.186.csv')

v1 = "2.328"
# v2="2.375"
v2 = "2.186"


def is_statistically_significant(mw_result, data1, data2, data_label, data1_label, data2_label):
    df_consolidated = pd.concat([data1, data2], axis=1)
    df_consolidated.columns = [data1_label, data2_label]
    ax = df_consolidated.boxplot()
    ax.get_figure().suptitle(t=data_label, fontsize=16)
    plt.show()

    if mw_result.pvalue < 0.05:
        print("Statistically Significant ")
    else:
        print("NOT Statistically Significant ")


print("RatioCommentToCode")
comment_df1 = df_v1[~df_v1['RatioCommentToCode'].isnull()]['RatioCommentToCode']
comment_df3 = df_v2[~df_v2['RatioCommentToCode'].isnull()]['RatioCommentToCode']
results = mannwhitneyu(comment_df1, comment_df3)
print(results)
is_statistically_significant(results, comment_df1, comment_df3, "RatioCommentToCode", v1, v2)
print("---------------------------------------")

print("CountLineCode")
loc_df1 = df_v1[~df_v1['CountLineCode'].isnull()]['CountLineCode']
loc_df3 = df_v2[~df_v2['CountLineCode'].isnull()]['CountLineCode']
results = mannwhitneyu(loc_df1, loc_df3)
print(results)
is_statistically_significant(results, loc_df1, loc_df3, "CountLineCode", v1, v2)
print("---------------------------------------")

print("Cyclomatic")
cyclomatic_df1 = df_v1[~df_v1['Cyclomatic'].isnull()]['Cyclomatic']
cyclomatic_df3 = df_v2[~df_v2['Cyclomatic'].isnull()]['Cyclomatic']
results = mannwhitneyu(cyclomatic_df1, cyclomatic_df3)
print(results)
is_statistically_significant(results, cyclomatic_df1, cyclomatic_df3, "Cyclomatic", v1, v2)
print("---------------------------------------")
