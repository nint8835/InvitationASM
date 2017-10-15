import os

__all__ = list(map(lambda x: x[:-3], filter(lambda x: x.endswith(".py"), os.listdir("extensions/"))))
