from nnpcr import NNPCR
import tensorflow as tf

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2, allow_growth=True)
session_config = tf.ConfigProto(device_count={'GPU': 0}, gpu_options=gpu_options)
sess_emb = tf.Session(config=session_config)
model = NNPCR()
model.loadModel('nnmodel.bin')
predictions = model.predict(['8.jpg'])
print predictions
