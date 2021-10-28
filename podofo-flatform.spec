
Summary: Utility to construct a PDF from a template and key/value pairs
Name: podofo-flatform
Version: 0.2
Release: 0
License: BSD
Group: Development/Libraries
URL: https://djaodjin.com/
Source: https://djaodjin.com/resources/srcs/podofo-flatform-%{version}.tar.bz2
Packager: Sebastien Mirolo <smirolo@djaodjin.com>

BuildRequires:  podofo-devel >= 0.9.3
Requires: podofo-libs  >= 0.9.3

%global debug_package %{nil}

%description
Utility to contruct a PDF from a template and key/value pairs

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} installTop=/usr

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/podofo-flatform

%changelog
* Tue Nov 30 2017 Sebastien Mirolo <smirolo@djaodjin.com> - 0.2-0
- prints list of available fields

* Tue Sep 6 2016 Sebastien Mirolo <smirolo@djaodjin.com> - 0.1-0
- Initial RPM release
