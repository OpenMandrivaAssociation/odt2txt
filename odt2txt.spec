Summary:	A simple (and stupid) converter from OpenDocument Text to plain text
Name:		odt2txt
Version:	0.5
Release:	1
Group:		Text tools
License:	GPLv2
Url:		http://stosberg.net/odt2txt/
Source0:	https://github.com/dstosberg/odt2txt/archive/refs/tags/v%{version}.zip
Patch0:		odt2txt-0.4-fwhole-program.patch 
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
%autopatch -p1

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{ldflags}" WHOLE_PROGRAM=1

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

