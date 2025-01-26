import cv2
import numpy as np
import logging
from datetime import datetime

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S.%f",
)


def input_data():
    """入力画像の読み込み"""
    logging.info("input_data: 画像の読み込みを開始します。")
    try:
        img = cv2.imread("data/road.jpg")
        img_g = cv2.imread("data/road.jpg", 0)
        if img is None or img_g is None:
            raise FileNotFoundError(
                "画像ファイルが見つかりません。パスを確認してください"
            )
        logging.info("input_data：画像の読み込みが完了しました。")
    except Exception as e:
        logging.error(f"input_data: 画像の読込中にエラーが発生しました： {e}")
        raise e
    # cv2.imshow("img", img)
    # cv2.imshow("img_g", img_g)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img, img_g


def edge_detection(img_g):
    """エッジ検出を行う"""
    logging.info("edge_detection: エッジ検出を開始します。")
    img_canny = cv2.Canny(img_g, 300, 450)
    # cv2.imshow("img_canny", img_canny)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_canny


def line_detection(img_canny, img):
    """ハフ変換を用いて線を検出し、画像に描画"""
    logging.info("line_detection: 線の検出を開始します。")
    lines = cv2.HoughLines(
        img_canny, rho=1, theta=np.pi / 360, threshold=100
    )  # ρの刻み幅、回転の刻み角度,100回以上ρとθの組み合わせが現れるとlinesに追加される
    # print(type(lines))

    for i in lines[:]:
        rho = i[0][0]

        theta = i[0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = rho * a
        y0 = rho * b
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

    return img


def main():
    """メイン処理"""
    logging.info("プログラムの実行を開始します。")
    start_time = datetime.now()
    img, img_g = input_data()
    img_canny = edge_detection(img_g)
    img = line_detection(img_canny, img)
    cv2.imshow("img_canny", img_canny)
    cv2.imshow("img_line", img)
    logging.info("プログラムの実行が完了しました")
    end_time = datetime.now()
    execution_time = (end_time - start_time).total_seconds() * 1000
    print(f"プログラムの実行時間： {execution_time:.2f}ms")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
