import ddddocr


def dddd():
    """
    验证码图片识别
    :return:
    """
    ocr = ddddocr.DdddOcr(show_ad=False)

    with open("src/base/pic/img.png", 'rb') as f:
        image = f.read()

    res = ocr.classification(image)
    return res


if __name__ == '__main__':
    print(dddd())