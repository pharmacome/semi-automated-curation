Semi-Automated Curation Results
===============================
This repository contains the results of semi-automated curation in the Human Brain Pharmacome project.

Installation
------------
This repository can be installed from GitHub using pip with the following command:

.. code-block:: sh

    $ pip install git+https://github.com/pharmacome/semi-automated-curation.git

For developers, this repository can be cloned and installd with the following commands:

.. code-block:: sh

    $ git clone https://github.com/pharmacome/semi-automated-curation.git hbp-semi-automated-curation
    $ cd hbp-semi-automated-curation
    $ pip install -e .

Usage
-----
It can be imported and used with the following. Note that it installs at a different name than the GitHub repository.

.. code-block:: python

    >>> from hbp_semi_automated_curation import repository
    >>> graph = repository.get_graph()
    >>> graph.summarize()

Content
-------
The curation can be found in the `src/curation` folder.

License
-------
- BEL scripts in this repository are licensed under the CC BY 4.0 license.
- Python source code in this repository is licensed under the MIT license.

Acknowledgements
----------------
This work was done during the `Human Brain Pharmacome project <https://pharmacome.scai.fraunhofer.de>`_ funded by the
Fraunhofer Society's MAVO program.
