%include	/usr/lib/rpm/macros.perl
Summary:	GD perl module
Summary(pl):	Modu� perla GD
Name:		perl-GD
Version:	1.33
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GD-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	XFree86-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	freetype1-devel
BuildRequires:	gd-devel >= 1.8.3
BuildRequires:	libjpeg-devel >= 6b
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD - Interface to Gd Graphics Library.

%description -l pl
GD - interfejs do biblioteki Gd.

%prep
%setup -q -n GD-%{version}
%patch0 -p1

%build
echo -e "y\ny\ny\n" |perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

cp -a demos bdf_scripts \
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
