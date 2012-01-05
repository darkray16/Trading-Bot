"""
This module is created solely to contain a global variable
which will hold a region object to be used with the Python
with statement in setting a region context for find statements.

Example:
global_region.global_region = Region(etc, etc, etc, etc)
with global_region.global_region:
    find(needle, haystack)

"""
global_region = None
