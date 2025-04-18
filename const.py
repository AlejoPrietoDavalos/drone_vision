from pathlib import Path

path_data = Path("data")
path_ntut = path_data / "ntut"
path_labels = path_ntut / "labels"
path_train = path_ntut / "train"
path_test = path_ntut / "test"
path_ntut.mkdir(parents=True, exist_ok=True)
path_labels.mkdir(parents=True, exist_ok=True)
path_train.mkdir(parents=True, exist_ok=True)
path_test.mkdir(parents=True, exist_ok=True)
