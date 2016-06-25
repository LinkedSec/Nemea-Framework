from distutils.core import setup, Extension

pytrapmodule = Extension('pytrap',
                    sources = ['pytrapmodule.c', 'unirecmodule.c', 'fields.c'],
                    libraries = ['trap', 'unirec'])

setup(name = 'pytrap',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [pytrapmodule],
       py_modules = ['URWrapper'])

