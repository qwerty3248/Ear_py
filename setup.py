from cx_Freeze import setup, Executable

setup(
    name="Traductor",
    version="1.0",
    description="Traduce",
    executables=[Executable("hablar.py")],
)
