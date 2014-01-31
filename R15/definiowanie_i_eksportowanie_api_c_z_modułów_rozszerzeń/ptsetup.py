# setup.py
from distutils.core import setup, Extension

setup(name="ptexample", 
      ext_modules=[
        Extension("ptexample",
                  ["ptexample.c"],
                  include_dirs = ['..','.'],  # Możliwe, że trzeba będzie podać katalog zawierający plik pysample.h
                  )
        ]
)
