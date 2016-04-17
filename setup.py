from setuptools import setup, find_packages

setup(name='bookingsynclord',
      version='0.1',
      description='Custom implementation of BookingSync API for server and script use',
      url='https://github.com/lavief/bookingsynclord',
      author='Francois Lavie',
      author_email='francois.lavie@gmail.com',
      license='GNU',
      packages= ['bookingsynclord','bookingsynclord.entities','bookingsynclord.data_store','bookingsynclord.tools'],
      zip_safe=False)
