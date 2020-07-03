import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('playoff_series.csv')
# Remove empty columns along with dates column
df = df.iloc[:, [0, 1, 2, 5, 6, 8, 9, 11, 12]]

df.head()

#%% Split team names and seeds
df[['win_team', 'win_seed']]  = df['Team'].str.strip(')').str.split('(', expand=True)
df[['loss_team', 'loss_seed']]  = df['Team.1'].str.strip(')').str.split('(', expand=True)
df['win_seed'] = pd.to_numeric(df['win_seed'])
df['loss_seed'] = pd.to_numeric(df['loss_seed'])
df.query('W == 3').sort_values('Yr')

#%% Calculate wins and losses by seed for playoffs and finals
seed_wins = df['win_seed'].value_counts()
seed_losses = df['loss_seed'].value_counts()
seed_playoffs = pd.DataFrame({'win': seed_wins, 'loss': seed_losses})

df_finals = df.query('Series == "Finals"')
seed_wins = df_finals['win_seed'].value_counts()
seed_losses = df_finals['loss_seed'].value_counts()
seed_finals = pd.DataFrame({'win': seed_wins, 'loss': seed_losses})


#%% Plot

fig, ax = plt.subplots(nrows = 2, figsize = (8, 8))
width = 0.4

ax[0].bar(seed_playoffs.index - width/2, seed_playoffs['win'], width = width, label = 'Wins')
ax[0].bar(seed_playoffs.index + width/2, seed_playoffs['loss'], width = width, label = 'Losses')
ax[0].legend(loc='upper right')
ax[0].set_ylabel('Playoffs')

ax[1].bar(seed_finals.index - width/2, seed_finals['win'], width = width, label = 'Wins')
ax[1].bar(seed_finals.index + width/2, seed_finals['loss'], width = width, label = 'Losses')
ax[1].legend(loc='upper right')
ax[1].set_xlabel('Seed')
ax[1].set_ylabel('Finals')
plt.show()
