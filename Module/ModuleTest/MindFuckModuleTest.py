import sys
import os

mft_path = os.path.dirname(__file__)

sys.path.insert(0, mft_path[:-11])

import MindFuckModule as mf

def main(mft_path):
    mf.run(os.path.join(mft_path, "mft_test.mfs"))

if __name__ == "__main__":
    main(mft_path)
