# tiny_2d_engine


![t2de](./td2e.png)

A Tk.Canevas widget augmented to allow 2D acquisitions:

1. load an image
2. Add a calibration for the image to set up your own world coordinates
3. Add Points or Lines on the image
4. Save your project. You will find the word coordinates of all your objects in the projects, ready for an other usage.

It can be used as a standaone application with:

```bash
> tiny_2d_engine gui
```

Or as a Tkinter widget like here:


```python
from tkinter import ttk
from tiny_2d_engine.main import Acquisition2D

def add_viewer_2d(otroot):
    """Injection of a viewer 2D to opentea"""
    title = "2D dialog"
    view2d_fr = ttk.Frame(otroot.notebook, name=title)
    otroot.notebook.add(view2d_fr, text=title)
    viewer = Viewer2D(
        view2d_fr,
        otroot,
    )
    return viewer


class Viewer2D(Acquisition2D):
    def __init__(self, master, otroot):
        super().__init__(master, standalone=True)
        self.pack( side="top")
        self.otroot = otroot

    def get(self):
        print("get data")
        return self.acq_canvas.as_dict()

    def set(self, data: dict):
        print("set data")
        self.acq_canvas.load_dict(data)
```

## Disclaimer

This package is very young and uncomplete.

Known issues are:

- A spurious contextual menu pops up sometimes
- Changing image can fail
- Moving the calibration around is quickly perturbating the acquisitions (You are not supposed to do that!)

But it works somehow. 