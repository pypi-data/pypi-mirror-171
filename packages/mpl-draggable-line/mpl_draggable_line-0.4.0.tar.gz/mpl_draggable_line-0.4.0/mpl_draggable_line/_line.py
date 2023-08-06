from __future__ import annotations

from numbers import Real

import numpy as np
from matplotlib.backend_bases import MouseEvent
from matplotlib.cbook import CallbackRegistry
from matplotlib.lines import Line2D
from matplotlib.widgets import AxesWidget

__all__ = [
    "DraggableLine",
    "DraggableVLine",
    "DraggableHLine",
]


class DraggableLine(AxesWidget):
    def __init__(self, ax, x, y, grab_range=10, useblit=False, **kwargs) -> None:
        """
        Parameters
        ----------
        ax : Axes
        x, y : (2,) Array of float
            The initial positions of the handles.
        grab_range : float, default: .1
            Grab range for the handles in Axes coordinates [0,1]
        useblit : bool, default False
            Whether to use blitting for faster drawing (if supported by the
            backend). See the tutorial :doc:`/tutorials/advanced/blitting`
            for details.
        **kwargs :
            Passed on to Line2D for styling
        """
        super().__init__(ax)
        self._useblit = useblit
        center_x = (x[0] + x[1]) / 2
        center_y = (y[0] + y[1]) / 2
        self._y_lock = False
        self._x_lock = False
        self._orientation_lock = False

        marker = kwargs.pop("marker", "o")
        color = kwargs.pop("color", "k")
        transform = kwargs.pop("transform", self.ax.transData)
        self._handles = Line2D(
            [x[0], center_x, x[1]],
            [y[0], center_y, y[1]],
            marker=marker,
            color=color,
            transform=transform,
            **kwargs,
        )
        self.ax.add_artist(self._handles)
        self.connect_event("button_press_event", self._on_press)
        self.connect_event("motion_notify_event", self._on_move)
        self.connect_event("button_release_event", self._on_release)
        self._handle_idx = None  # none implies not moving
        self._grab_range = grab_range
        self._observers = CallbackRegistry()

    @property
    def lock_x(self) -> bool:
        return self._x_lock

    @lock_x.setter
    def lock_x(self, val: bool):
        if not isinstance(val, bool):
            raise TypeError("lock_x must be a bool")
        self._x_lock = val

    @property
    def lock_y(self) -> bool:
        return self._y_lock

    @lock_y.setter
    def lock_y(self, val: bool):
        if not isinstance(val, bool):
            raise TypeError("lock_y must be a bool")
        self._y_lock = val

    @property
    def lock_orientation(self) -> bool:
        return self._orientation_lock

    @lock_orientation.setter
    def lock_orientation(self, val: bool):
        if not isinstance(val, bool):
            raise TypeError("lock_orientation must be a bool")
        self._orientation_lock = val

    @property
    def grab_range(self) -> Real:
        """
        Grab range for the handles in Axes coordinates [0,1]
        """
        return self._grab_range

    @grab_range.setter
    def grab_range(self, val: Real):
        if not isinstance(val, Real):
            raise TypeError(f"Val must be a number but got type {type(val)}")
        self._grab_range = val

    def _on_press(self, event: MouseEvent):
        if self.ax != event.inaxes:
            return
        if not self.canvas.widgetlock.available(self):
            return
        # figure out if any handles are being grabbed
        # maybe possible to do this with a pick event?

        x, y = self._handles.get_data()
        # this is taken pretty much directly from the implementation
        # in matplotlib.widget.ToolHandles.closest
        pts = self.ax.transLimits.transform(np.column_stack([x, y]))
        diff = pts - self.ax.transLimits.transform((event.xdata, event.ydata))
        dist = np.hypot(*diff.T)
        idx = np.argmin(dist)
        if dist[idx] < self._grab_range:
            self._handle_idx = idx

        else:
            self._handle_idx = None

    def _on_move(self, event: MouseEvent):
        if self.ax != event.inaxes:
            return
        if self._handle_idx is None:
            # not dragging one of out handles
            return
        x, y = self._handles.get_data()
        if not self._x_lock:
            if self._orientation_lock or self._handle_idx == 1:
                x += event.xdata - x[self._handle_idx]
            else:
                x[self._handle_idx] = event.xdata
                x[1] = (x[0] + x[2]) / 2
        if not self._y_lock:
            if self._orientation_lock or self._handle_idx == 1:
                y += event.ydata - y[self._handle_idx]
            else:
                y[self._handle_idx] = event.ydata
                y[1] = (y[0] + y[2]) / 2
        self._handles.set_data(x, y)
        self._observers.process("line-changed", (x[0], x[2]), (y[0], y[2]))
        if self.drawon:
            self.ax.figure.canvas.draw_idle()

    def _on_release(self, event: MouseEvent):
        self._handle_idx = None

    def on_line_changed(self, func):
        """
        Connect *func* as a callback function whenever the line is moved.
        *func* will receive the end points of the line as (x, y) with each of x and y
        having shape (2,).

        Parameters
        ----------
        func : callable
            Function to call when a point is added.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect("line-changed", lambda *args: func(*args))

    def get_length(self) -> tuple[Real, Real]:
        """
        Get the current length of the line in data coordinates.

        Returns
        -------
        length : float
        """
        x, y = self._handles.get_data()
        return ((x[2] - x[0]) ** 2 + (y[2] - y[0]) ** 2) ** (1 / 2)

    def get_endpoints(self) -> tuple[list[float], list[float]]:
        """
        Get the current endpoints of the line.

        Returns
        -------
        x, y : (2,) arraylike of float
        """
        x, y = self._handles.get_data()
        return [x[0], x[2]], [y[0], y[2]]

    def set_endpoints(self, x: tuple[float, float], y: tuple[float, float]):
        """
        Set the endpoints of the line.

        Parameters
        ----------
        x, y : (2,) arraylike of float
        """
        self._handles.set_data(x, y)


class DraggableVLine(DraggableLine):
    def __init__(self, ax, x, grab_range=0.1, useblit=False, **kwargs) -> None:
        """
        A draggable line constrained to move horizontally.

        Parameters
        ----------
        ax : Axes
        x : float
            The initial position of the line.
        grab_range : float, default: .1
            Grab range for the handles in Axes coordinates [0,1]
        useblit : bool, default False
            Whether to use blitting for faster drawing (if supported by the
            backend). See the tutorial :doc:`/tutorials/advanced/blitting`
            for details.
        **kwargs :
            Passed on to Line2D for styling
        """
        super().__init__(
            ax,
            (x, x),
            (0, 1),
            grab_range=grab_range,
            useblit=useblit,
            transform=ax.get_xaxis_transform(),
            **kwargs,
        )
        self._y_lock = True
        self._orientation_lock = True

    def on_line_changed(self, func):
        """
        Connect *func* as a callback function whenever the line is moved.
        *func* will receive the x position the line as a float

        Parameters
        ----------
        func : callable
            Function to call when a point is added.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect("line-changed", lambda *args: func(args[0][0]))

    @property
    def lock_y(self) -> bool:
        return self._y_lock

    @lock_y.setter
    def lock_y(self, val: bool):
        raise ValueError("lock_y not settable on DraggableHLine")

    @property
    def lock_orientation(self) -> bool:
        return self._orientation_lock

    @lock_orientation.setter
    def lock_orientation(self, val: bool):
        raise ValueError("lock_orientation not settable on DraggableVLine")


