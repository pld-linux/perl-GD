#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	GD - Interface to Gd Graphics Library
Summary(pl):	GD - interfejs do biblioteki graficznej Gd
Name:		perl-GD
Version:	2.02
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GD/GD-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-gif-support.patch
BuildRequires:	gd-devel >= 2.0.1
%{!?_without_gif:BuildRequires:	gd-devel(gif)}
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	XFree86-devel
Requires:	gd >= 2.0.1
%{!?_without_gif:Provides:	perl-GD(gif) = %{version}-%{release}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD.pm is a Perl interface to Thomas Boutell's gd graphics library
(version 2.0.1 or higher). GD allows you to create color drawings using
a large number of graphics primitives, and emit the drawings as PNG
files.

%description -l pl
GD.pm jest perlowym interfejsem do biblioteki graficznej gd Thomasa
Boutella (w wersji 2.0.1 lub wy¿szej). GD pozwala na tworzenie
kolorowych rysunków przy u¿yciu du¿ej liczby graficznych prymitywów
oraz zapisywanie ich w formacie PNG.

%prep
%setup -q -n GD-%{version}
%patch0 -p1
%{!?_without_gif:%patch1 -p1}

%build
%{__perl} Makefile.PL </dev/null
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}
# %{__make} test partially fails - reference pictures were generated
#   by some older version of gd

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{perl_sitelib}/GD}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -fa demos bdf_scripts \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/bdf_scripts/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README*
%{perl_sitearch}/GD.pm
%{perl_sitearch}/GD
%{perl_sitearch}/qd.pl
%dir %{perl_sitearch}/auto/GD
%{perl_sitearch}/auto/GD/autosplit.ix
%{perl_sitearch}/auto/GD/GD.bs
%attr(755,root,root) %{perl_sitearch}/auto/GD/GD.so
%dir %{perl_sitelib}/GD
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
