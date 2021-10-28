# Hacky unofficial spec file to generate RPMs for podofo 0.9.7

Name:           podofo
Version:        0.9.7
Release:        18%{?dist}
Summary:        Tools and libraries to work with the PDF file format

Group:          Applications/Publishing
License:        GPLv2+
URL:            http://podofo.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 2.5
BuildRequires:  doxygen
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libidn-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libpng-devel
BuildRequires:  cppunit-devel
BuildRequires:  lua-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel


%description
PoDoFo is a library to work with the PDF file format. The name comes from
the first letter of PDF (Portable Document Format). A few tools to work
with PDF files are already included in the PoDoFo package.

The PoDoFo library is a free, portable C++ library which includes classes
to parse PDF files and modify their contents into memory. The changes can be
written back to disk easily. The parser can also be used to extract
information from a PDF file (for example the parser could be used in a PDF
viewer). Besides parsing PoDoFo includes also very simple classes to create
your own PDF files. All classes are documented so it is easy to start writing
your own application using PoDoFo.


%package libs
Summary:        Runtime library for %{name}
Group:          System Environment/Libraries
License:        LGPLv2+

%description libs
Runtime library for %{name}.


%package devel
Summary:        Development files for %{name} library
Group:          Development/Libraries
License:        LGPLv2+
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Development files and documentation for the %{name} library.


%prep
%setup -q

# disable timestamps in docs
echo "HTML_TIMESTAMP = NO" >> Doxyfile


%build
%cmake -DPODOFO_BUILD_SHARED=1 \
%if 0%{?__isa_bits} == 64
-DWANT_LIB64=1 \
%endif
.
make %{?_smp_mflags}

# build the docs
doxygen

# set timestamps on generated files to some constant
find doc/html -exec touch -r %{SOURCE0} {} \;


%install
make install DESTDIR=$RPM_BUILD_ROOT


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig


%files
%doc COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.1*

%files libs
%doc AUTHORS COPYING.LIB ChangeLog FAQ.html README.html TODO
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/libpodofo-0.pc

%files devel
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/*.so


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.9.1-15
- Fix FTBFS on aarch64 (#1111745)

* Tue Jun 10 2014 Dan Horák <dan[at]danny.cz> - 0.9.1-14
- fix FTBFS (#1106651)
- spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 20 2013 Dan Horák <dan[at]danny.cz> - 0.9.1-12
- fix build with Lua 5.2 (#992811)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.9.1-9
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.9.1-8
- rebuild against new libjpeg

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 03 2012 Dan Horák <dan[at]danny.cz> - 0.9.1-6
- disable timestamps in docs (#565683)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Dan Horák <dan[at]danny.cz> - 0.9.1-4
- build fix for unistd.h

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.1-2
- Rebuild for new libpng

* Thu Apr 28 2011 Dan Horák <dan[at]danny.cz> 0.9.1-1
- updated to 0.9.1

* Thu Apr 14 2011 Dan Horák <dan[at]danny.cz> 0.9.0-1
- updated to 0.9.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  2 2010 Dan Horák <dan[at]danny.cz> 0.8.4-1
- updated to 0.8.4

* Fri Oct 22 2010 Dan Horák <dan[at]danny.cz> 0.8.3-1
- updated to 0.8.3

* Tue Jun  8 2010 Dan Horák <dan[at]danny.cz> 0.8.1-2
- fix building tests

* Mon Jun  7 2010 Dan Horák <dan[at]danny.cz> 0.8.1-1
- updated to 0.8.1

* Thu Apr 29 2010 Dan Horák <dan[at]danny.cz> 0.8.0-1
- updated to 0.8.0

* Tue Feb 16 2010 Dan Horák <dan[at]danny.cz> 0.7.0-4
- set timestamp on generated docs (#565683)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 30 2009 Dan Horák <dan[at]danny.cz> 0.7.0-2
- remove BR: openssl-devel, it could be required in the future (but then
    an exception clause will be added to the licenses)
- add missing doc files

* Sun Mar 29 2009 Dan Horák <dan[at]danny.cz> 0.7.0-1
- initial Fedora package
