import tensorflow as tf

flags = tf.app.flags

############################
#    hyper parameters      #
############################

# For separate margin loss
flags.DEFINE_float('m_plus', 0.9, 'the parameter of m plus')
flags.DEFINE_float('m_minus', 0.1, 'the parameter of m minus')
flags.DEFINE_float('lambda_val', 0.5, 'down weight of the loss for absent digit classes')

# for training
flags.DEFINE_integer('batch_size', 64, 'batch size') #128->64, 128 will overflow memory
flags.DEFINE_integer('epoch', 50, 'epoch') #origin 50
flags.DEFINE_integer('iter_routing', 3, 'number of iterations in routing algorithm')
flags.DEFINE_boolean('mask_with_y', True, 'use the true label to mask out target capsule or not')

flags.DEFINE_float('stddev', 0.01, 'stddev for W initializer')
flags.DEFINE_float('regularization_scale', 0.392, 'regularization coefficient for reconstruction loss, default to 0.0005*784=0.392')
#if change 28*28 to x*x, regularization_scale need to change too


############################
#   environment setting    #
############################
flags.DEFINE_string('dataset', 'mnist', 'The name of dataset [myself, fashion-mnist')
flags.DEFINE_boolean('is_training', True, 'train or predict phase')
flags.DEFINE_integer('num_threads', 8, 'number of threads of enqueueing examples')
flags.DEFINE_string('logdir', 'logdir', 'logs directory')
flags.DEFINE_integer('train_sum_freq', 10, 'the frequency of saving train summary(step)') #100
flags.DEFINE_integer('val_sum_freq', 50, 'the frequency of saving valuation summary(step)') #500
flags.DEFINE_integer('save_freq', 5, 'the frequency of saving model(epoch)') #3
flags.DEFINE_string('results', 'results', 'path for saving results')

############################
#   distributed setting    #
############################
flags.DEFINE_integer('num_gpu', 1, 'number of gpus for distributed training') #2
flags.DEFINE_integer('batch_size_per_gpu', 128, 'batch size on 1 gpu')
flags.DEFINE_integer('thread_per_gpu', 4, 'Number of preprocessing threads per tower.')

cfg = tf.app.flags.FLAGS
# tf.logging.set_verbosity(tf.logging.INFO)
