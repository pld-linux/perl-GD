%include	/usr/lib/rpm/macros.perl
Summary:	GD perl module
Summary(pl):	Modu³ perla GD
Name:		perl-GD
Version:	1.38
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GD-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	XFree86-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD - Interface to Gd Graphics Library.

%description -l pl
GD - interfejs do biblioteki Gd.

%prep
%setup -q -n GD-%{version}
%patch0 -p1

%build
echo -e "y\ny\ny\ny\n" |perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

cp -fa demos bdf_scripts \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/bdf_scripts/README \
	ChangeLog README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/GD.pm
%{perl_sitearch}/qd.pl
%dir %{perl_sitearch}/auto/GD
%{perl_sitearch}/auto/GD/autosplit.ix
%{perl_sitearch}/auto/GD/GD.bs
%attr(755,root,root) %{perl_sitearch}/auto/GD/GD.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
