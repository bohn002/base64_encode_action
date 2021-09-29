import os
from base64 import b64encode


def main():
    env_name = os.environ['INPUT_ENV_NAME']
    data = os.environ[env_name]
    set_output(str(b64encode(data.encode())))


def set_output(data):
    print(f"::add-mask::{data}", flush=True)
    print(f"::set-output name=encoded_string::{data}", flush=True)


if __name__ == "__main__":
    main()
