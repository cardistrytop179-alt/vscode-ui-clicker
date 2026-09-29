# VS Code UI Click Helper

Small Windows desktop automation experiment that locates a configured VS Code toolbar button from a reference image and clicks it with PyAutoGUI.

## Files

- `main_clicker.py` — image-based button search and click.
- `simple_clicker.py` — simplified click flow.
- `run.PNG`, `accept_all.PNG` — visual reference images used by the scripts.
- `check_dependencies.py` and `run_clicker.bat` — setup and launch helpers.

## Run

Install Python 3, then run `python check_dependencies.py` followed by `python main_clicker.py`, or use `run_clicker.bat`.

The script interacts with the visible desktop and can activate the wrong control if the screen layout differs from the reference images. Keep the target window visible and supervise every run. PyAutoGUI's fail-safe can stop the script when the pointer is moved to the upper-left corner.
