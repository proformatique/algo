def format_exception_numpy(etype, value, tb, limit=None):
    """
    Format the exception with a traceback.

    Parameters
    ----------
    etype : str
        exception type
    value : int
        exception value
    tb : traceback
        traceback object
    limit : int or None
        maximum number of stack frames to show

    Returns
    -------
    out : list of strings
        list of strings

    See Also
    --------
    numpy : a numerical package

    Notes
    -----
    This is an example of autodoc using numpydoc, the Numpy documentation format
    with the numpydoc extension [1]_

    This explanation of the column headers is not complete, for an exhaustive
    specification see [2]_.

    References
    ----------
    .. [1] `numpydoc <https://github.com/numpy/numpy/tree/master/doc/sphinxext>`_, \
        Numpy Documentation.
    .. [2] `Sphinx <http://sphinx-doc.org/domains.html#domains>`_, Sphinx Domains \
        Documentation.

    Examples
    --------
    >>> data = format_exception_numpy('dumb', 0, IOError)
    """
    return etype, value, tb