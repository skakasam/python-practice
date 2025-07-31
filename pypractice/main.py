"""Hello Python"""

import os
from common.project import create_project


if __name__ == "__main__":
    print(create_project(os.getcwd() + "/ref/taking_python_to_production.ref"))
