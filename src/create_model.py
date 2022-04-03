import tensorflow as tf
import pickle as pickle


model = tf.keras.applications.VGG19(
        include_top = True,
        weights = "imagenet",
        input_tensor = None,
        input_shape = None,
        pooling = None,
        classes = 1000,
        classifier_activation = "softmax",)


#model.save("../models/vgg19")
model.save("../models/vgg19.h5")
# pickle.dump(model, open("../models/vgg19.pkl", "wb"))