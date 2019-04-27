import pandas as pd


def get_text(name="reviews", label="plus_s"):
    # LABELS
    # amb
    # minus_m
    # minus_s
    # plus_m
    # plus_s
    # zero

    path = f"/home/maciej/myProjects/char-rnn-keras/data_sentiment_pl/texts/{name}.text.train.txt"
    df = pd.read_csv(path, header=None, engine="python", sep="__label__meta_")

    labels = pd.Series(df.iloc[:, 1]).unique()
    print(labels)

    for label_i, df_label in df.groupby(1):
        if label_i == label:
            return " ".join(df_label.iloc[:, 0])
            # splitted_without_sw = [w for w in splitted if w not in df_sw.values and len(w)>1]
