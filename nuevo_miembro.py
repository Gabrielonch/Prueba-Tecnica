import pandas as pd # Libreria pandas para el manejo de datos
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sbn

sbn.set_style("darkgrid")
sbn.set_palette("bright")


plt.style.use('ggplot')
markers = ['*' 'k', 'v','P','X','^']
colors = ['#e74c3c','#5dade2','#58d68d','#af7ac5','#f7dc6f']

score = pd.read_csv("documentos/tiempos_para_llegar_al_mejor_score.csv")

dias = list(score.Day.unique())
players= list(score['Player ID'].unique())
media = score.groupby("Player ID")['Minutes to get that score'].mean()


plt.figure(figsize=(20,6))
sbn.lineplot(x="Day", y="Minutes to get that score", hue='Player ID', data=score, palette=colors, markers=True,)

plt.title("Score", fontsize=20)
plt.ylabel("Tiempo",fontsize=18)
plt.xlabel("Día",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(dias,fontsize = 18)
#plt.xlim(-1,20)
ax.xaxis.grid(True)
plt.show()
#De acuerdo a la gráfica anterior, el Player 2 fue el que tuvo un mejor rendimiento, ya que solo un día tuvo un tiempo alto para completar la prueba que no pasó los 30 minutos, mientras que los demás jugadores tuvieron 1 o más días en los que les tomo más de 30 minútos en completar la prueba.

f, ax = plt.subplots(figsize=(15, 6))
plt.bar(list(media.index),media, 0.5, color = colors)
plt.title("Tiempo Promedio", fontsize=20)

plt.ylabel("Tiempo en minutos",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(fontsize = 18)

ax.xaxis.grid(True)
for i in range(len(media)):
    plt.annotate('%1.2f' %media[i], xy=((i-0.1),media[i]),fontsize = 16)
plt.show()
#Esta gráfica nos muestra el tiempo promedio que le tomo a cada participante en finalizar su prueba, siendo el **Player 1** el participante que en los 30 días, tardo menos en promedio, seguido del **Player 2** que tuvo un gran rendimiento.

mediana = score.groupby("Player ID")['Minutes to get that score'].median()
f, ax = plt.subplots(figsize=(12, 8))
plt.title("Tiempo para score", fontsize=20)
sbn.violinplot(y="Player ID", x="Minutes to get that score", data=score, palette=colors)
sns.stripplot(y="Player ID", x="Minutes to get that score", data=score ,size=5, color="k", linewidth=0, alpha=.6)

plt.xlabel("Tiempo en minutos",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(fontsize = 18)
plt.xlim(-5,40)
ax.xaxis.grid(True)


plt.show()

#Esta última gráfica muestra los tiempos que obtuvieron los participantes y su distribución en los 30 días que se realizó la prueba, siendo el Player 1 y el Player 2 quienes demostraron mejores resultados al tener una mayor concentración de sus resultados en los valores debajo de 5 minutos al observarse una gráfica más amplia en esa zona en comparación con los diferentes participantes.


genero = pd.read_csv("documentos/scores_by_game_and_player.csv")

genero.columns = ['match','player','adventure', 'score']
print("Se jugaron un total de", genero.adventure.nunique(), 'generos de videojuegos')
print('Las categorías son:', str(genero.adventure.unique()))
print('Cada uno de los', genero.player.nunique(), 'jugadores jugó \n', genero.groupby(['player','adventure']).match.count())

promedio = (genero[genero.score > 10].groupby(['adventure','player']).score.count()/genero.groupby(['player','adventure']).match.count())
action = promedio[0:5]
fps = promedio[5:10]
rpg = promedio[10:15]
titulo = [ 'action', 'fps', 'rpg']

f, ax = plt.subplots(figsize=(12, 5))

plt.bar(genero.player.unique(),action, 0.5, color=colors)
plt.title("Action", fontsize=20)
plt.ylabel("Porcentaje",fontsize=18)
plt.yticks([0,0.05,0.10,0.15,0.20],fontsize=18)

plt.xticks(fontsize = 18)
    #plt.xlim(-1,20)
ax.xaxis.grid(True)
plt.show()
#Esta gráfica nos demuestra que el **Player 1** y el **Player 3** fueron los que obtuvieron mejores resultados al tener un 20% de partidas exitosas en el genero **Action** .

f, ax = plt.subplots(figsize=(12, 5))

plt.bar(genero.player.unique(),fps, 0.5, color=colors)
plt.title("FPS", fontsize=20)
plt.ylabel("Porcentaje",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(fontsize = 18)
    #plt.xlim(-1,20)
ax.xaxis.grid(True)
plt.show()

#En el genero FPS el Player 3 fue quien obtuvo el mejor resultado con un 35% de sus partidas exitosas, seguido de el Player 4 y Player 5 con un 15% de partidas exitosas.

f, ax = plt.subplots(figsize=(12, 5))

plt.bar(genero.player.unique(),rpg, 0.5, color=colors)
plt.title("RPG", fontsize=20)
plt.ylabel("Porcentaje",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(fontsize = 18)
    #plt.xlim(-1,20)
ax.xaxis.grid(True)
plt.show()
#En el genero RPG hubo un resultado homogeneo de 25% de partidas exitosas, siendo el Player 3 el que peor desempeño tuvo en esta categoría con un 10% de partidas exitosas.

pos = pd.read_csv("documentos/position_of_players.csv")

a=0
f, ax = plt.subplots(figsize=(12,12))

for play in players:
 
    plt.plot(pos[pos.No == play].Longitud, pos[pos.No == play].Latitude, '.', color=colors[a],markersize=18, mec = 'k', alpha = 0.65)
    
    a=a+1
    
plt.legend(players)
sbn.kdeplot(x='Longitud', y='Latitude',levels=3, color="k", linewidths=1, data=pos)
plt.title("Posición de Jabalina", fontsize=20)
plt.xlabel("Longitud",fontsize=18)
plt.ylabel("Latitud",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(fontsize = 18)

ax.grid(True)   


plt.show()
#Esta gráfica muestra la posición de cada jabalina lanzada por cada participante, mostrando que los lanzamientos se agruparon principalmente en una zona.


a=0
f, ax = plt.subplots(figsize=(12,12))

for play in players:
 
    plt.plot(pos[pos.No == play].Longitud, pos[pos.No == play].Latitude, '.', color=colors[a],markersize=18, mec = 'k', alpha = 0.65)
    
    a=a+1
    
plt.legend(players)
sbn.kdeplot(x='Longitud', y='Latitude',levels=3, color="k", linewidths=1, data=pos)
plt.title("Posición de Jabalina", fontsize=20)
plt.xlabel("Longitud",fontsize=18)
plt.ylabel("Latitud",fontsize=18)
plt.yticks(fontsize=18)
plt.xticks(fontsize = 18)
    #plt.xlim(-1,20)
ax.grid(True)   

plt.xlim(121.52, 121.56)
plt.ylim(24.96,24.99)
plt.show()

a=0


for play in players:
    f, ax = plt.subplots(figsize=(10, 10)) 
    plt.plot(pos[pos.No == play].Longitud, pos[pos.No == play].Latitude, 'o', color=colors[a],markersize=12, mec = 'k', alpha = 0.7)
    sbn.kdeplot(x=pos[pos.No == play].Longitud, y=pos[pos.No == play].Latitude, levels=3, color="k", linewidths=1)
    #plt.legend(players[a])
    plt.title("Posición de Jabalina de %s" %players[a], fontsize=20)
    plt.xlabel("Longitud",fontsize=18)
    plt.ylabel("Latitud",fontsize=18)
    plt.yticks(fontsize=18)
    plt.xticks(fontsize = 18)
    plt.xlim(pos.Longitud.min()-0.01,pos.Longitud.max()+0.01)
    plt.ylim(pos.Latitude.min()-0.01,pos.Latitude.max()+0.01)
    ax.grid(True) 
    plt.show()
    #print(players[a])
    a=a+1
    
    
