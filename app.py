from quickli import Application, Argument

from .lib.create_dir import create_directory_if_not_present
from .lib.switch_directories import switch_directories

app = Application(name="profile")


@app.entrypoint(
    arguments=[Argument("directory_name")]
)
def directory_creation_and_switching(directory_name: str) -> str:
    # TODO: implement. Import functions from '/lib/'
    # and use them correspondingly
    my_dir = create_directory_if_not_present(directory_name)
    switch_directories(my_dir)
    print(f"Switched to directory: {my_dir}")


if __name__ == "__main__":
    app.main()
