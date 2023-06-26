from pathlib import Path
import pandas


def main():
    dataset = pandas.read_feather("output/dataset.arrow")
    total_events = dataset.num_subcutaneous_morphine_events.sum()
    Path("output/total_subcutaneous_morphine_events.txt").write_text(str(total_events))


if __name__ == "__main__":
    main()
