%include	/usr/lib/rpm/macros.perl
Summary:	GD perl module
Summary(pl):	Modu� perla GD
Name:		perl-GD
Version:	1.23
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/GD/GD-%{version}.tar.gz
Patch0:		perl-GD-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRequires:	freetype-devel
BuildRequires:	gd-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GD - Interface to Gd Graphics Library.

%description -l pl
GD - interfejs do biblioteki Gd.

%prep
%setup -q -n GD-%{version}
%patch0 -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install DESTDIR=$RPM_BUILD_ROOT

cp -a demos bdf_scripts \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/GD/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/GD
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	$RPM_BUILD_ROOT/usr/src/examples/%{name}/bdf_scripts/README \
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

/usr/src/examples/%{name}
