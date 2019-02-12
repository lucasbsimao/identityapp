import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.examples.tutorials.mnist import input_data

class Model:

	def create_model(self):
		self.train_finished = False
		mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

		n_train = mnist.train.num_examples # Taining data
		n_validation = mnist.validation.num_examples # Validation data
		n_test = mnist.test.num_examples # Testing data

		n_input = 784 # Input layer (28X28 pixels)
		n_hidden1 = 512 # 1st hidden layer
		n_hidden2 = 256 # 2nd hidden layer
		n_hidden3 = 128 # 3rd hidden layer
		n_output = 10 # Output layer (0-9 digits)

		learning_rate = 1e-4
		n_iterations = 1000
		batch_size = 128
		dropout = 0.5

		self.X = tf.placeholder("float", [None, n_input])
		Y = tf.placeholder("float", [None, n_output])
		keep_prob = tf.placeholder(tf.float32) # Control dropout rate

		weights = {
			'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
			'w2': tf.Variable(tf.truncated_normal([n_hidden1, n_hidden2], stddev=0.1)),
			'w3': tf.Variable(tf.truncated_normal([n_hidden2, n_hidden3], stddev=0.1)),
			'out': tf.Variable(tf.truncated_normal([n_hidden3, n_output], stddev=0.1)),
		}

		biases = {
			'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
			'b2': tf.Variable(tf.constant(0.1, shape=[n_hidden2])),
			'b3': tf.Variable(tf.constant(0.1, shape=[n_hidden3])),
			'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
		}

		layer_1 = tf.add(tf.matmul(self.X, weights['w1']), biases['b1'])
		layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
		layer_3 = tf.add(tf.matmul(layer_2, weights['w3']), biases['b3'])
		layer_drop = tf.nn.dropout(layer_3, keep_prob)
		self.output_layer = tf.matmul(layer_3, weights['out']) + biases['out']

		cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=self.output_layer)) # Loss function
		train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy) # Gradient descent optimization

		correct_pred = tf.equal(tf.argmax(self.output_layer, 1), tf.argmax(Y, 1))
		accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

		init = tf.global_variables_initializer()
		self.sess = tf.Session()
		self.sess.run(init)

		# Training on mini batches
		for i in range(n_iterations):
			batch_x, batch_y = mnist.train.next_batch(batch_size)
			self.sess.run(train_step, feed_dict={self.X: batch_x, Y: batch_y, keep_prob:dropout})

			# Print loss and accuracy (per minibatch)
			if i%100 == 0:
				minibatch_loss, minibatch_accuracy = self.sess.run([cross_entropy, accuracy], feed_dict={self.X: batch_x, Y: batch_y, keep_prob: 1.0})
				print("Iteration", str(i), "\t| Loss =", str(minibatch_loss), "\t| Accuracy =", str(minibatch_accuracy))

		test_accuracy = self.sess.run(accuracy, feed_dict={self.X: mnist.test.images, Y: mnist.test.labels, keep_prob: 1.0})
		print("\nAccuracy on test set:", test_accuracy)

		# Testing over sample image
		img = np.invert(Image.open("test_img.png").convert('L')).ravel()
		prediction = self.sess.run(tf.argmax(self.output_layer, 1), feed_dict={self.X: [img]})
		print("Prediction for test image:", np.squeeze(prediction))

		self.train_finished = True
	
	def predict(self):
		if self.train_finished == False:
			return None
		# img = tf.image.decode_image(img_bytes)
		img = np.invert(Image.open("test_img.png").convert('L')).ravel()
		prediction = self.sess.run(tf.argmax(self.output_layer, 1), feed_dict={self.X: [img]})
		print("Prediction for test image:", np.squeeze(prediction))
		return prediction
