# -*- coding: utf-8 -*-

"""This script converts the curation sheets to BEL."""

import os

from bel_enrichment import BELSheetsRepository
from bel_repository import BELMetadata
from bel_repository.utils import serialize_authors

__all__ = [
    'AUTHORS',
    'metadata',
    'repository',
    'main',
]

AUTHORS = [
    'Charles Tapley Hoyt',
    'Daniel Domingo-Fernández',
    'Esther Wollert',
    'Sandra Spalek',
    'Keerthika Lohanadan',
    'Rana Al Disi',
    'Lingling Xu',
    'Kristian Kolpeja',
]

AUTHOR_STRING = serialize_authors(AUTHORS)

# Folder pointers
HERE = os.path.abspath(os.path.dirname(__file__))
CURATION_DIRECTORY = os.path.join(HERE, 'curation')

VERSION = '0.1.1'

metadata = BELMetadata(
    name='HBP Semi-Automated Curation',
    version=VERSION,
    description="This knowledge graph contains content generated with the semi-automated curation workflow"
                "in the Human Brain Pharmacome project.",
    authors=AUTHOR_STRING,
    contact='charles.hoyt@scai.fraunhofer.de',
    license='CC BY 4.0',
)

repository = BELSheetsRepository(
    directory=CURATION_DIRECTORY,
    output_directory=HERE,
    metadata=metadata,
)

main = repository.build_cli()
