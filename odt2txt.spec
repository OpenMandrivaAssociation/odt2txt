Name:		odt2txt
Version:	0.4
Release:	6
Source0:	http://stosberg.net/odt2txt/odt2txt-%{version}.tar.gz
Source1:	http://stosberg.net/odt2txt/odt2txt-%{version}.tar.gz.asc
URL:		http://stosberg.net/odt2txt/
Summary:	A simple (and stupid) converter from OpenDocument Text to plain text
Group:		Text tools
License:	GPLv2
BuildRequires:	pkgconfig(zlib)

%description
odt2txt is a command-line tool which extracts the text out of OpenDocument
Texts produced by OpenOffice.org, StarOffice, KOffice and others.

odt2txt is ...
* small
* supports multiple output encodings
* adopts to your locale
* able to substitute common characters which the output charset does
  not contain with ascii look-a-likes
* written in C, has few dependencies
* portable (runs on Linux, *BSD, Solaris, HP-UX, Windows, Cygwin)
* licensed under GPL, version 2

%prep
%setup -q

%build
%setup_compile_flags
%make

%install
%makeinstall_std PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 13 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4-6
- cleanups

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdv2011.0
+ Revision: 666940
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdv2011.0
+ Revision: 607006
- rebuild

* Wed Dec 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.4-1mdv2010.1
+ Revision: 479513
- new version 0.4
- fix files list

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2010.0
+ Revision: 430195
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 254393
- rebuild
- fix no-buildroot-tag

* Wed Nov 14 2007 Funda Wang <fwang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 108812
- rebuild

* Wed Oct 31 2007 Nicolas Vigier <nvigier@mandriva.com> 0.3-1mdv2008.1
+ Revision: 104181
- import odt2txt


