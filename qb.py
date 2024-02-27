
import os
from time import time
import pandas as pd
import itertools


# Using readlines()
file1_2020 = open('passing_summary (2020).csv', 'r')
file1_2021 = open('passing_summary (2021).csv', 'r')
file1_2022 = open('passing_summary (2022).csv', 'r')
file1_2023 = open('passing_summary (2023).csv', 'r')
file1_2024 = open('passing_summary (2024).csv', 'r')

#file2 = open('wr all pro.txt', 'r')

Lines_2020 = file1_2020.readlines()
Lines_2021 = file1_2021.readlines()
Lines_2022 = file1_2022.readlines()
Lines_2023 = file1_2023.readlines()
Lines_2024 = file1_2024.readlines()
  
count = 0
passing_results_2020 = []
passing_results_2021 = []
passing_results_2022 = []
passing_results_2023 = []
passing_results_2024 = []
allpro_combine = []

# Strips the newline character
for line in Lines_2020:
    passing_results_2020.append(line)

for line in Lines_2021:
    passing_results_2021.append(line)

for line in Lines_2022:
    passing_results_2022.append(line)

for line in Lines_2023:
    passing_results_2023.append(line)

for line in Lines_2024:
    passing_results_2024.append(line)


passing_2020 = []

len_list = []

len_list.append(len(passing_results_2020))
len_list.append(len(passing_results_2021))
len_list.append(len(passing_results_2022))
len_list.append(len(passing_results_2023))
len_list.append(len(passing_results_2024))

print(passing_results_2020[0])








n = max(len_list)
player_list = []
pr_2020 = []
for player in passing_results_2020:
    #print(type(player))
    player_list = player.rstrip('\n').split('\t')
    
    if (player[0] == 'Name' ):
        continue
    else:
        pr_2020.append(player_list)
    
    
pr2020 = []
pr2021 = []
pr2022 = []
pr2023 = []
pr2024 = []

for a, b, c, d, e in zip(passing_results_2020, passing_results_2021,passing_results_2022,passing_results_2023,passing_results_2024): 
    data_2020 = a.rstrip('\n').split(',')
    data_2021 = b.rstrip('\n').split(',')
    data_2022 = c.rstrip('\n').split(',')
    data_2023 = d.rstrip('\n').split(',')
    data_2024 = e.rstrip('\n').split(',')
    
    pr2020.append(data_2020)
    pr2021.append(data_2021)
    pr2022.append(data_2022)
    pr2023.append(data_2023)
    pr2024.append(data_2024)
    
#print(pr2022)
    

df_2020 = pd.DataFrame(pr2020[1:],columns=pr2020[0])
df_2021 = pd.DataFrame(pr2021[1:],columns=pr2021[0])
df_2022 = pd.DataFrame(pr2022[1:],columns=pr2022[0])
df_2023 = pd.DataFrame(pr2023[1:],columns=pr2023[0])
df_2024 = pd.DataFrame(pr2024[1:],columns=pr2024[0])


#astype(float)
print(df_2024)
df_2024.player_game_count = pd.to_numeric(df_2024.player_game_count, errors='coerce')
df_2024.def_gen_pressures = pd.to_numeric(df_2024.def_gen_pressures, errors='coerce')
df_2024.avg_time_to_throw = pd.to_numeric(df_2024.avg_time_to_throw, errors='coerce')
df_2024.sack_percent = pd.to_numeric(df_2024.sack_percent, errors='coerce')
df_2024.hit_as_threw = pd.to_numeric(df_2024.hit_as_threw, errors='coerce')
df_2024.sacks = pd.to_numeric(df_2024.sacks, errors='coerce')
df_2024.pressure_to_sack_rate = pd.to_numeric(df_2024.pressure_to_sack_rate, errors='coerce')
df_2024.accuracy_percent = pd.to_numeric(df_2024.accuracy_percent, errors='coerce')
df_2024.aimed_passes = pd.to_numeric(df_2024.aimed_passes, errors='coerce')
df_2024.attempts = pd.to_numeric(df_2024.attempts, errors='coerce')
df_2024.big_time_throws = pd.to_numeric(df_2024.big_time_throws, errors='coerce')
df_2024.completions = pd.to_numeric(df_2024.completions, errors='coerce')
df_2024.dropbacks = pd.to_numeric(df_2024.dropbacks, errors='coerce')
df_2024.grades_offense = pd.to_numeric(df_2024.grades_offense, errors='coerce')
df_2024.grades_pass = pd.to_numeric(df_2024.grades_pass, errors='coerce')
df_2024.grades_run = pd.to_numeric(df_2024.grades_run, errors='coerce')
df_2024.touchdowns = pd.to_numeric(df_2024.touchdowns, errors='coerce')
df_2024.turnover_worthy_plays = pd.to_numeric(df_2024.turnover_worthy_plays, errors='coerce')
df_2024.twp_rate = pd.to_numeric(df_2024.twp_rate, errors='coerce')

