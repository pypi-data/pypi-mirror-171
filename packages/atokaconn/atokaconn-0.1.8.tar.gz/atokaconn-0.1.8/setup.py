# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['atokaconn', 'atokaconn.cli']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=8.10.1,<9.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.25.1,<3.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['atokaconn = atokaconn.cli.main:app']}

setup_kwargs = {
    'name': 'atokaconn',
    'version': '0.1.8',
    'description': 'A package that facilitates connections to and data extractions from the ATOKA API service.',
    'long_description': "[![Latest Version](https://img.shields.io/pypi/v/atokaconn.svg)](https://pypi.python.org/pypi/atokaconn)\n[![Latest Version](https://img.shields.io/pypi/pyversions/atokaconn.svg)](https://pypi.python.org/pypi/atokaconn)\n[![License](https://img.shields.io/pypi/l/atokaconn.svg)](https://pypi.python.org/pypi/atokaconn)\n[![Downloads](https://pepy.tech/badge/atokaconn/month)](https://pepy.tech/project/atokaconn/month)\n\n[![Twitter Follow](https://img.shields.io/twitter/follow/openpolislab)](https://twitter.com/openpolislab)\n\n![Tests Badge](https://op-badges.s3.eu-west-1.amazonaws.com/atokaconn/tests-badge.svg?2)\n![Coverage Badge](https://op-badges.s3.eu-west-1.amazonaws.com/atokaconn/coverage-badge.svg?2)\n![Flake8](https://op-badges.s3.eu-west-1.amazonaws.com/atokaconn/flake8-badge.svg?2)\n\n\n`atokaconn` is a python package that allows connections to and data extractions from the \n[ATOKA](https://atoka.io/pages/en/) API service.\n\nATOKA is a service provided by SpazioDati (Cerved), based on companies' data from the \nCamera di Commercio.\n\nAn extensive introduction to these data's structure is available here: https://atoka.io/pages/en/data-structure/.\n\nThe API reference is available here: https://developers.atoka.io/v2/.\n\n## Installation\n\nPython versions from 3.6 are supported.\n\nThe package is hosted on pypi, and can be installed, for example using pip:\n\n    pip install atokaconn\n\n## Usage\n\nOnce a key has been obtained from ATOKA's service (you need to pay for this), then\n\n    from atokaconn import AtokaConn\n    atoka_conn = AtokaConn(key=MYKEY)\n    atoka_p = atoka_conn.get_person_from_tax_id(tax_id)\n \nATOKA has an incredibly rich set of endpoints and filters, allowing a wide variety of usages \nfor their API. This package implements a **very limited set of public methods** that facilitate\naccessing only part of all available information. \n\nSee https://gitlab.com/spaziodati/atoka-cli for a go-based CLI implementation.\n\nSee the Contributing section to increase coverage.\n\n### get_person_from_tax_id\nGets a single person, as a dict, from its tax_id. \nRaises one of the Atoka exceptions if errors are present or no persons are found.\nsee: https://developers.atoka.io/v2/people.html#people_taxIds\n\n### search_person\nRetrieves a single person from ATOKA API, starting from its anagraphical data.\nRaises Atoka exceptions if errors or no objects are found.\n \n`person` is an object instance of Popolo Person type to look for into ATOKA\n  Can be an instance of an object with these attributes:\n    - family_name,\n    - given_name,\n    - birth_date (YYYY[-MM][-DD])\n    - birth_location_area (object of Popolo Area type, an instance with a name attribute will do)\n\nTODO: this is not generic enough, as OPDM/Popolo concepts creeps in. Must be generalized.\n\n### get_people_from_atoka_ids\nReturns a list of dictionaries, with persons corresponding to the passed atoka ids.\n\n### get_people_from_tax_ids\nReturns a list of dictionaries, with persons corresponding to the passed tax ids\n\n### get_companies_from_atoka_ids\nReturns a list of dictionaries, with companies corresponding to the passed atoka ids.\n\n### get_companies_from_tax_ids\nReturns a list of dictionaries, with companies corresponding to the passed tax ids.\n\n### get_roles_from_atoka_ids\nReturns all people in companies with given atoka ids, used to extract people with roles in these companies\n\nMost of the above methods are based on the internal generic `get_items_from_ids`, which uses \n`posts_requests`, in order to correctly build the multipart *batch* post request.\n\nWhen extracting roles, we hit a 50 items limit, and the `extend_response` method must be used, in order to fetch \nitems when the returned count is greater than 50.   \n\n## Support\n\nThere is no guaranteed support available, but authors will try to keep up with issues \nand merge proposed solutions into the code base.\n\n## Project Status\nThis project is currently being developed by the [Openpolis Foundation](https://www.openpolis.it/openpolis-foundation/)\nand does only cover those parts of the ATOKA API that are needed in the Foundation's projects. \nShould more be needed, you can either ask to increase the coverage, or try to contribute, following instructions below.\n\n## Contributing\nIn order to contribute to this project:\n* verify that python 3.6+ is being used (or use [pyenv](https://github.com/pyenv/pyenv))\n* verify or install [poetry](https://python-poetry.org/), to handle packages and dependencies in a leaner way, \n  with respect to pip and requirements\n* clone the project `git clone git@github.com:openpolis/atokaconn.git` \n* install the dependencies in the virtualenv, with `poetry install`,\n  this will also install the dev dependencies\n* develop and test \n* create a [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)\n* wait for the maintainers to review and eventually merge your pull request into the main repository\n\n### Testing\nTests are under the tests folder, and can be launched with \n\n    pytest\n\nRequests and responses from ATOKA's API are mocked, in order to avoid having to connect to \nthe remote service during tests (slow and needs an API key).\n\nCoverage is installed as a dev dependency and can be used to see how much of the package's code is covered by tests:\n\n    coverage run -m pytest\n\n    # sends coverage report to terminal\n    coverage report -m \n\n    # generate and open a web page with interactive coverage report\n    coverage html\n    open htmlcov/index.html \n\nSyntax can be checked with `flake8`.\n\nCoverage and flake8 configurations are in their sections within `setup.cfg`.\n\n## Authors\nGuglielmo Celata - guglielmo@openpolis.it\n\n## Licensing\nThis package is released under an MIT License, see details in the LICENSE.txt file.\n",
    'author': 'guglielmo',
    'author_email': 'guglielmo@openpolis.it',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/openpolis/atokaconn/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
