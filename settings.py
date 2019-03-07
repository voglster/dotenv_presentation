from dotenv import load_dotenv

load_dotenv()

from os import getenv
from dotmap import DotMap


config = DotMap()

#your config here
config.user = getenv("USER", "King Roland")
config.pw = getenv("PASSWORD", "12345")



if __name__ == "__main__":
    with open(".env", "w") as f:
        for key, value in config.items():
            f.write(f"{str(key).upper()}={value}\n")
