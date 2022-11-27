import numpy as np

def show_values_on_bars(axs, perc=False, round_to=0):
    def _show_on_single_plot(ax):
        for p in ax.patches:
            if np.isnan(p.get_height()):
                continue
            _x = p.get_x() + p.get_width() / 2
            _y = p.get_y() + p.get_height()
            _h = p.get_height()
            value = _h * 100 if perc else _h
            value = round(value, round_to)
            value = str(int(value)) if round_to == 0 else str(value)
            ax.text(_x, _y, value, ha="center", fontsize=8)

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)
