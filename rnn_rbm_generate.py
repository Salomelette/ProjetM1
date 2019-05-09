import tensorflow as tf
import numpy as np
import rnn_rbm
import extract_polyphonic  
import os
database = os.listdir("./database")

#num correspond aux nombres de chansons a generer 
def generate_music(ckpt_datapath):

    x, generate, cost, W, bh, bv, learning_rate, Wuh, Wuv, Wvu, Wuu, bu, u0 = rnn_rbm.rnnrbm()
    variables = [W, Wuh, Wuv, Wvu, Wuu, bh, bv, bu, u0]

    saver = tf.train.Saver(variables) #ha c'est là qu'il a tout gardé ??

    songs = extract_polyphonic.extract_poly(database)[0]

    with tf.Session() as session:
        init = tf.initializers.global_variables()
        session.run(init)

        saver.restore(session, ckpt_datapath) #a faire ou pas ?? 

        generated_music = session.run(generate(700), feed_dict={x: songs})
        print(generated_music)
        #return generated_music
        new_music_filename = "generated_music_beeth.mid"
        extract_polyphonic.write_midi_poly(generated_music,new_music_filename)

if __name__=="__main__":
    q=generate_music("./ckpt_dir/epoch_100.ckpt")# ckpt_datapath ? c'est quoi ca ? 








