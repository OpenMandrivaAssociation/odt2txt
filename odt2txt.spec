Name:		odt2txt
Version:	0.4
Release:	%mkrel 3
Source0:	http://stosberg.net/odt2txt/odt2txt-%{version}.tar.gz
Source1:	http://stosberg.net/odt2txt/odt2txt-%{version}.tar.gz.asc
URL:		http://stosberg.net/odt2txt/
Summary:	A simple (and stupid) converter from OpenDocument Text to plain text
Group:		Text tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2
BuildRequires:	zlib-devel
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
%{make}

%install
%{__rm} -Rf %{buildroot}
%{__make} DESTDIR=%{buildroot} PREFIX=%{_prefix} install

%files
%doc GPL-2
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
