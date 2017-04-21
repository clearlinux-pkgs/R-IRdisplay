#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-IRdisplay
Version  : 0.4.4
Release  : 5
URL      : https://cran.r-project.org/src/contrib/IRdisplay_0.4.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/IRdisplay_0.4.4.tar.gz
Summary  : 'Jupyter' Display Machinery
Group    : Development/Tools
License  : MIT
Requires: R-repr
Requires: R-withr
BuildRequires : R-repr
BuildRequires : R-withr
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n IRdisplay

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492799043

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492799043
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library IRdisplay
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library IRdisplay


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
