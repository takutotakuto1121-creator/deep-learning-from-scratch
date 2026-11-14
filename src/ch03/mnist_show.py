import sys, os
import numpy as np
from PIL import Image
from src.dataset.mnist import load_mnist


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def mnist_show():
    """
    load_mnist()は(訓練画像, 訓練ラベル), (テスト画像, テストラベル)を返す
    normalize: 入力画像を0.0~1.0に正規化
    flatten: 入力画像を１次元配列にする
    one_hot_label: ラベルがone-hot表現(通常は1, 7のような正解データのところ、[0, ..., 1, 0]のように正解のみ1のラベルになる)
    """
    print("= mnist_show =")

    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
    img = x_train[0]
    label = t_train[0]
    print(label)

    print(img.shape)
    img = img.reshape(28, 28)
    print(img.shape)

    img_show(img)
    print()
    