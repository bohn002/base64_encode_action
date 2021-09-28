import os


def main():
    env_name = os.environ['INPUT_ENV_NAME']
    export_var_name = os.environ['INPUT_EXPORT_VAR_NAME']
    data = os.environ[env_name]
    set_output(data)


def set_output(data):
    print(f"::set-output name=encoded_string::{data}", flush=True)


if __name__ == "__main__":
    main()
