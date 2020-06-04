from .scale import scale
from copy import deepcopy

class scale_x_discrete(scale):
    """
    Scale x axis as discrete values

    Parameters
    ----------
    breaks: list
        maps to xbreaks
    labels: list, dict
        maps to xtick_labels

    Examples
    --------
    >>> print ggplot(mtcars, aes('mpg', 'qsec')) + \
    ...     geom_point() + \
    ...     scale_x_discrete(breaks=[10,20,30],  \
    ...     labels=["horrible", "ok", "awesome"])

    """
    VALID_SCALES = ['name', 'limits', 'labels', 'breaks', 'trans']
    def __radd__(self, gg):
        gg = deepcopy(gg)
        if self.name:
            gg.xlab = self.name
        if self.limits is not None:
            gg.xlimits = self.limits
        if self.breaks is not None:
            gg.xbreaks = self.breaks
        if self.labels is not None:
            gg.xtick_labels = self.labels
        return gg