df_2023.player_game_count = pd.to_numeric(df_2023.player_game_count, errors='coerce')
df_2023.def_gen_pressures = pd.to_numeric(df_2023.def_gen_pressures, errors='coerce')
df_2023.avg_time_to_throw = pd.to_numeric(df_2023.avg_time_to_throw, errors='coerce')
df_2023.sack_percent = pd.to_numeric(df_2023.sack_percent, errors='coerce')
df_2023.hit_as_threw = pd.to_numeric(df_2023.hit_as_threw, errors='coerce')
df_2023.sacks = pd.to_numeric(df_2023.sacks, errors='coerce')
df_2023.pressure_to_sack_rate = pd.to_numeric(df_2023.pressure_to_sack_rate, errors='coerce')
df_2023.accuracy_percent = pd.to_numeric(df_2023.accuracy_percent, errors='coerce')
df_2023.aimed_passes = pd.to_numeric(df_2023.aimed_passes, errors='coerce')
df_2023.attempts = pd.to_numeric(df_2023.attempts, errors='coerce')
df_2023.big_time_throws = pd.to_numeric(df_2023.big_time_throws, errors='coerce')
df_2023.completions = pd.to_numeric(df_2023.completions, errors='coerce')
df_2023.dropbacks = pd.to_numeric(df_2023.dropbacks, errors='coerce')
df_2023.grades_offense = pd.to_numeric(df_2023.grades_offense, errors='coerce')
df_2023.grades_pass = pd.to_numeric(df_2023.grades_pass, errors='coerce')
df_2023.grades_run = pd.to_numeric(df_2023.grades_run, errors='coerce')
df_2023.touchdowns = pd.to_numeric(df_2023.touchdowns, errors='coerce')
df_2023.turnover_worthy_plays = pd.to_numeric(df_2023.turnover_worthy_plays, errors='coerce')
df_2023.twp_rate = pd.to_numeric(df_2023.twp_rate, errors='coerce')

#print(df_2022.player_game_count)
df_2022.player_game_count = pd.to_numeric(df_2022.player_game_count, errors='coerce')
df_2022.def_gen_pressures = pd.to_numeric(df_2022.def_gen_pressures, errors='coerce')
df_2022.avg_time_to_throw = pd.to_numeric(df_2022.avg_time_to_throw, errors='coerce')
df_2022.sack_percent = pd.to_numeric(df_2022.sack_percent, errors='coerce')
df_2022.hit_as_threw = pd.to_numeric(df_2022.hit_as_threw, errors='coerce')
df_2022.sacks = pd.to_numeric(df_2022.sacks, errors='coerce')
df_2022.pressure_to_sack_rate = pd.to_numeric(df_2022.pressure_to_sack_rate, errors='coerce')
df_2022.accuracy_percent = pd.to_numeric(df_2022.accuracy_percent, errors='coerce')
df_2022.aimed_passes = pd.to_numeric(df_2022.aimed_passes, errors='coerce')
df_2022.attempts = pd.to_numeric(df_2022.attempts, errors='coerce')
df_2022.big_time_throws = pd.to_numeric(df_2022.big_time_throws, errors='coerce')
df_2022.completions = pd.to_numeric(df_2022.completions, errors='coerce')
df_2022.dropbacks = pd.to_numeric(df_2022.dropbacks, errors='coerce')
df_2022.grades_offense = pd.to_numeric(df_2022.grades_offense, errors='coerce')
df_2022.grades_pass = pd.to_numeric(df_2022.grades_pass, errors='coerce')
df_2022.grades_run = pd.to_numeric(df_2022.grades_run, errors='coerce')
df_2022.touchdowns = pd.to_numeric(df_2022.touchdowns, errors='coerce')
df_2022.turnover_worthy_plays = pd.to_numeric(df_2022.turnover_worthy_plays, errors='coerce')
df_2022.twp_rate = pd.to_numeric(df_2022.twp_rate, errors='coerce')

