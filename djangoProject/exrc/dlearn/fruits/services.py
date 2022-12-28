import os
import keras
import numpy as np
from keras import layers, Sequential
import tensorflow as tf
import matplotlib.pyplot as plt

from keras.callbacks import ModelCheckpoint
from api.path import fruits

# TF_CPP_MIN_LOG_LEVEL Default Setting 관련 경고 임시 조치
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class FruitsService:

    def __init__(self):
        global \
            trainpath, testpath, \
            Apple_Braeburn_train, Apple_Crimson_Snow_train, \
            Apple_Golden_1_train, Apple_Golden_2_train, Apple_Golden_3_train, \
            Apple_Braeburn_test, Apple_Crimson_Snow_test, \
            Apple_Golden_1_test, Apple_Golden_2_test, Apple_Golden_3_test,\
            batch_size, img_height, img_width, class_names, \
            modelpath

        trainpath = f"{fruits}\\fruits-360-5\\Training"
        testpath = f"{fruits}\\fruits-360-5\\Test"

        Apple_Braeburn_train = f"{trainpath}\\Apple Braeburn"
        Apple_Crimson_Snow_train = f"{trainpath}\\Apple Crimson Snow"
        Apple_Golden_1_train = f"{trainpath}\\Apple Golden 1"
        Apple_Golden_2_train = f"{trainpath}\\Apple Golden 2"
        Apple_Golden_3_train = f"{trainpath}\\Apple Golden 3"

        Apple_Braeburn_test = f"{testpath}\\Apple Braeburn"
        Apple_Crimson_Snow_test = f"{testpath}\\Apple Crimson Snow"
        Apple_Golden_1_test = f"{testpath}\\Apple Golden 1"
        Apple_Golden_2_test = f"{testpath}\\Apple Golden 2"
        Apple_Golden_3_test = f"{testpath}\\Apple Golden 3"

        batch_size = 32
        img_height = 100
        img_width = 100

        self.train_ds = self.load_train_ds()
        self.val_ds = self.load_val_ds()
        self.test_ds = self.load_test_ds()
        self.test_ds1 = self.load_test_ds1()

        class_names = ['Apple Braeburn', 'Apple Crimson Snow', 'Apple Golden 1', 'Apple Golden 2', 'Apple Golden 3']

        modelpath = f"{fruits}\\save\\fruits_model.h5"

    def fruits_hook(self):
        self.create_model()

    def show_apple(self):
        img = tf.keras.preprocessing.image.load_img \
            (f'{Apple_Golden_3_train}\\0_100.jpg')
        plt.imshow(img)
        plt.axis("off")
        plt.show()

    def load_train_ds(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="training",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

    def load_val_ds(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            trainpath,
            validation_split=0.3,
            subset="validation",
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

    def load_test_ds(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size)

    def load_test_ds1(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            testpath,
            seed=1,
            image_size=(img_height, img_width),
            batch_size=batch_size,
            shuffle=False)

    def create_model(self):
        BUFFER_SIZE = 10000
        AUTOTUNE = tf.data.experimental.AUTOTUNE

        train_ds = self.train_ds.cache().shuffle(BUFFER_SIZE).prefetch(buffer_size=AUTOTUNE)
        val_ds = self.val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds = self.test_ds.cache().prefetch(buffer_size=AUTOTUNE)
        test_ds1 = self.test_ds1

        num_classes = 5
        model = Sequential([
            tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
            tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Dropout(.50),
            tf.keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
            tf.keras.layers.MaxPooling2D(2),
            tf.keras.layers.Dropout(.50),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(500, activation='relu'),
            tf.keras.layers.Dropout(.50),
            tf.keras.layers.Dense(num_classes, activation='softmax')
        ])
        model.summary()
        model.compile(
            optimizer='adam',
            loss=tf.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy'])
        checkpointer = ModelCheckpoint(f'{fruits}\\save\\CNNClassifier.h5', save_best_only=True)
        early_stopping_cb = keras.callbacks.EarlyStopping(patience=5, monitor='val_accuracy',
                                                          restore_best_weights=True)
        epochs = 20

        history = model.fit(
            train_ds,
            batch_size=batch_size,
            validation_data=val_ds,
            epochs=epochs,
            callbacks=[checkpointer, early_stopping_cb]
        )

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs_range = range(1, len(loss) + 1)

        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(epochs_range, acc, label='Training Accuracy')
        plt.plot(epochs_range, val_acc, label='Validation Accuracy')
        plt.legend(loc='lower right')
        plt.title('Training and Validation Accuracy')

        plt.subplot(1, 2, 2)
        plt.plot(epochs_range, loss, label='Training Loss')
        plt.plot(epochs_range, val_loss, label='Validation Loss')
        plt.legend(loc='upper right')
        plt.title('Training and Validation Loss')
        plt.show()

        model.load_weights(f'{fruits}\\save\\CNNClassifier.h5')

        test_loss, test_acc = model.evaluate(test_ds)

        print("test loss: ", test_loss)
        print()
        print("test accuracy: ", test_acc)
        predictions = model.predict(test_ds1)

        score = tf.nn.softmax(predictions[0])
        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )

        score = tf.nn.softmax(predictions[-1])
        print(
            "This image most likely belongs to {} with a {:.2f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )


if __name__ == '__main__':
    service = FruitsService()
    service.fruits_hook()
