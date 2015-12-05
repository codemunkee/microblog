from distutils.core import setup

setup(
    name='microblog',
    version='0.0.1',
    packages=['microblog'],
    url='',
    license='',
    author='Russ Nealis',
    author_email='codemunkee@gmail.com',
    description='API for somecards App',
    install_requires=['flask',
                      'flask-login',
                      'flask-openid',
                      'flask-mail',
                      'flask-sqlalchemy',
                      'sqlalchemy',
                      'sqlalchemy-migrate',
                      'flask-whooshalchemy',
                      'flask-wtf',
                      'flask-babel',
                      'guess_language',
                      'flipflop',
                      'coverage']
)