df_2021.player_game_count = pd.to_numeric(df_2021.player_game_count, errors='coerce')
df_2021.def_gen_pressures = pd.to_numeric(df_2021.def_gen_pressures, errors='coerce')
df_2021.avg_time_to_throw = pd.to_numeric(df_2021.avg_time_to_throw, errors='coerce')
df_2021.sack_percent = pd.to_numeric(df_2021.sack_percent, errors='coerce')
df_2021.hit_as_threw = pd.to_numeric(df_2021.hit_as_threw, errors='coerce')
df_2021.sacks = pd.to_numeric(df_2021.sacks, errors='coerce')
df_2021.pressure_to_sack_rate = pd.to_numeric(df_2021.pressure_to_sack_rate, errors='coerce')
df_2021.accuracy_percent = pd.to_numeric(df_2021.accuracy_percent, errors='coerce')
df_2021.aimed_passes = pd.to_numeric(df_2021.aimed_passes, errors='coerce')
df_2021.attempts = pd.to_numeric(df_2021.attempts, errors='coerce')
df_2021.big_time_throws = pd.to_numeric(df_2021.big_time_throws, errors='coerce')
df_2021.completions = pd.to_numeric(df_2021.completions, errors='coerce')
df_2021.dropbacks = pd.to_numeric(df_2021.dropbacks, errors='coerce')
df_2021.grades_offense = pd.to_numeric(df_2021.grades_offense, errors='coerce')
df_2021.grades_pass = pd.to_numeric(df_2021.grades_pass, errors='coerce')
df_2021.grades_run = pd.to_numeric(df_2021.grades_run, errors='coerce')
df_2021.touchdowns = pd.to_numeric(df_2021.touchdowns, errors='coerce')
df_2021.turnover_worthy_plays = pd.to_numeric(df_2021.turnover_worthy_plays, errors='coerce')
df_2021.twp_rate = pd.to_numeric(df_2021.twp_rate, errors='coerce')

df_2020.player_game_count = pd.to_numeric(df_2020.player_game_count, errors='coerce')
df_2020.def_gen_pressures = pd.to_numeric(df_2020.def_gen_pressures, errors='coerce')
df_2020.avg_time_to_throw = pd.to_numeric(df_2020.avg_time_to_throw, errors='coerce')
df_2020.sack_percent = pd.to_numeric(df_2020.sack_percent, errors='coerce')
df_2020.hit_as_threw = pd.to_numeric(df_2020.hit_as_threw, errors='coerce')
df_2020.sacks = pd.to_numeric(df_2020.sacks, errors='coerce')
df_2020.pressure_to_sack_rate = pd.to_numeric(df_2020.pressure_to_sack_rate, errors='coerce')
df_2020.accuracy_percent = pd.to_numeric(df_2020.accuracy_percent, errors='coerce')
df_2020.aimed_passes = pd.to_numeric(df_2020.aimed_passes, errors='coerce')
df_2020.attempts = pd.to_numeric(df_2020.attempts, errors='coerce')
df_2020.big_time_throws = pd.to_numeric(df_2020.big_time_throws, errors='coerce')
df_2020.completions = pd.to_numeric(df_2020.completions, errors='coerce')
df_2020.dropbacks = pd.to_numeric(df_2020.dropbacks, errors='coerce')
df_2020.grades_offense = pd.to_numeric(df_2020.grades_offense, errors='coerce')
df_2020.grades_pass = pd.to_numeric(df_2020.grades_pass, errors='coerce')
df_2020.grades_run = pd.to_numeric(df_2020.grades_run, errors='coerce')
df_2020.touchdowns = pd.to_numeric(df_2020.touchdowns, errors='coerce')
df_2020.turnover_worthy_plays = pd.to_numeric(df_2020.turnover_worthy_plays, errors='coerce')
df_2020.twp_rate = pd.to_numeric(df_2020.twp_rate, errors='coerce')

