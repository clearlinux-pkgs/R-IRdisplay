#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-IRdisplay
Version  : 0.7.0
Release  : 41
URL      : https://cran.r-project.org/src/contrib/IRdisplay_0.7.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/IRdisplay_0.7.0.tar.gz
Summary  : 'Jupyter' Display Machinery
Group    : Development/Tools
License  : MIT
Requires: R-cli
BuildRequires : R-assertthat
BuildRequires : R-cli
BuildRequires : R-repr
BuildRequires : R-rlang
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
IRdisplay [![b-Travis]][Travis] [![b-CRAN]][CRAN]
=========
[b-Travis]: https://travis-ci.org/IRkernel/IRdisplay.svg?branch=master "Build status"
[Travis]: https://travis-ci.org/IRkernel/IRdisplay
[b-CRAN]: https://www.r-pkg.org/badges/version/IRdisplay "Comprehensive R Archive Network"
[CRAN]: https://cran.r-project.org/package=IRdisplay

%prep
%setup -q -c -n IRdisplay

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552892529

%install
export SOURCE_DATE_EPOCH=1552892529
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library IRdisplay
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library IRdisplay
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library IRdisplay
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  IRdisplay || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/IRdisplay/DESCRIPTION
/usr/lib64/R/library/IRdisplay/INDEX
/usr/lib64/R/library/IRdisplay/LICENSE
/usr/lib64/R/library/IRdisplay/Meta/Rd.rds
/usr/lib64/R/library/IRdisplay/Meta/features.rds
/usr/lib64/R/library/IRdisplay/Meta/hsearch.rds
/usr/lib64/R/library/IRdisplay/Meta/links.rds
/usr/lib64/R/library/IRdisplay/Meta/nsInfo.rds
/usr/lib64/R/library/IRdisplay/Meta/package.rds
/usr/lib64/R/library/IRdisplay/NAMESPACE
/usr/lib64/R/library/IRdisplay/R/IRdisplay
/usr/lib64/R/library/IRdisplay/R/IRdisplay.rdb
/usr/lib64/R/library/IRdisplay/R/IRdisplay.rdx
/usr/lib64/R/library/IRdisplay/help/AnIndex
/usr/lib64/R/library/IRdisplay/help/IRdisplay.rdb
/usr/lib64/R/library/IRdisplay/help/IRdisplay.rdx
/usr/lib64/R/library/IRdisplay/help/aliases.rds
/usr/lib64/R/library/IRdisplay/help/paths.rds
/usr/lib64/R/library/IRdisplay/html/00Index.html
/usr/lib64/R/library/IRdisplay/html/R.css
/usr/lib64/R/library/IRdisplay/tests/testthat.R
/usr/lib64/R/library/IRdisplay/tests/testthat/test-options.r
/usr/lib64/R/library/IRdisplay/tests/testthat/test_base_display.r
/usr/lib64/R/library/IRdisplay/tests/testthat/test_display_functions.r
/usr/lib64/R/library/IRdisplay/tests/testthat/test_display_functions_images.r
/usr/lib64/R/library/IRdisplay/tests/testthat/test_display_functions_textual.r
