def load_hdfs(path):
    with open(path) as f:
        return [line.strip() for line in f.readlines()]