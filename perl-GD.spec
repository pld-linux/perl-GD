%include	/usr/lib/rpm/macros.perl
Summary:	GD perl module
Summary(pl):	Modu³ perla GD
Name:		perl-GD
Version:	1.30
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GD-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	zlib-devel
BuildRequires:	freetype-devel
BuildRequires:	gd-devel >= 1.8.3
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GD - Interface to Gd Graphics Library.

%description -l pl
GD - interfejs do biblioteki Gd.

%prep
%setup -q -n GD-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a demos bdf_scripts \
	$RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/GD/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/GD
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
$RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}/bdf_scripts/README \
        ChangeLog README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README*}.gz

%{perl_sitearch}/GD.pm
%{perl_sitearch}/qd.pl

%dir %{perl_sitearch}/auto/GD
%{perl_sitearch}/auto/GD/.packlist
%{perl_sitearch}/auto/GD/autosplit.ix
%{perl_sitearch}/auto/GD/GD.bs
%attr(755,root,root) %{perl_sitearch}/auto/GD/GD.so

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}
