#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	GD - interface to Gd graphics library
Summary(pl):	GD - interfejs do biblioteki graficznej Gd
Name:		perl-GD
Version:	2.15
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GD/GD-%{version}.tar.gz
# Source0-md5:	8afc6be5a7a5be545840ff11fb3b02cf
Patch0:		%{name}-paths.patch
BuildRequires:	XFree86-devel
BuildRequires:	gd-devel >= 2.0.28
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gd >= 2.0.28
Provides:	perl-GD(gif) = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD.pm is a Perl interface to Thomas Boutell's gd graphics library. GD
allows you to create color drawings using a large number of graphics
primitives, and emit the drawings as PNG files.

%description -l pl
GD.pm jest perlowym interfejsem do biblioteki graficznej gd Thomasa
Boutella. GD pozwala na tworzenie kolorowych rysunków przy u¿yciu
du¿ej liczby graficznych prymitywów oraz zapisywanie ich w formacie
PNG.

%prep
%setup -q -n GD-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{perl_vendorlib}/GD}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -fa demos bdf_scripts \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/bdf_scripts/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README*
%{perl_vendorarch}/GD.pm
%{perl_vendorarch}/GD
%{perl_vendorarch}/qd.pl
%dir %{perl_vendorarch}/auto/GD
%{perl_vendorarch}/auto/GD/autosplit.ix
%{perl_vendorarch}/auto/GD/GD.bs
%attr(755,root,root) %{perl_vendorarch}/auto/GD/GD.so
%dir %{perl_vendorlib}/GD
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
