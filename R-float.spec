#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-float
Version  : 0.2.6
Release  : 7
URL      : https://cran.r-project.org/src/contrib/float_0.2-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/float_0.2-6.tar.gz
Summary  : 32-Bit Floats
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-float-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
(double precision) vectors/matrices. However, sometimes single precision (or
    less!) is more than enough for a particular task.  This package extends R's
    linear algebra facilities to include 32-bit float (single precision) data.
    Float vectors/matrices have half the precision of their "numeric"-type
    counterparts but are generally faster to numerically operate on, for a
    performance vs accuracy trade-off.  The internal representation is an S4
    class, which allows us to keep the syntax identical to that of base R's.
    Interaction between floats and base types for binary operators is generally
    possible; in these cases, type promotion always defaults to the higher
    precision.  The package ships with copies of the single precision 'BLAS' and
    'LAPACK', which are automatically built in the event they are not available
    on the system.

%package lib
Summary: lib components for the R-float package.
Group: Libraries

%description lib
lib components for the R-float package.


%prep
%setup -q -c -n float
cd %{_builddir}/float

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632184481

%install
export SOURCE_DATE_EPOCH=1632184481
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library float
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library float
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library float
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc float || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/float/CITATION
/usr/lib64/R/library/float/DESCRIPTION
/usr/lib64/R/library/float/INDEX
/usr/lib64/R/library/float/LICENSE
/usr/lib64/R/library/float/Meta/Rd.rds
/usr/lib64/R/library/float/Meta/data.rds
/usr/lib64/R/library/float/Meta/features.rds
/usr/lib64/R/library/float/Meta/hsearch.rds
/usr/lib64/R/library/float/Meta/links.rds
/usr/lib64/R/library/float/Meta/nsInfo.rds
/usr/lib64/R/library/float/Meta/package.rds
/usr/lib64/R/library/float/Meta/vignette.rds
/usr/lib64/R/library/float/NAMESPACE
/usr/lib64/R/library/float/R/float
/usr/lib64/R/library/float/R/float.rdb
/usr/lib64/R/library/float/R/float.rdx
/usr/lib64/R/library/float/benchmarks/cov.r
/usr/lib64/R/library/float/benchmarks/lmfit.r
/usr/lib64/R/library/float/benchmarks/prcomp.r
/usr/lib64/R/library/float/data/Rdata.rdb
/usr/lib64/R/library/float/data/Rdata.rds
/usr/lib64/R/library/float/data/Rdata.rdx
/usr/lib64/R/library/float/doc/float.Rnw
/usr/lib64/R/library/float/doc/float.pdf
/usr/lib64/R/library/float/doc/index.html
/usr/lib64/R/library/float/help/AnIndex
/usr/lib64/R/library/float/help/aliases.rds
/usr/lib64/R/library/float/help/float.rdb
/usr/lib64/R/library/float/help/float.rdx
/usr/lib64/R/library/float/help/paths.rds
/usr/lib64/R/library/float/html/00Index.html
/usr/lib64/R/library/float/html/R.css
/usr/lib64/R/library/float/include/float/float32.h
/usr/lib64/R/library/float/include/float/slapack.h
/usr/lib64/R/library/float/libs/libfloat.a
/usr/lib64/R/library/float/tests/arithmetic.r
/usr/lib64/R/library/float/tests/backsolve.r
/usr/lib64/R/library/float/tests/bind.r
/usr/lib64/R/library/float/tests/c.r
/usr/lib64/R/library/float/tests/chol.r
/usr/lib64/R/library/float/tests/chol2inv.r
/usr/lib64/R/library/float/tests/colSums.r
/usr/lib64/R/library/float/tests/comparison.r
/usr/lib64/R/library/float/tests/cond.r
/usr/lib64/R/library/float/tests/crossprod.r
/usr/lib64/R/library/float/tests/diag.r
/usr/lib64/R/library/float/tests/eigen.r
/usr/lib64/R/library/float/tests/extremes.r
/usr/lib64/R/library/float/tests/isSymmetric.r
/usr/lib64/R/library/float/tests/math.r
/usr/lib64/R/library/float/tests/matmult.r
/usr/lib64/R/library/float/tests/na.r
/usr/lib64/R/library/float/tests/norm.r
/usr/lib64/R/library/float/tests/print.r
/usr/lib64/R/library/float/tests/qr.r
/usr/lib64/R/library/float/tests/rand.r
/usr/lib64/R/library/float/tests/rep.r
/usr/lib64/R/library/float/tests/scale.r
/usr/lib64/R/library/float/tests/sign.r
/usr/lib64/R/library/float/tests/solve.r
/usr/lib64/R/library/float/tests/sum.r
/usr/lib64/R/library/float/tests/svd.r
/usr/lib64/R/library/float/tests/sweep.r
/usr/lib64/R/library/float/tests/xpose.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/float/libs/float.so
/usr/lib64/R/library/float/libs/float.so.avx2
/usr/lib64/R/library/float/libs/float.so.avx512
