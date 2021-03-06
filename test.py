

#https://www.tensorflow.org/tutorials/sequences/text_generation
from extraction_fichiers import extract
import tensorflow as tf
tf.enable_eager_execution()
import numpy as np
import os
import time
#from discord_hooks import Webhook
from sklearn.model_selection import GridSearchCV
from generateur import create_midi_file


database = os.listdir("./database")
# n = 0.8*len(database)
# database_train = database[:n]
# database_test = database[n+1:]
notes, vel, nb_occ = extract(database,False)
res=notes[0]
res2=[]
#print(res)
for i in range(len(res)):
    #↨print(i)
    velo_keys=list(vel[tuple(res[i])].keys())
    velo_values=list(vel[tuple(res[i])].values())
    tirage=np.random.choice(len(velo_keys), 1, p=velo_values)[0]
    if res[i][0]=="PAUSE":
            res2.append((64,res[i][1],0))
    else:
        res2.append((res[i][0],res[i][1],velo_keys[tirage]))
#print(res2)
create_midi_file(res2,"frkzjkfezls.mid")
#occ_sorted=sorted(nb_occ.items(),key=lambda x:x[1],reverse=True)
#
#
#tab=[(64,1000,60),(64,10,0),(56,100,100),(56,10,0)]
#create_midi_file(tab,"tes2t.mid")



