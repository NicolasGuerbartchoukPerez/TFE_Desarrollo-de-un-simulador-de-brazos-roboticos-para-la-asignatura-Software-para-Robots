# Robotic Software Simulator
<p align="center">
  <img src="assets/logo.svg" width="200" alt="Simulator Robotic Software logo">
</p>

## Simulator for Linear Actuator and Mobile Robots (using Arduino)
This simulator is an Arduino simulator for robots, those being:
- Linear Actuator, which is composed by a servo, a joystick and two buttons acting as path limiters.
- Mobile robot, composed by two servos which will move the wheels, an ultrasonic sensor and, depending on the case:
    - Two infrared sensors: This robot is thought to be used in path following cases.
    - Four infrared sensors: This robot is thought to be used in labyrinth solving.

This system is designed with the intent to allow the development of new robots and libraries. In fewer words, it can be expanded with more robots and more Arduino code (not only libraries, but further Arduino syntax).

# Getting the simulator
## Binary downloads
Official binaries for the simulator can be found [here](https://github.com/diegofs29/simulator-robotic-software/releases).

## Generate executable
There are two ways of generating the program's executable. First one is by calling the build.py module:

`python build.py`

The alternative way is by using [Pyinstaller](https://pyinstaller.org/en/stable/) on a command prompt:

`pyinstaller main.spec`

Both ways, a build and a dist folder will be created. It is under the second one where the application's folder will be found. In this folder you can find the executable for the application. If opened, it will show two windows, a console and the program itself.

## SonarQube coverage
The repository now includes the base configuration needed for SonarQube to import Python test coverage from CI-based analysis.

Install the CI and coverage dependencies:

`python -m pip install -r requirements-sonar.txt`

Generate the coverage report before running the Sonar scanner:

`python -m coverage run --rcfile=.coveragerc -m pytest`

`python -m coverage xml -o coverage.xml`

The generated `coverage.xml` file is referenced by `sonar-project.properties` through `sonar.python.coverage.reportPaths=coverage.xml`.

Important notes:
- Coverage import is only supported by SonarQube Cloud when the project uses CI-based analysis, not automatic analysis.
- The Sonar scanner step must run after the two commands above so it can upload `coverage.xml`.
- Test files under `simulator/` and `simulator/tests/` are marked as tests for Sonar and excluded from the coverage target itself.
- The repository includes `.github/workflows/sonar.yml`, which runs tests, generates `coverage.xml`, uploads it as an artifact, and launches the SonarQube scan.
- The workflow expects two GitHub repository variables: `SONAR_PROJECT_KEY` and `SONAR_ORGANIZATION`, plus the secret `SONAR_TOKEN`.
- The ANTLR runtime is pinned to `4.11.1` in CI because the generated parser files in `simulator/compiler/` were created with ANTLR `4.11.1`.

# License
This program is distributed under the [GNU General Public License Version 3](https://github.com/diegofs29/simulator-robotic-software/blob/main/LICENSE)
