from distutils.core import setup

setup(
    name='mockingbird',
    version='0.0.1',
    packages=[''],
    url='https://github.com/harnash/mockingbird',
    license='MIT',
    author='Łukasz Harasimowicz',
    author_email='lukasz@harnash.eu',
    description='',
    install_requires=[
        # 'flask==1.0.0', for now just install from github
        'nose==1.3.7',
        'Flask-Restless==0.17.0',
        'ujson==1.33',
        'flask-restful==0.3.4',
    ]
)
