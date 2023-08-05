CHANGELOG file
--------------

The rules for MAICoS' CHANGELOG file:

- entries are sorted newest-first.
- summarize sets of changes (don't reproduce every git log comment here).
- don't ever delete anything.
- keep the format consistent (79 char width, Y/M/D date format) and do not
  use tabs but use spaces for formatting

.. inclusion-marker-changelog-start


v0.6.1 (2022/10/10)
-----------------
Henrik Jaeger

- Fix the output to display the actual arguments (!173)
- `Chemicalpotentialplanar` uses the new output interface (!173)
- Fix confusing argument behaviour of zpos and center in
  `Chemicalpotentialplanar` (!173)

v0.6 (2022/09/01)
-----------------
Philip Loche, Simon Gravelle, Srihas Velpuri, Henrik Jaeger,
Alexander Schlaich, Maximilian Becker, Kira Fischer

- Write total epsilon as defined in paper (!155)
- Introduce generic header (!149)
- Fix error estimate in `EpsilonPlanar` (!153)
- Fix sym option in `EpsilonPlanar` (!148)
- Use standard error of the mean instead of variance for error estimate (!147)
- Make all tests that write file use temporary file directory (!151)
- Rewrite `Velocity` module using `ProfilePlanarBase` (!142)
- Add `RDFPlanar` (!133)
- Refactor `EpsilonPlanar` (!139)
- Add a correlation time estimator (!137)
- Add `frame` dict to `AnalysisBase` (!138)
- Generalize `comgroup` attribute to all dimensions (!132)
- Output headers do not require residue names anymore (!134)
- Remove `Debyer` class (!130)
- Generalize `concfreq` attribute in `AnalysisBase` (!122)
- Fix broken binning in `EpsilonPlanar` (!125)
- Removed `repairMolecules` (!119)
- Added `grouping` and `binmethod` option (!117)
- Bump minimum MDAnalysis version to 2.2.0 (!117)
- Bump minimum Python version to 3.8 (!117)
- Use base units exclusively (!115)
- Higher tolerance for non-neutral systems (1E-4 instead of 1E-5)
- `charge`neutral decorator uses `check_compound` now
- Add option to symmetrize profiles using `ProfilePlanarBase` (!116)
- Fix `comgroup` parameter working only in the z direction (!116)
- Remove `center` option from `ProfileBase` (!116)
- Introduces new `ProfilePlanarBase` (!111)
- Split new `DensityPlanar` into `ChemicalPotentialPlanar`, `DensityPlanar`,
  `TemperaturePlanar` (!111)
- Convert more `print` statements into logger calls (!111)
- Fix wrong `Diporder` normalization + tests (!111)
- Add `zmin` and `zmax` to DensityPlanar and Diporder (!109)
- Fix EpsilonPlanar (!108)
- More tests for `DensityPlanar`, `DensityCylinder`, `KineticEnergy` and
  `DipoleAngle` (!104)
- Remove `EpsilonBulk` (!107)
- Add Code of Conduct (!97)
- Fix lint errors (!95)

v0.5.1 (2022/02/21)
-------------------
Henrik Jaeger

- Fix pypi installation (!98)

v0.5 (2022/02/17)
-----------------
Philip Loche, Srihas Velpuri, Simon Gravelle

- Convert Tutorials into notebooks (!93)
- New docs design (!93)
- Build gitlab docs only on master branch (!94, #62)
- Removed oxygen binning from diporder (!85)
- Improved CI including tests for building and linting
- Create a consistent value of `zmax`` in every frame (!79)
- Corrected README for pypi (!83)
- Use Results class for attributes and improved docs (!81)
- Bump minimum Python version to 3.7 (!80)
- Remove spaghetti code in `__main__.py`` and introduce `mdacli` as
  cli server library. (!80)
- Remove `SingleGroupAnalysisBase` and `MultiGroupAnalysisBase`` classes in
  favour of a unified `AnalysisBase`` class (!80)
- Change `planar_base`` decorator to a `PlanarBase`` class (!80)
- Rename modules to be consistent with PEP8
  (`density_planar`` -> `DensityPlanar``) (!80)
- Use Numpy's docstyle for doc formatting (!80)
- Use Python's powerful logger library instead of bare `print` (!80)
- Use Python 3.6 string formatting (!80)
- Remove `_calculate_results`` methods. This method is covered by the
  `_conclude` method. (!80)
- Make results saving a public function (save) (!80)
- Added docstring Decorator for `PlanarDocstring` and `verbose` option (!80)
- Use `MDAnalysis`'s' `center_of_mass` function for center of
  mass shifting (!80)


v0.4.1 (2021/12/17)
-------------------
Philip Loche

- Fixed double counting of the box length in diporder (#58, !76)

v0.4 (2021/12/13)
-----------------

Philip Loche, Simon Gravelle, Philipp Staerk, Henrik Jaeger,
Srihas Velpuri, Maximilian Becker

- Restructure docs and build docs for develop and release version
- Include README files into sphinx doc
- Add tutorial for density_cylinder module
- Add `planar_base` decorator unifying the syntax for planar analysis modules
  as `denisty_planar`, `epsilon_planar` and `diporder` (!48)
- Corrected time_series module and created a test for it
- Added support for Python 3.9
- Created sphinx documentation
- Raise error if end is to small (#40)
- Add sorting of atom groups into molecules, enabling import of LAMMPS data
- Corrected plot format selection in `dielectric_spectrum` (!66)
- Fixed box dimension not set properly (!64)
- Add docs for timeseries modulees (!72)
- Fixed diporder does not compute the right quantities (#55, !75)
- Added support of calculating the chemical potentials for multiple atomgroups.
- Changed the codes behaviour of calculating the chemical potential if
  atomgroups contain multiple residues.

v0.3 (2020/03/03)
-----------------

Philip Loche, Amanuel Wolde-Kidan

- Fixed errors occurring from changes in MDAnalysis
- Increased minimal requirements
- Use new ProgressBar from MDAnalysis
- Increased total_charge to account for numerical inaccuracy

v0.2 (2020/04/03)
-----------------

Philip Loche

- Added custom module
- Less noisy DeprecationWarning
- Fixed wrong center of mass velocity in velocity module
- Fixed documentation in diporder for P0
- Fixed debug if error in parsing
- Added checks for charge neutrality in dielectric analysis
- Added test files for an air-water trajectory and the diporder module
- Performance tweaks and tests for sfactor
- Check for molecular information in modules

v0.1 (2019/10/30)
-----------------

Philip Loche

- first release out of the lab

.. inclusion-marker-changelog-end
