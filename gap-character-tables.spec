%global upstreamver 1r2p1

Name:           gap-character-tables
Version:        %(echo %upstreamver | sed -r "s/r|p/./g")
Release:        1%{?dist}
Summary:        GAP Character Table Library

Group:          Sciences/Mathematics
License:        GPLv2+
URL:            http://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/
Source0:        http://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/ctbllib-%{upstreamver}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
Requires:       gap-table-of-marks
Provides:       gap-pkg-ctbllib = %{version}-%{release}

%description
This package provides the Character Table Library by Thomas Breuer.

%prep
%setup -q -n ctbllib

# Compress large tables
gzip --best data/*.tbl

%build
# Nothing to do

%install
mkdir -p $RPM_BUILD_ROOT%{_gap_dir}/pkg/ctbllib
cp -a data doc gap4 tst *.g $RPM_BUILD_ROOT%{_gap_dir}/pkg/ctbllib

%posttrans
    %{_bindir}/update-gap-workspace

%postun
    %{_bindir}/update-gap-workspace

%files
%doc README htm
%{_gap_dir}/pkg/ctbllib/

%changelog
* Thu Sep 13 2012 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream release

* Wed Jan  4 2012 Jerry James <loganjerry@gmail.com> - 1.1.3-1
- Initial RPM