sorted_df_2020 = df_2020.sort_values(by = ['def_gen_pressures','sack_percent','hit_as_threw', 'sacks',
                                           'pressure_to_sack_rate' ], axis=0, 
                           ascending=[False,False,False,False,False], 
                           inplace=False,
               kind='quicksort', na_position='first', 
                           ignore_index=True, key=None)




sorted_df_2021 = df_2021.sort_values(by = ['sack_percent','def_gen_pressures','hit_as_threw', 'sacks', 
                                           'pressure_to_sack_rate' ], axis=0, 
                           ascending=[False,False,False,False,False], 
                           inplace=False,
               kind='quicksort', na_position='first', 
                           ignore_index=True, key=None)



sorted_df_2022 = df_2022.sort_values(by = ['sack_percent','def_gen_pressures','hit_as_threw', 'sacks', 
                                           'pressure_to_sack_rate' ], axis=0, 
                           ascending=[False,False,False,False,False], 
                           inplace=False,
               kind='quicksort', na_position='first', 
                           ignore_index=True, key=None)

sorted_df_2023 = df_2023.sort_values(by = ['sack_percent','def_gen_pressures','hit_as_threw', 'sacks', 
                                           'pressure_to_sack_rate' ], axis=0, 
                           ascending=[False,False,False,False,False],  
                           inplace=False,
               kind='quicksort', na_position='first', 
                           ignore_index=True, key=None)



sorted_df_2024 = df_2024.sort_values(by = ['sack_percent','def_gen_pressures','hit_as_threw', 'sacks', 
                                           'pressure_to_sack_rate' ], axis=0, 
                           ascending=[False,False,False,False,False],  
                           inplace=False,
               kind='quicksort', na_position='first', 
                           ignore_index=True, key=None)


top_10 = sorted_df_2020.head(10)
top_10_2021 = sorted_df_2021.head(10)
top_10_2022 = sorted_df_2022.head(10)
top_10_2023 = sorted_df_2023.head(10)
top_10_2024 = sorted_df_2024.head(10)


top10 = pd.concat([top_10,top_10_2021,top_10_2022,top_10_2023])

#df = pd.DataFrame(columns=passing_results_2020[0])

#column_name = passing_results_2020[0].split(',')


#df = pd.DataFrame(pr2020)
#df.columns = column_name
#df.columns = df.iloc[0]

#df = df[1:]

#print(df)

    
#df['col1'] = df. col1.apply(lambda l: [s.split() for s in l])



l = '''
d = {'List_2020' : pd.Series(passing_results_2020),
     'List_2021' : pd.Series(passing_results_2021),
     'List_2022': pd.Series(passing_results_2022),
     'List_2023': pd.Series(passing_results_2023), 
     'List_2024': pd.Series(passing_results_2024)}
'''

#df = pd.DataFrame(d)


sorted_df_2020.to_csv('sorted qb data_2020.csv', index=False)
sorted_df_2021.to_csv('sorted qb data_2021.csv', index=False)
sorted_df_2022.to_csv('sorted qb data_2022.csv', index=False)
sorted_df_2023.to_csv('sorted qb data_2023.csv', index=False)    
sorted_df_2024.to_csv('sorted qb data_2024.csv', index=False)      
top10.to_csv('top.csv', index = False)   