class DraggableHLine(DraggableLine):
    def __init__(self, ax, y, grab_range=0.1, useblit=False, **kwargs) -> None:
        """
        A draggable line constrained to move vertically.

        Parameters
        ----------
        ax : Axes
        y : float
            The initial position of the line.
        grab_range : float, default: .1
            Grab range for the handles in Axes coordinates [0,1]
        useblit : bool, default False
            Whether to use blitting for faster drawing (if supported by the
            backend). See the tutorial :doc:`/tutorials/advanced/blitting`
            for details.
        **kwargs :
            Passed on to Line2D for styling
        """
        super().__init__(
            ax,
            (0, 1),
            (y, y),
            grab_range=grab_range,
            useblit=useblit,
            transform=ax.get_yaxis_transform(),
            **kwargs,
        )
        self._x_lock = True
        self._orientation_lock = True

    def on_line_changed(self, func):
        """
        Connect *func* as a callback function whenever the line is moved.
        *func* will receive the y position the line as a float

        Parameters
        ----------
        func : callable
            Function to call when a point is added.

        Returns
        -------
        int
            Connection id (which can be used to disconnect *func*).
        """
        return self._observers.connect("line-changed", lambda *args: func(args[1][0]))

    @property
    def lock_x(self) -> bool:
        return self._x_lock

    @lock_x.setter
    def lock_x(self, val: bool):
        raise ValueError("lock_x not settable on DraggableHLine")

    @property
    def lock_orientation(self) -> bool:
        return self._orientation_lock

    @lock_orientation.setter
    def lock_orientation(self, val: bool):
        raise ValueError("lock_orientation not settable on DraggableHLine")
