# read version from installed package
from importlib.metadata import version
from pycounts.plotting import plot_words

__version__ = version("pycounts")