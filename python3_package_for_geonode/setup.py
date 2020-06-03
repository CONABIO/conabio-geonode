from setuptools import setup, find_packages

setup(name="geonode_conabio",
      version="0.1",
      description=u"Simplify import of layers into geonode.conabio.gob.mx",
      url="https://github.com/CONABIO/geonode",
      author="CONABIO",
      author_email="",
      license="GPLv3",
      packages=['geonode_conabio'],
      #packages=find_packages(),
      entry_points = {
          'console_scripts': [
                             'import_raster=geonode_conabio.import_raster:main',
                             ]
                      }
      )
