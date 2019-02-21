Semi-automated Curation Results
===============================
This repository contains the results of semi-automated curation in the Human Brain Pharmacome project.

Installation
------------
This repository requires a particular package structure and can currently only be installed with pip in development
mode using the following command:

.. code-block:: sh

    $ git clone https://github.com/pharmacome/semi-automated-curation.git
    $ cd semi-automated-curation
    $ pip install -e .

It can be imported and used with the following. Note that it installs at a different name than the GitHub repository.

.. code-block:: python

    >>> from hbp_semi_automated_curation import repository
    >>> graph = repository.get_graph()
    >>> graph.summarize()

License
-------
- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.

Acknowledgements
----------------
This work was done during the `Human Brain Pharmacome project <https://pharmacome.scai.fraunhofer.de>` funded by the
Fraunhofer Society's MAVO program.
