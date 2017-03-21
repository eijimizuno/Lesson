

# -*- coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def main():
    # CSVのロード
    data = np.genfromtxt("nikkei16.csv",delimiter=",", skip_header=1, dtype='float')
    
    # 5行目を抽出(日経平均株価の終値)
    f = data[:,4]/1000.0
    
    #　xの値を生成
    x = np.linspace(1, len(f), len(f))
    
    #　フィッティング
    a, b = np.polyfit(x, f, 1)
    
    # フィッティング直線
    fh = a * x + b
    
    # グラフ作成
    plt.figure(1)

    # サンプル(日経平均株価)
    plt.plot(x, f,  label="f")
    plt.plot(x, fh, label="fh")
    #　ラベル軸
    plt.xlabel("Day")
    plt.ylabel("f")
    # 凡例
    plt.legend()
    # グリッド
    plt.grid()
    # グラフ表示
    plt.show()
    
if __name__ == "__main__":
    main()

