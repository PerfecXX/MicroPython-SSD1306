import io
from os.path import abspath, dirname, join
import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
    name='micropython-ssd1306-driver',
    py_modules=['ssd1306'],
    version='1.0.2',
    description='MicroPython Library for SSD1306 OLED Displays with some simple shape drawing functions.',
    long_description=DESCRIPTION,
    keywords= ['oled','ssd1306', 'esp32','micropython'],
    url='https://github.com/PerfecXX/MicroPython-SSD1306',
    author='Teeraphat Kullanankanjana',
    author_email='ku.teeraphat@hotmail.com',
    maintainer='Teeraphat Kullanankanjana',
    maintainer_email='ku.teeraphat@hotmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 3 - Alpha', 
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)
