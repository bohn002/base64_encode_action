import os


def main():
    env_name = os.environ['INPUT_ENV_NAME']
    export_var_name = os.environ['INPUT_EXPORT_VAR_NAME']
    data = os.environ[env_name]
    os.environ[export_var_name] = data


def set_output(cmd):
    print(f"::set-output name=random_string::{cmd}", flush=True)


if __name__ == "__main__":
    main()
