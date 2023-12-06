import pandas as pd
df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

# 1)

df_2015 = df[df['year'] == 2015]
H_top10_2015 = df_2015.nlargest(10, 'H')['batter_name']
avg_top10_2015 = df_2015.nlargest(10, 'avg')['batter_name']
HR_top10_2015 = df_2015.nlargest(10, 'HR')['batter_name']
OBP_top10_2015 = df_2015.nlargest(10, 'OBP')['batter_name']

df_2016 = df[df['year'] == 2016]
H_top10_2016 = df_2016.nlargest(10, 'H')['batter_name']
avg_top10_2016 = df_2016.nlargest(10, 'avg')['batter_name']
HR_top10_2016 = df_2016.nlargest(10, 'HR')['batter_name']
OBP_top10_2016 = df_2016.nlargest(10, 'OBP')['batter_name']

df_2017 = df[df['year'] == 2017]
H_top10_2017 = df_2017.nlargest(10, 'H')['batter_name']
avg_top10_2017 = df_2017.nlargest(10, 'avg')['batter_name']
HR_top10_2017 = df_2017.nlargest(10, 'HR')['batter_name']
OBP_top10_2017 = df_2017.nlargest(10, 'OBP')['batter_name']

df_2018 = df[df['year'] == 2018]
H_top10_2018 = df_2018.nlargest(10, 'H')['batter_name']
avg_top10_2018 = df_2018.nlargest(10, 'avg')['batter_name']
HR_top10_2018 = df_2018.nlargest(10, 'HR')['batter_name']
OBP_top10_2018 = df_2018.nlargest(10, 'OBP')['batter_name']

print(H_top10_2015)
print()
print(avg_top10_2015)
print()
print(HR_top10_2015)
print()
print(OBP_top10_2015)
print()

print(H_top10_2016)
print()
print(avg_top10_2016)
print()
print(HR_top10_2016)
print()
print(OBP_top10_2016)
print()

print(H_top10_2017)
print()
print(avg_top10_2017)
print()
print(HR_top10_2017)
print()
print(OBP_top10_2017)
print()

print(H_top10_2018)
print()
print(avg_top10_2018)
print()
print(HR_top10_2018)
print()
print(OBP_top10_2018)
print()

#-----------------------------------------------------------------------------------------
# 2)

df_top1_2018 = df_2018.sort_values(by="war", ascending=False).groupby("cp").head(1)
print(df_top1_2018['batter_name'])
print()

#--------------------------------------------------------------------------------------
# 3)

a=[]
a.append(df.R.corr(df.salary))
a.append(df.H.corr(df.salary))
a.append(df.HR.corr(df.salary))
a.append(df.RBI.corr(df.salary))
a.append(df.SB.corr(df.salary))
a.append(df.war.corr(df.salary))
a.append(df.avg.corr(df.salary))
a.append(df.OBP.corr(df.salary))
a.append(df.SLG.corr(df.salary))

max_idx = a.index(max(a))
if max_idx == 0 :
    print('R')
elif max_idx == 1:
    print('H')
elif max_idx == 2:
    print('HR')
elif max_idx == 3:
    print('RBI')
elif max_idx == 4:
    print('SB')
elif max_idx == 5:
    print('war')
elif max_idx == 6:
    print('avg')
elif max_idx == 7:
    print('OBP')
elif max_idx == 8:
    print('SLG')

print()