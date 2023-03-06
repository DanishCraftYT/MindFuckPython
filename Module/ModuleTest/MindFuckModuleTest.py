import sys
import os

mft_path = os.path.dirname(__file__)
mf_path = os.path.dirname(os.path.dirname(mft_path))

sys.path.insert(0, mft_path[:-11])

import MindFuckModule as mf

def main(mft_path):
    mf.compiler(os.path.join(mft_path, "mft_test.mfs"), icon_path=os.path.join(mf_path, "Icons", "icon.ico"))
    mf.run(os.path.join(mft_path, "mft_test.mfs"))

if __name__ == "__main__":
    main(mft_path)
