.. {{cookiecutter.project_name}} documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{cookiecutter.welcome}}

.. toctree::
   :maxdepth: 2
   :glob:

   topics/{{cookiecutter.project_name}}
   tutorial/index
   releases/index

.. toctree::
   :caption: Get Involved
   :maxdepth: 2
   :glob:

   topics/contributing
   topics/license
   Project Repository <https://gitlab.com/saltstack/pop/pop-create/>

Indices and tables
==================

* :ref:`modindex`
